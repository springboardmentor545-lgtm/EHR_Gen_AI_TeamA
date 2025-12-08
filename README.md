# EHR_Gen_AI_TeamA
🏥 AI-Powered Enhanced EHR Imaging & Documentation System

This project is an end-to-end AI platform designed to enhance medical imaging, generate clinical notes, and automate ICD-10 coding. It integrates:

🩻 Medical Image Enhancement (SRCNN-based)

📝 Clinical Note Generation using NLP

🧾 Automated ICD-10 Code Prediction

⚙️ FastAPI Backend

🎨 Streamlit Frontend

🐳 Dockerized Deployment Architecture

📌 Project Architecture Overview
             ┌────────────────────┐
             │   Streamlit UI     │
             │  (Frontend Layer)   │
             └─────────┬──────────┘
                       │
                       ▼
          ┌──────────────────────────┐
          │       FastAPI Backend    │
          │  • Image Enhancement     │
          │  • Note Generation       │
          │  • ICD-10 Coding API     │
          └──────────┬──────────────┘
                     │
                     ▼
          ┌──────────────────────────┐
          │   ML Models (SRCNN,NLP) │
          └──────────────────────────┘

📁 Repository Structure
EHR_Gen_AI_TeamA/
│
├── backend/
│   ├── main.py
│   ├── enhancement.py
│   ├── notes_icd.py
│   ├── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│
├── Dockerfile
├── Procfile
├── requirements.txt
│
├── MILESTONE 3/
├── MILESTONE2/
├── MILESTONE1/   (if applicable)
│
├── docs/
├── notebooks/
└── README.md

🧠 Key Features
🩻 1. Image Enhancement

SRCNN-inspired deep learning model

Improves medical image clarity

Helpful for clinical interpretation

📝 2. Clinical Note Generation

Transformer-based NLP

Generates structured clinical notes

Summarizes important details automatically

🧾 3. ICD-10 Code Prediction

Automatic ICD-10 classification

Multi-label prediction

Reduces clinician documentation time

🚀 Backend (FastAPI)
▶ Run backend locally:
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

▶ API Documentation:

Open in browser:

http://127.0.0.1:8000/docs

🎨 Frontend (Streamlit)
▶ Run frontend locally:
cd frontend
pip install -r requirements.txt
streamlit run app.py

🐳 Docker Instructions
▶ Build Docker image:
docker build -t ehr_app .

▶ Run container:
docker run -p 8000:8000 ehr_app

☁️ Deployment (Pending)

Deployment Target: Railway / Render / Azure / GCP

🚀 Deployment Link: To be added after cloud deployment

🧪 Testing Summary

Includes:

Image enhancement validation

NLP output consistency checks

ICD-10 code accuracy testing

End-to-end pipeline verification

🎯 Milestone Completion Status
Milestone	Description	Status
1	Data Collection & Preprocessing	✔ Completed
2	Image Enhancement	✔ Completed
3	NLP + ICD-10 Coding	✔ Completed
4	Cloud Deployment	⏳ Pending (awaiting repository access)
5	Integration Testing	✔ Completed
6	GitHub Repository Setup	✔ Completed
📜 License

This project is developed for academic and research purposes as part of the Springboard Mentor Program.

