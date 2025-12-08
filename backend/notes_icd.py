import re

# ---------------------------
# 1. Data Preparation
# ---------------------------

class DataPreparationPipeline:
    def prepare_patient_json(self, patient_dict):
        """
        Cleans and standardizes patient data for model input.
        """
        return {
            "PatientName": patient_dict.get("name"),
            "Age": patient_dict.get("age"),
            "Gender": patient_dict.get("gender"),
            "Symptoms": patient_dict.get("symptoms"),
            "ScanResult": patient_dict.get("scan_result"),
            "MedicalHistory": patient_dict.get("medical_history", "None")
        }

    def format_for_model(self, patient_json):
        """
        Converts patient data into a structured prompt for text-generation model.
        """
        prompt = (
            f"Generate a professional clinical note.\n\n"
            f"Patient Name: {patient_json['PatientName']}\n"
            f"Age: {patient_json['Age']}\n"
            f"Gender: {patient_json['Gender']}\n"
            f"Symptoms: {patient_json['Symptoms']}\n"
            f"Scan Result: {patient_json['ScanResult']}\n"
            f"Medical History: {patient_json['MedicalHistory']}\n\n"
            f"Clinical Note:"
        )
        return prompt


# ---------------------------
# 2. Clinical Note Generation
# ---------------------------

class HuggingFaceModelConnector:
    """
    Simulates a text-generation model (no online HF calls required for deployment).
    Replace with a real API if needed.
    """

    def generate_clinical_output(self, prompt):
        # Simple simulated output (safe for offline backend)
        return (
            "The patient presents with symptoms consistent with respiratory infection. "
            "Recommend clinical correlation and follow-up imaging. "
            "Possible diagnosis includes pneumonia or viral infection."
        )


# ---------------------------
# 3. ICD-10 Code Assignment
# ---------------------------

class ICD10CodeAssigner:

    ICD_LOOKUP = {
        "pneumonia": "J18.9",
        "respiratory infection": "J22",
        "viral infection": "B34.9",
        "fever": "R50.9",
        "cough": "R05.1",
        "chest pain": "R07.9"
    }

    def match_icd10_codes(self, text):
        """
        Finds which ICD codes apply based on keyword matching.
        """
        text = text.lower()
        matched = []

        for keyword, code in self.ICD_LOOKUP.items():
            if keyword in text:
                matched.append(code)

        return matched if matched else ["UNKNOWN"]


# ---------------------------
# 4. Final Output Structuring
# ---------------------------

class OutputStructurer:
    def parse_model_response(self, clinical_text, symptoms, icd_assigner):
        """
        Extract structured fields from generated clinical note.
        """
        icd_codes = icd_assigner.match_icd10_codes(clinical_text + " " + symptoms)

        matched_keywords = []
        for word in icd_assigner.ICD_LOOKUP.keys():
            if word in clinical_text.lower() or word in symptoms.lower():
                matched_keywords.append(word)

        accuracy = round((len(matched_keywords) / max(len(symptoms.split()), 1)) * 100, 2)

        return {
            "clinical_note": clinical_text,
            "icd_codes": ", ".join(icd_codes),
            "matched_keywords": matched_keywords,
            "accuracy": accuracy
        }

    def create_final_output(self, patient_json, parsed):
        return {
            "PatientName": patient_json["PatientName"],
            "Age": patient_json["Age"],
            "Gender": patient_json["Gender"],
            "Symptoms": patient_json["Symptoms"],
            "ScanResult": patient_json["ScanResult"],
            "ClinicalNote": parsed["clinical_note"],
            "ICD10Code": parsed["icd_codes"],
            "CodeAccuracy%": parsed["accuracy"],
            "MatchedKeywords": parsed["matched_keywords"]
        }
