##TEAMA_EHR_Gen_AI – AI Powered Enhanced EHR Imaging & Documentation System


## **Milestone 1 – Data Collection & Preprocessing**

### **Tasks Completed**
- Dataset collection (Kaggle, NIH, PhysioNet)  
- Cleaning: removing duplicates, renaming, resizing  
- Generating **mapping.csv**  
- Creating documentation on dataset sources and preprocessing  

---

## **Milestone 2 – Image Enhancement Using SRCNN**

### **Key Deliverables**
- Implemented **SRCNN**  
- Generated:
  - **Original vs Blurred vs Enhanced** images  
  - **PSNR / SSIM** metrics  
- Documented methodology, challenges, and comparisons  

---

## **Milestone 3 – Clinical Note Generation & ICD-10 Coding**

### **Core Implementations**
- Used **FLAN-T5** and **HF pipelines** to generate structured summaries  
- Hybrid ICD-10 mapping:
  - **Rule-based lookup**
  - **Keyword matching**
  - **AI fallback**  
- Exported:
  - **1000+ patient JSON outputs**
  - Evaluation metrics (BLEU, ROUGE, F1)
  - Batch result dashboards  

---

## **Milestone 4 – Integration & Deployment**

### **Backend – FastAPI**
- Endpoints:
  - `/generate_note`
  - `/assign_icd10`
  - `/enhance_image`
  - `/run_pipeline`
- Outputs structured JSON responses  
- Modular architecture for cloud deployment  

### **Frontend – Streamlit**
- Upload patient files & images  
- Real-time note generation  
- ICD-10 prediction  
- JSON output preview & download  

### **Deployment**
- **Dockerfile** for backend containerization  
- **Devcontainer** support  
- Ready for Azure, AWS, Render, Railway  

---

# **TECH STACK**

### **Languages & Frameworks**
- **Python**  
- **FastAPI**  
- **Streamlit**  
- **Docker**  
- **Jupyter Notebook**

### **AI & ML**
- **PyTorch / TensorFlow**  
- **Hugging Face Transformers**  
- **SRCNN**  
- **FLAN-T5 / T5 Models**

### **Libraries**
- **NumPy, Pandas**  
- **OpenCV**  
- **Matplotlib, Seaborn**

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
