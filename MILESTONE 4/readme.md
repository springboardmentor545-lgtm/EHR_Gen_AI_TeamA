#  **Milestone 4 – AI-Powered EHR System (Frontend + Backend + Cloud Deployment)**

This repository contains the full implementation of **Milestone 4** for the *AI-Powered Enhanced EHR Imaging & Documentation System*.
The project integrates the **frontend interface**, **backend ML pipeline**, and **cloud deployment framework** into a unified working solution.


##  **Project Overview**

This milestone focuses on building a production-ready system that supports:

### **1. Streamlit Frontend**

A user-friendly interface for:

* Uploading clinical images or textual inputs
* Triggering model inference
* Displaying generated clinical notes
* Automatic ICD-10 code assignment
* Visualizing structured output and evaluation metrics

### **2. Backend ML Pipeline**

Modular backend pipeline that handles:

* Data preprocessing
* Hugging Face model inference
* Clinical note generation
* ICD-10 code mapping
* Output structuring for downstream systems
* Evaluation metrics for quality assessment

### **3. Cloud Deployment Setup**

Cloud-compatible architecture with:

* FastAPI/Flask based cloud backend
* Docker container for deployment
* Clean separation of local vs cloud requirements

---

##  **Repository Structure**

```
📦 milestone4-ai-ehr-system
│
├── .devcontainer/
│   └── devcontainer.json
│
├── .streamlit/
│   └── config.toml
│
├── Frontend/
│   ├── streamlit_app.py
│   └── requirements.txt
│
├── Src/
│   ├── data_preparation.py
│   ├── evaluation_metrics.py
│   ├── hf_model_connector.py
│   ├── icd10_code_assigner.py
│   ├── output_structurer.py
│   ├── workflow_pipeline.py
│   └── __pycache__/   (ignored during deployment)
│
├── Cloud/
│   ├── cloud_app.py
│   ├── app.py
│   ├── Dockerfile
│   ├── model.dockerignore
│   ├── requirements-cloud.txt
│   └── README.md   (cloud deployment steps)
│
├── .gitignore
└── README.md
```

---

## **System Workflow**

### **Input Stage**

Users upload clinical images or textual data via the Streamlit interface.

### ** Backend Processing**

The backend pipeline performs:

* Preprocessing
* Model inference using Transformers
* ICD-10 code assignment
* Output packaging
* Evaluation metric generation

### ** Output Stage**

Frontend displays:

* Generated clinical note
* ICD-10 codes
* Structured output JSON
* Model evaluation metrics

---

## **Technologies Used**

### **Frontend**

* Streamlit
* Python

### **Backend & ML**

* Hugging Face Transformers
* Custom ICD-10 mapping logic
* Python modular pipeline

### **Cloud Deployment**

* Docker
* FastAPI / Flask
* Cloud-ready directory and requirements

---

##  **Running the Application Locally**

### **1. Install Frontend Dependencies**

```
pip install -r Frontend/requirements.txt
```

### **2. Start the Streamlit Application**

```
streamlit run Frontend/streamlit_app.py
```

### **3. Run Cloud Backend (optional)**

```
cd Cloud
python cloud_app.py
```

---

##  **Docker Deployment**

### **Build Docker Image**

```
docker build -t ehr-ai-system .
```

### **Run Container**

```
docker run -p 8080:8080 ehr-ai-system
```

---

##  **Cloud Deployment**

The Cloud folder contains:

* Cloud-specific backend app
* Deployment instructions
* Optimized model ignore files
* Cloud dependency list

This allows deployment to services such as:

* Azure Web Apps
* AWS Elastic Beanstalk
* Google Cloud Run
* Render
* Railway

---
