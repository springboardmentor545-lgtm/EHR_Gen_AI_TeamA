# EHR_Gen_AI_TeamA
Milestone 1: Data Collection & Preprocessing
Objective:
The goal of this milestone is to collect, organize, and preprocess medical imaging and clinical (EHR) data in preparation for downstream AI/GenAI model training and applications.
Tasks Completed:
Data Collection
Medical Imaging Datasets:
Collected openly available datasets for imaging modalities: X-ray (COVID-19 Radiography Database).
Sources: Kaggle, PhysioNet, NIH, and other open repositories.
Collected imaging samples in formats such as .png, .jpg, .jpeg, and .dcm.
Electronic Health Records (EHR):
Gathered structured data: demographics, vitals, lab test results, and coded values (ICD, CPT).
Gathered unstructured data: patient notes, discharge summaries, and free-text reports.
Preprocessing
Cleaning:
Removed duplicates and noisy/unreadable samples from both medical imaging and EHR datasets.
Standardized missing values (e.g., ICD codes) and normalized units in the EHR data.
Labeling:
Created mappings between imaging samples and corresponding patient metadata (e.g., images to EHR records).
Annotated EHR notes with structured labels (e.g., diagnosis codes, conditions).
Standardization:
Converted images into a uniform format (.png, 256x256 resolution).
Tokenized and standardized text data for GenAI compatibility (UTF-8, lowercasing, de-identification).
Ensured compliance with privacy and de-identification protocols (HIPAA/GDPR safe).
📊 Output of Milestone 1
The following file structure has been created after completing the milestone:

Enhancing_EHRs_with_GenAI/
│
├── data/
│   ├── images/
│   │   ├── MRI_001.png
│   │   ├── MRI_002.png
│   │   └── CT_001.png
│   │
│   ├── ehr_notes/
│   │   ├── note_001.txt
│   │   ├── note_002.txt
│   │   └── note_003.txt
│   │
│   ├── mapping.csv
│
├── docs/
│   ├── dataset_sources.md
│   ├── cleaning_steps.md
│   └── challenges.md
│
└── README.md

Challenges & Learnings:
Data Imbalance: Some imaging categories (e.g., COVID-19 X-rays) had more samples than others (e.g., MRI, CT scans), leading to an imbalance in dataset sizes.
Missing Data: Several EHR notes had missing or incomplete ICD codes. We implemented an auto-fill feature using NLP techniques to suggest ICD codes from the notes.
Data Privacy & Compliance: Ensured de-identification and HIPAA/GDPR compliance, including masking personal information in EHR notes.
