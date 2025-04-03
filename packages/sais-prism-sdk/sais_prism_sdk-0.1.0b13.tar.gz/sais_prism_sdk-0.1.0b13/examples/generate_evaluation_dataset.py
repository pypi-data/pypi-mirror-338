#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Generate evaluation dataset for pharmaceutical domain models.
Creates a JSONL file with test questions for evaluation.
"""

import json
import os
import argparse


def create_evaluation_dataset(output_path, num_questions=None):
    """
    Create an evaluation dataset and save it as JSONL.
    
    Args:
        output_path: Path to save the evaluation file
        num_questions: Number of questions to include (None for all)
    """
    # Define evaluation questions
    evaluation_questions = [
        {
            "instruction": "What are the different classifications of the drug Imatinib?",
            "input": "",
            "output": "Imatinib (Gleevec/Glivec) can be classified as: 1) a tyrosine kinase inhibitor (TKI), 2) a targeted therapy, 3) an antineoplastic agent, 4) a BCR-ABL inhibitor, 5) a c-KIT inhibitor, and 6) a PDGFR inhibitor. It's also categorized by its therapeutic use for chronic myeloid leukemia (CML), gastrointestinal stromal tumors (GIST), and other rare cancers."
        },
        {
            "instruction": "Describe the mechanism of action for metformin.",
            "input": "",
            "output": "Metformin decreases hepatic glucose production through inhibition of the mitochondrial respiratory chain (complex I) and activation of AMPK (AMP-activated protein kinase). This leads to reduced gluconeogenesis and glycogenolysis. It also increases peripheral glucose uptake in skeletal muscle, reduces intestinal glucose absorption, and improves insulin sensitivity by increasing insulin receptor tyrosine kinase activity and insulin receptor expression."
        },
        {
            "instruction": "What are the pharmacokinetic properties of atorvastatin?",
            "input": "",
            "output": "Atorvastatin has oral bioavailability of approximately 14%, high protein binding (>98%), extensive first-pass metabolism in the liver via CYP3A4, and is primarily eliminated through biliary excretion. Its mean plasma elimination half-life is approximately 14 hours, but the inhibitory effect on HMG-CoA reductase lasts 20-30 hours due to active metabolites. It is best absorbed under fasting conditions and has dose-proportional pharmacokinetics."
        },
        {
            "instruction": "Describe the chemical structure of sildenafil.",
            "input": "",
            "output": "Sildenafil (C22H30N6O4S) is a pyrazolopyrimidinone derivative. Its chemical structure consists of a pyrazolopyrimidinone core with a methylpiperazine ring, a sulfonamide group, and an ethoxy group. The IUPAC name is 5-{2-ethoxy-5-[(4-methylpiperazin-1-yl)sulfonyl]phenyl}-1-methyl-3-propyl-1,6-dihydro-7H-pyrazolo[4,3-d]pyrimidin-7-one."
        },
        {
            "instruction": "What clinical trials have been conducted for the drug pembrolizumab?",
            "input": "",
            "output": "Key clinical trials for pembrolizumab include KEYNOTE-001 (first-in-human study), KEYNOTE-006 (melanoma), KEYNOTE-024 and KEYNOTE-042 (first-line NSCLC), KEYNOTE-189 (non-squamous NSCLC), KEYNOTE-407 (squamous NSCLC), KEYNOTE-048 (head and neck cancer), KEYNOTE-057 (bladder cancer), KEYNOTE-181 (esophageal cancer), KEYNOTE-426 (renal cell carcinoma), and KEYNOTE-522 (triple-negative breast cancer). These trials established its efficacy across multiple cancer types, leading to numerous FDA approvals."
        },
        {
            "instruction": "What are the adverse effects of isotretinoin?",
            "input": "",
            "output": "Common adverse effects of isotretinoin include mucocutaneous effects (dry lips, dry skin, rash), hypertriglyceridemia, elevated liver enzymes, musculoskeletal pain, headache, and dry eyes. Serious adverse effects include teratogenicity (pregnancy category X), psychiatric effects (depression, suicidal ideation), pseudotumor cerebri, inflammatory bowel disease, and severe skin reactions. Laboratory monitoring is required for liver function, lipid levels, and pregnancy testing."
        },
        {
            "instruction": "How does the drug rivaroxaban work?",
            "input": "",
            "output": "Rivaroxaban is a direct factor Xa inhibitor that selectively and reversibly blocks the active site of factor Xa, preventing the conversion of prothrombin to thrombin in the coagulation cascade. By inhibiting factor Xa, rivaroxaban prevents both thrombin formation and subsequent thrombus development. Unlike warfarin, rivaroxaban does not require vitamin K as a cofactor and directly inhibits factor Xa without requiring antithrombin as a mediator."
        },
        {
            "instruction": "What are the different formulations of insulin available for diabetic patients?",
            "input": "",
            "output": "Insulin formulations include: 1) Rapid-acting (insulin aspart, lispro, glulisine) with onset 15-30 minutes, peak 1-2 hours, duration 3-5 hours; 2) Short-acting (regular insulin) with onset 30-60 minutes, peak 2-4 hours, duration 5-8 hours; 3) Intermediate-acting (NPH) with onset 1-2 hours, peak 4-6 hours, duration 10-16 hours; 4) Long-acting (insulin glargine, detemir, degludec) with onset 1-2 hours, no pronounced peak, duration 20-36 hours; 5) Ultra-long-acting with duration of 42+ hours; 6) Premixed combinations of rapid/short-acting with intermediate-acting insulin."
        },
        {
            "instruction": "Explain the classification of beta-lactam antibiotics.",
            "input": "",
            "output": "Beta-lactam antibiotics are classified into several groups: 1) Penicillins (natural penicillins, aminopenicillins, antipseudomonal penicillins, penicillinase-resistant penicillins); 2) Cephalosporins (first through fifth generations); 3) Carbapenems (imipenem, meropenem, ertapenem, doripenem); 4) Monobactams (aztreonam); and 5) Beta-lactamase inhibitors (clavulanic acid, sulbactam, tazobactam, avibactam). All contain the beta-lactam ring structure, which inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs)."
        },
        {
            "instruction": "What is the regulatory approval history of PARP inhibitors for cancer treatment?",
            "input": "",
            "output": "PARP inhibitors received FDA approvals chronologically: Olaparib (2014, first approval for germline BRCA-mutated ovarian cancer; later expanded to breast, pancreatic, and prostate cancers); Rucaparib (2016, ovarian cancer; 2020, prostate cancer); Niraparib (2017, ovarian cancer maintenance; 2020, first-line maintenance regardless of BRCA status); Talazoparib (2018, germline BRCA-mutated HER2-negative breast cancer). EMA approvals followed similar patterns. Approvals initially required BRCA mutations but expanded to homologous recombination deficiency (HRD) and broader maintenance settings."
        }
    ]

    # Limit the number of questions if specified
    if num_questions is not None:
        evaluation_questions = evaluation_questions[:num_questions]

    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write to JSONL file
    with open(output_path, 'w') as f:
        for question in evaluation_questions:
            f.write(json.dumps(question, ensure_ascii=False) + '\n')

    print(
        f"Created evaluation dataset with {len(evaluation_questions)} questions at {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate evaluation dataset for pharmaceutical models")
    parser.add_argument("--output", type=str, default="examples/evaluation_dataset.jsonl",
                        help="Path to save the evaluation JSONL file")
    parser.add_argument("--num_questions", type=int, default=None,
                        help="Number of questions to include (default: all)")

    args = parser.parse_args()
    create_evaluation_dataset(args.output, args.num_questions)
