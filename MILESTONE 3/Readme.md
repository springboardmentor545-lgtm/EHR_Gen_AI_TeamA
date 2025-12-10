# Milestone 3: Clinical Note Generation & ICD-10 Coding

## 🚀 Overview

This project generates **clinical notes** using a Hugging Face FLAN-T5 model and assigns **ICD-10 codes** with confidence scoring. It processes patient symptoms, imaging details, and demographics, then outputs structured JSON/CSV files.


## 📂 Project Structure
```

project-root/
├── data/                 # Input files (mapping.csv)
├── outputs/              # Generated results
│   ├── patients/         # Individual patient JSONs
├── src/                  # Core modules
│   ├── data_preparation.py
│   ├── hf_model_connector.py
│   ├── icd10_code_assigner.py
│   ├── workflow_pipeline.py
│   ├── evaluation_metrics.py
├── notebooks/            # Development notebooks
├── documents
│   ├── Presentation
│   ├── Documenatation
├── requirements.txt
└── README.md
```
## ▶️ Run in Google Colab

1. Upload your datasets to Google Drive
2. Open the notebook in `/notebooks/`
3. Run all cells to:

   * Generate clinical notes
   * Assign ICD-10 codes
   * Save analytics + reports

No additional scripts are required.


## 📊 Generated Outputs

After running the notebook, the following are automatically created:

| Output                                 | Description                            |
| -------------------------------------- | -------------------------------------- |
| **batch_results.csv**                  | All processed patients in a single CSV |
| **batch_results.json**                 | Structured JSON version                |
| **patients/*.json**                    | Individual patient records             |
| **evaluation_metrics.json**            | Accuracy + quality scores              |
| **analysis_report.png**                | Visual charts                          |
| **Milestone3_Complete_Submission.zip** | Complete packaged deliverable          |


## 🧠 Model Used

* **google/flan-t5-large** (fallback: flan-t5-base)
* Hugging Face Transformers pipeline
* Repetition filtering + accuracy scoring

## ✔️ Requirements


transformers
torch
pandas
numpy
scikit-learn
rouge-score
matplotlib
seaborn
tqdm
sentencepiece
nltk
