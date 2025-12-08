import streamlit as st
import requests

st.title("AI-Powered Enhanced EHR Imaging & Documentation System")

BACKEND_URL = "https://your-backend-url"   # <-- we will update after deployment


# -------------------------
# Image Enhancement Section
# -------------------------
st.header("1. Upload X-ray Image for Enhancement")

uploaded_image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", width=300)

    if st.button("Enhance Image"):
        files = {"file": uploaded_image.getvalue()}
        res = requests.post(f"{BACKEND_URL}/enhance-image-baseline", files=files)

        if res.status_code == 200:
            st.success("Image enhanced successfully!")
        else:
            st.error("Enhancement failed.")


# -------------------------
# Clinical Note + ICD-10
# -------------------------
st.header("2. Clinical Note Generation & ICD-10 Coding")

name = st.text_input("Patient Name", "Patient 1")
age = st.number_input("Age", 30)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
symptoms = st.text_area("Symptoms", "cough, fever")
scan_result = st.text_area("Scan Result", "Chest X-ray shows infiltrates")

if st.button("Generate Note + ICD-10 Code"):
    payload = {
        "name": name,
        "age": age,
        "gender": gender,
        "symptoms": symptoms,
        "scan_result": scan_result
    }

    res = requests.post(f"{BACKEND_URL}/process-ehr", json=payload)

    if res.status_code == 200:
        output = res.json()
        st.subheader("Generated Clinical Note")
        st.write(output["clinical_note"])

        st.subheader("ICD-10 Code")
        st.write(output["icd10_code"])

        st.subheader("Accuracy %")
        st.write(output["code_accuracy"])

        st.subheader("Matched Keywords")
        st.write(output["matched_keywords"])
    else:
        st.error("Error generating output.")
