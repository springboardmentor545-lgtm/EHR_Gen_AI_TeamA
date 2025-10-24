# Data Cleaning & Preprocessing Steps

## 1. Images
- Converted DICOM and JPG/PNG images to 256x256 grayscale PNGs.
- Skipped corrupted files.
- Saved processed images to `data/images_processed/`.

## 2. EHR Notes
- Extracted text from PDFs using pdfplumber.
- Cleaned and saved TXT files to `data/ehr_notes_processed/`.

## 3. Mapping CSV
- Created `data/mapping.csv` linking images and notes.
- Filled ICD-10 codes using keyword lookup table.

## 4. ICD-10 Lookup Table
- Keywords: pneumonia, hypertension, diabetes
- Generated `data/icd_lookup.csv`
- Used `suggest_icd()` function to auto-fill codes.

## 5. Sanity Checks
- Verified all image/note paths exist.
- Checked ICD-10 codes for correct format.
- Auto-filled missing/unknown ICD codes.

## 6. Notes
- No PHI included; all data is de-identified.
- At least 20 processed images and 5 notes present for testing.
