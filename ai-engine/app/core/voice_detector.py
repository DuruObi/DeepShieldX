import numpy as np

def analyze_voice(file_bytes):
    size = len(file_bytes)
    score = (size % 100) / 100

    return {
        "score": score,
        "verdict": "likely_deepfake" if score > 0.5 else "clean",
        "model_version": "stub-v0.1"
    }
