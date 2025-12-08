import cv2
import numpy as np

def enhance_baseline(img_gray):
    """
    Baseline medical image enhancement:
    1. Noise reduction (Non-Local Means)
    2. Sharpening (Unsharp Mask)
    3. Contrast enhancement
    """

    # 1. Denoising
    denoised = cv2.fastNlMeansDenoising(
        img_gray, None, h=10, templateWindowSize=7, searchWindowSize=21
    )

    # 2. Sharpening using Unsharp Mask
    blurred = cv2.GaussianBlur(denoised, (0, 0), sigmaX=3)
    sharpened = cv2.addWeighted(denoised, 1.5, blurred, -0.5, 0)

    # 3. Brightness and contrast tuning
    enhanced = cv2.convertScaleAbs(sharpened, alpha=1.25, beta=8)

    return enhanced
