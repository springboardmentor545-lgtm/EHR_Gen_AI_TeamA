import requests
import json
import time
import sys

def test_api():
    base_url = "http://127.0.0.1:8000"
    
    # Wait for API to be ready
    print("Waiting for API to be ready...")
    # Wait for API to be ready (up to 5 minutes for model download)
    print("Waiting for API to be ready...")
    for i in range(150):
        try:
            response = requests.get(f"{base_url}/health")
            if response.status_code == 200:
                print("API is ready!")
                break
        except requests.exceptions.ConnectionError:
            if i % 10 == 0:
                print(f"Waiting... ({i*2}s)")
            time.sleep(2)
    else:
        print("API failed to start.")
        sys.exit(1)

    # Test data
    patient_data = {
        "name": "John Doe",
        "age": 45,
        "gender": "Male",
        "symptoms": "Persistent cough and fever",
        "scan_result": "Chest X-ray shows mild opacity",
        "medical_history": "None",
        "vital_signs": {"temp": 38.5, "bp": "120/80"}
    }

    print("\nTesting /process_patient endpoint...")
    try:
        response = requests.post(f"{base_url}/process_patient", json=patient_data)
        if response.status_code == 200:
            print("✅ Success!")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"❌ Failed with status {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_api()
