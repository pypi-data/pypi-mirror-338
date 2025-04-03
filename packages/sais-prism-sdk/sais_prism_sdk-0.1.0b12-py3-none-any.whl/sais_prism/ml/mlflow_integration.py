from typing import Any, Dict, List
from pytorch_lightning.callbacks import Callback
from transformers import TrainerCallback
from ..core.config import ConfigManager
import os
import time
import threading
import queue

class MLflowManager(Callback, TrainerCallback):
    """MLflow integration manager that acts as both a PyTorch Lightning callback and Transformers callback"""

    def __init__(self, experiment_name: str, experiment_description: Any = None, config: Any=None, mlflow: Any=None) -> None:
        super().__init__()
        self.url = "http://mlflow.internal.sais.com.cn"
        self.experiment_name = experiment_name
        self.experiment_description = experiment_description
        self.ml_config = config
        self.config = ConfigManager()
        self.mlflow = mlflow
        
        # Add metrics recording tracking
        self.logged_epochs = set()
        self.pending_logs = queue.Queue()
        self.log_worker_active = False
        self.log_worker = None
        self.max_retries = 3
        self.retry_delay = 1.0  # Retry interval in seconds

        if self.ml_config.security.enabled:
            # enable authentication
            username = getattr(self.ml_config.security, 'username', '')
            password = str(getattr(self.ml_config.security, 'password', ''))
            os.environ["MLFLOW_TRACKING_USERNAME"] = username
            os.environ["MLFLOW_TRACKING_PASSWORD"] = password
        self.mlflow.set_tracking_uri(self.url)
        self.mlflow.set_experiment(experiment_name)
        self.system_tracing(self.ml_config.system_tracing)
        self.mlflow.autolog()
        
        # Start asynchronous logging thread
        self._start_log_worker()

    def _start_log_worker(self):
        """Start asynchronous logging thread"""
        if not self.log_worker_active:
            self.log_worker_active = True
            self.log_worker = threading.Thread(target=self._process_log_queue, daemon=True)
            self.log_worker.start()
            
    def _process_log_queue(self):
        """Worker thread for processing log queue asynchronously"""
        while self.log_worker_active:
            try:
                if self.pending_logs.empty():
                    time.sleep(0.1)  # Avoid busy waiting
                    continue
                    
                log_item = self.pending_logs.get(timeout=0.5)
                if log_item is None:  # End signal
                    break
                    
                log_type, data, step = log_item
                
                for attempt in range(self.max_retries):
                    try:
                        if log_type == "metrics":
                            self.mlflow.log_metrics(data, step=step)
                            if step is not None:  # If epoch-level metrics
                                self.logged_epochs.add(step)
                        elif log_type == "params":
                            self.mlflow.log_params(data)
                        elif log_type == "artifacts":
                            if isinstance(data, list):
                                for artifact in data:
                                    self.mlflow.log_artifacts(artifact)
                            else:
                                self.mlflow.log_artifacts(data)
                        break  # Exit retry loop after successful logging
                    except Exception as e:
                        if attempt == self.max_retries - 1:
                            print(f"Failed to log {log_type} after {self.max_retries} attempts: {e}")
                        else:
                            print(f"Attempt {attempt+1} to log {log_type} failed, retrying: {e}")
                            time.sleep(self.retry_delay)
                            
                self.pending_logs.task_done()
            except Exception as e:
                print(f"Error in log worker thread: {e}")
                time.sleep(0.5)  # Brief pause when error occurs

    # PyTorch Lightning callback methods - these have to match the PL interface
    def on_fit_start(self, trainer, pl_module):
        """Called when fit begins"""
        self.init_run()

    def on_train_batch_end(self, trainer, pl_module, outputs, batch, batch_idx):
        """Called when the train batch ends, log metrics if available"""
        if hasattr(outputs, "get") and isinstance(outputs, dict) and "loss" in outputs:
            metrics = {"batch_loss": outputs["loss"].item() if hasattr(outputs["loss"], "item") else outputs["loss"]}
            self._queue_metrics(metrics, step=trainer.global_step)

    def on_validation_batch_end(self, trainer, pl_module, outputs, batch, batch_idx, dataloader_idx=0):
        """Called when the validation batch ends"""
        pass  # Implement if needed for validation metrics

    def on_train_epoch_end(self, trainer, pl_module):
        """Called when the train epoch ends"""
        metrics = trainer.callback_metrics
        epoch_metrics = {k: v.item() if hasattr(v, 'item') else v
                      for k, v in metrics.items() if isinstance(v, (int, float))}
        
        # Add health check and network connection status metric
        epoch_metrics["mlflow_healthy"] = 1.0
        
        self._queue_metrics(epoch_metrics, step=trainer.current_epoch)
        
        # Check for missing epoch records
        self._check_missing_epochs(trainer.current_epoch)

    def _check_missing_epochs(self, current_epoch):
        """Check for missing epoch records and attempt to recover"""
        if current_epoch <= 0:
            return
            
        # Check if all previous epochs have been recorded
        missing_epochs = [e for e in range(current_epoch) if e not in self.logged_epochs]
        if missing_epochs:
            print(f"Detected missing epoch logs: {missing_epochs}")
            # Record detected missing epochs metric
            self._queue_metrics({"missing_epochs_detected": len(missing_epochs)}, step=current_epoch)

    def on_fit_end(self, trainer, pl_module):
        """Called when fit ends"""
        # Ensure all pending logs are completed
        self._flush_logs()
        
        if self.ml_config.artifacts:
            self._queue_artifacts(self.ml_config.artifacts)
            self._flush_logs()
            
        self._ml_termination_()

    # Important: Add this method for PyTorch Lightning specifically
    def on_train_end(self, trainer, pl_module):
        """Called when training ends in PyTorch Lightning"""
        # Log final metrics if any
        metrics = trainer.callback_metrics
        if metrics:
            final_metrics = {k: v.item() if hasattr(v, 'item') else v
                          for k, v in metrics.items() if isinstance(v, (int, float))}
            # Add training completion marker metric
            final_metrics["training_completed"] = 1.0
            final_metrics["total_epochs_trained"] = trainer.current_epoch
            
            self._queue_metrics(final_metrics)
            self._flush_logs()

    # Transformers TrainerCallback methods - these use the Transformers interface
    def on_log(self, args, state, control, logs=None, **kwargs):
        """Callback method to log metrics during training (Transformers)"""
        if state.is_world_process_zero and logs is not None:
            metrics = {k: v for k, v in logs.items() if isinstance(v, (int, float))}
            if metrics:
                self._queue_metrics(metrics, step=state.global_step)

    def on_train_begin(self, args, state, control, **kwargs):
        """Called when training begins (Transformers)"""
        self.init_run()

    # This version is only for Transformers
    def on_train_end(self, args=None, state=None, control=None, **kwargs):
        """Called when training ends (Transformers)"""
        # Ensure all pending logs are completed
        self._flush_logs()
        
        if hasattr(self.ml_config, "artifacts"):
            self._queue_artifacts(self.ml_config.artifacts)
            self._flush_logs()
            
        # Record training completion metrics
        if state:
            self._queue_metrics({
                "training_completed": 1.0,
                "total_steps_trained": state.global_step
            })
            self._flush_logs()
            
        self._ml_termination_()

    # MLflow specific methods
    def init_run(self) -> None:
        """Initialize MLflow run with parameters, model info and artifacts"""
        if not self.mlflow.active_run():
            self.mlflow.start_run(description=self.experiment_description)

        if self.ml_config and hasattr(self.ml_config, "params"):
            self.log_params(self.ml_config.params)

        # Log model information if available
        if self.ml_config and hasattr(self.ml_config, "model"):
            model_info = getattr(self.ml_config, "model", None)
            if model_info and isinstance(model_info, dict):
                self.log_model(model_info)

        # Log initial artifacts if available
        if self.ml_config and hasattr(self.ml_config, "initial_artifacts"):
            initial_artifacts = getattr(self.ml_config, "initial_artifacts", None)
            if initial_artifacts:
                self.log_artifacts(initial_artifacts)

        # Log run start time
        self._queue_metrics({"run_started": 1.0, "run_start_timestamp": time.time()})

    def system_tracing(self, enabled: bool) -> None:
        """Enable or disable system metrics logging"""
        if not hasattr(self.ml_config, "system_tracing"):
            enabled = False
            
        if enabled and hasattr(self.mlflow, "enable_system_metrics_logging"):
            self.mlflow.enable_system_metrics_logging()

    def log_model(self, params: Dict[str, Any]) -> None:
        """Log model information to MLflow"""
        required_fields = ["model_uri", "name", "version"]
        missing = [field for field in required_fields if field not in params]
        if missing:
            raise ValueError(f"Missing required fields: {missing}")

        if not self.mlflow.active_run():
            self.mlflow.start_run(description=self.experiment_description)

        model_uri = params["model_uri"].format(
            run_id=self.mlflow.active_run().info.run_id)

        # Use retry mechanism to register model
        for attempt in range(self.max_retries):
            try:
                self.mlflow.register_model(
                    model_uri=model_uri,
                    name=params["name"],
                    tags={
                        "version": params["version"],
                        **(params.get("tag", {}) or {})
                    }
                )
                break
            except Exception as e:
                if attempt == self.max_retries - 1:
                    print(f"Failed to register model after {self.max_retries} attempts: {e}")
                else:
                    print(f"Attempt {attempt+1} to register model failed, retrying: {e}")
                    time.sleep(self.retry_delay)

    def log_params(self, params: Dict[str, Any]) -> None:
        """Log parameters to MLflow"""
        if params and self.mlflow.active_run():
            # Filter out parameters that have already been logged with different values
            try:
                run_id = self.mlflow.active_run().info.run_id
                client = self.mlflow.tracking.MlflowClient()
                # Get existing parameters - MLflow returns them as a dictionary
                existing_params = client.get_run(run_id).data.params
                
                safe_params = {}
                skipped_params = []
                for key, value in params.items():
                    str_value = str(value)
                    if key in existing_params:
                        if existing_params[key] != str_value:
                            skipped_params.append({
                                'key': key, 
                                'old_value': existing_params[key],
                                'new_value': str_value
                            })
                        # Skip if already exists with different value
                        continue
                    safe_params[key] = value
                    
                if skipped_params:
                    print(f"Warning: Skipped logging parameters with different values: {skipped_params}")
                    
                if safe_params:
                    self._queue_params(safe_params)
            except Exception as e:
                print(f"Warning: Error handling parameter logging: {e}")
                # Fallback to direct logging if there's an issue with the parameter checking
                self._queue_params(params)

    def log_metrics(self, metrics: Dict[str, float], step: int = 0) -> None:
        """Log metrics to MLflow with optional step number"""
        if metrics and self.mlflow.active_run():
            # Convert tensor values to Python scalars if needed
            cleaned_metrics = {}
            for k, v in metrics.items():
                if hasattr(v, 'item'):
                    cleaned_metrics[k] = v.item()
                else:
                    cleaned_metrics[k] = v
            
            self._queue_metrics(cleaned_metrics, step=step)

    def log_artifacts(self, artifacts: Dict[str, Any]) -> None:
        """Log artifacts to MLflow"""
        if artifacts and self.mlflow.active_run():
            self._queue_artifacts(artifacts)

    def _queue_metrics(self, metrics: Dict[str, float], step: int = None) -> None:
        """Add metrics to asynchronous processing queue"""
        if metrics and self.mlflow.active_run():
            self.pending_logs.put(("metrics", metrics, step))

    def _queue_params(self, params: Dict[str, Any]) -> None:
        """Add parameters to asynchronous processing queue"""
        if params and self.mlflow.active_run():
            self.pending_logs.put(("params", params, None))

    def _queue_artifacts(self, artifacts: Any) -> None:
        """Add artifacts to asynchronous processing queue"""
        if artifacts and self.mlflow.active_run():
            if isinstance(artifacts, list):
                artifacts = {"artifacts": artifacts}
            
            for artifact in artifacts.values():
                if artifact:
                    self.pending_logs.put(("artifacts", artifact, None))

    def _flush_logs(self) -> None:
        """Wait for all pending logs to complete"""
        timeout = 30  # Maximum wait of 30 seconds
        try:
            # Don't use q.join() to avoid permanent blocking
            start_time = time.time()
            while not self.pending_logs.empty() and time.time() - start_time < timeout:
                time.sleep(0.5)
                
            if not self.pending_logs.empty():
                remaining = self.pending_logs.qsize()
                print(f"Warning: Timed out waiting for {remaining} log entries to be processed")
        except Exception as e:
            print(f"Error while flushing logs: {e}")

    def set_log_artifacts(self, obj_str: str) -> None:
        """Log a single artifact to MLflow"""
        if obj_str and self.mlflow.active_run():
            self._queue_artifacts([obj_str])

    def set_log_params(self, key: str, val: str) -> None:
        """Log a single parameter to MLflow"""
        if key and val and self.mlflow.active_run():
            self._queue_params({key: val})

    def _ml_termination_(self) -> None:
        """End the current MLflow run"""
        # Stop log worker thread
        if self.log_worker_active:
            self.log_worker_active = False
            # Send termination signal
            self.pending_logs.put(None)
            if self.log_worker and self.log_worker.is_alive():
                self.log_worker.join(timeout=5)
        
        # Record final health status check
        if self.mlflow.active_run():
            try:
                self.mlflow.log_metrics({"mlflow_termination": 1.0})
            except Exception as e:
                print(f"Failed to log final metric: {e}")
            
            # End MLflow run
            self.mlflow.end_run()


def initialize(experiment_name: str, experiment_description: Any = None, config: Any=None, mlflow: Any=None) -> MLflowManager:
    """Initialize and return a new MLflowManager instance"""
    global client
    client = MLflowManager(experiment_name, experiment_description, config, mlflow)
    return client
