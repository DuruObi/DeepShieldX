import cv2
import numpy as np

def analyze_image(file_path: str):
    image = cv2.imread(file_path)

    if image is None:
        return {"score": 0.0, "verdict": "invalid_image"}

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    variance = np.var(gray)

    score = (variance % 100) / 100
    verdict = "likely_deepfake" if score > 0.5 else "clean"

    return {
        "score": float(score),
        "verdict": verdict,
        "forensic_signal": {"pixel_variance": float(variance)},
        "model_version": "image-stub-v0.1"
    }
