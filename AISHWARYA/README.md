**My Individual Contribution — Milestone 1**

**In Milestone 1, I completed the full Data Collection & Preprocessing pipeline:**

-Set up Kaggle API and configured kaggle.json for secure dataset downloads.

-Created the complete project folder structure for raw and processed data.

-Downloaded two major datasets:

-COVID-19 Radiography (X-ray images)

-Medical Transcriptions (EHR notes)

-Built the image preprocessing pipeline:

-Handled PNG/JPG/JPEG/DICOM images

-Converted to grayscale, normalized, resized to 256×256

-Saved all outputs in a unified processed dataset

-Verified dataset integrity and ensured all processed files were correctly stored for team use.

✔ Total images processed: 21,165
✔ Provided clean, standardized data for the next milestones.


**My Individual Contribution — Milestone 2**

**In Milestone 2, I developed the complete Medical Image Enhancement Prototype using classical image processing and a GenAI-based SRCNN model. I also created the full GitHub project structure and documentation for this milestone.**

**My Contributions**

*Installed and configured all required libraries (TensorFlow, OpenCV, scikit-image, tqdm, PIL).

*Prepared the demo dataset by checking Milestone 1 outputs or generating synthetic X-ray-like images.

*Implemented the baseline enhancement pipeline:

*Denoising (Non-Local Means)

*Sharpening (Unsharp Mask)

*Contrast adjustment

*Built and trained the SRCNN GenAI model for medical image super-resolution.

*Generated visual comparisons:
**Original → Low-Res → Baseline Enhanced → SRCNN Enhanced**

*Calculated key quality metrics (PSNR, SSIM) for sample and batch images.

*Saved all enhanced images, comparison figures, and metric CSVs.

*Created the complete **GitHub folder structure** for this milestone, including:

-demo_data/original/

-demo_data/enhanced/

-data/metrics/

*Organized code, outputs, and evaluation files

*Prepared and wrote the **full documentation for Milestone 2**, explaining the workflow, methods, results, and outputs.
