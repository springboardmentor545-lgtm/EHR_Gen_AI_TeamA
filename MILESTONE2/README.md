# 🧠 Milestone 2 — Medical Image Enhancement (GenAI)

## 📋 Project Overview
This milestone focuses on **enhancing medical images using Generative AI** techniques to improve clarity, diagnostic visibility, and Electronic Health Record (EHR) documentation quality.  
The enhancement process employs **SRCNN (Super-Resolution Convolutional Neural Network)** and traditional OpenCV methods to compare classical and AI-based approaches.

---

## 🎯 Objective
- To apply **GenAI** for improving image resolution and reducing noise in X-ray/MRI/CT images.  
- To support doctors by generating **clearer, high-quality medical visuals** for accurate diagnosis.  
- To evaluate image quality using quantitative metrics (**PSNR**, **SSIM**) and visual comparisons.

---

## 🧩 Folder Structure
milestone_2/
│
├── data/
│ ├── images_processed/ # Input dataset (from Milestone 1)
│ └── metrics/ # Quantitative results & comparison images
│
├── demo_data/
│ ├── original/ # 20 demo input medical images
│ └── enhanced/ # AI-enhanced outputs (Baseline + SRCNN)
│
├── models/ # Trained SRCNN model weights
│ └── srcnn.h5
│
├── notebooks/
│ └── milestone2_enhancement.ipynb
│
├── results/
│ ├── enhancement_demo_comparison.png
│ └── enhancement_metrics_batch.csv
│
└──  README.md # Project documentation (this file)
