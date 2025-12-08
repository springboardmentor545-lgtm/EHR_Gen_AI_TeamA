from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from io import BytesIO
from PIL import Image
import numpy as np

from enhancement import enhance_baseline
from notes_icd import (
    DataPreparationPipeline,
    HuggingFaceModelConnector,
    ICD10CodeAssigner,
    OutputStructurer
)

app = FastAPI(
    title="AI-Powered Enhanced EHR Imaging & Documentation System",
    description="Backend API for image enhancement, clinical note generation & ICD-10 coding",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PatientInput(BaseModel):
    name: str = "Patient_1"
    age: int = 45
    gender: str = "Female"
    symptoms: str = "cough, fever, chest pain"
    scan_result: str = "Chest X-ray shows infiltrates"
    medical_history: Optional[str] = None

class EHRProcessResponse(BaseModel):
    patient_name: str
    age: int
    gender: str
    symptoms: str
    scan_result: str
    clinical_note: str
    icd10_code: str
    code_accuracy: float
    matched_keywords: List[str]

data_prep = DataPreparationPipeline()
hf_model = HuggingFaceModelConnector()
icd_assigner = ICD10CodeAssigner()
output_structurer = OutputStructurer()

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Backend running"}

@app.post("/enhance-image-baseline")
async def enhance_image_baseline(file: UploadFile = File(...)):
    contents = await file.read()
    img = Image.open(BytesIO(contents)).convert("L")
    arr = np.array(img)
    enhanced = enhance_baseline(arr)
    enhanced_img = Image.fromarray(enhanced)
    buffer = BytesIO()
    enhanced_img.save(buffer, format="PNG")
    buffer.seek(0)
    return {"message": "Image enhanced successfully"}

@app.post("/generate-note")
def generate_note(patient: PatientInput):
    patient_json = data_prep.prepare_patient_json(patient.dict())
    prompt = data_prep.format_for_model(patient_json)
    generated_note = hf_model.generate_clinical_output(prompt)
    return {"clinical_note": generated_note}

class ICDInput(BaseModel):
    symptoms: str
    clinical_note: str

@app.post("/assign-icd")
def assign_icd(data: ICDInput):
    parsed = output_structurer.parse_model_response(
        data.clinical_note,
        data.symptoms,
        icd_assigner
    )
    return parsed

@app.post("/process-ehr", response_model=EHRProcessResponse)
def process_ehr(patient: PatientInput):
    patient_json = data_prep.prepare_patient_json(patient.dict())
    prompt = data_prep.format_for_model(patient_json)

    note_text = hf_model.generate_clinical_output(prompt)
    
    parsed = output_structurer.parse_model_response(
        note_text,
        patient.symptoms,
        icd_assigner
    )

    final = output_structurer.create_final_output(patient_json, parsed)

    return EHRProcessResponse(
        patient_name=final["PatientName"],
        age=final["Age"],
        gender=final["Gender"],
        symptoms=final["Symptoms"],
        scan_result=final["ScanResult"],
        clinical_note=final["ClinicalNote"],
        icd10_code=final["ICD10Code"],
        code_accuracy=final["CodeAccuracy%"],
        matched_keywords=final["MatchedKeywords"],
    )
