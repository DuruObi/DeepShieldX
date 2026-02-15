import cv2
import numpy as np
import os
import uuid
import matplotlib.pyplot as plt


MAX_FRAMES = 60  # limit for MVP speed


def analyze_video(file_path: str):
    """
    Analyze video frames to detect potential deepfake inconsistencies.
    Generates a forensic heatmap graph for brightness + edge variance patterns.
    Returns structured forensic output ready for real-model integration.
    """

    if not os.path.exists(file_path):
        return {
            "score": 0.0,
            "verdict": "error",
            "details": "File does not exist"
        }

    cap = cv2.VideoCapture(file_path)

    if not cap.isOpened():
        return {
            "score": 0.0,
            "verdict": "error",
            "details": "Could not open video file"
        }

    frame_count = 0
    brightness_values = []
    edge_values = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Brightness metric
        brightness = np.mean(gray)
        brightness_values.append(brightness)

        # Edge detection metric
        edges = cv2.Canny(gray, 100, 200)
        edge_density = np.mean(edges)
        edge_values.append(edge_density)

        frame_count += 1

        if frame_count >= MAX_FRAMES:
            break

    cap.release()

    if frame_count == 0:
        return {
            "score": 0.0,
            "verdict": "invalid_video"
        }

    # Statistical anomaly calculations
    brightness_variance = np.var(brightness_values)
    edge_variance = np.var(edge_values)

    # Combined anomaly signal
    combined_signal = (brightness_variance + edge_variance) / 2

    # Stub scoring logic (replace with real ML later)
    score = float((combined_signal % 100) / 100)

    verdict = "likely_deepfake" if score > 0.55 else "clean"

    # Generate heatmap graph
    heatmap_path = generate_heatmap(
        brightness_values,
        edge_values
    )

    return {
        "score": score,
        "verdict": verdict,
        "frames_analyzed": frame_count,
        "forensic_signal": {
            "brightness_variance": float(brightness_variance),
            "edge_variance": float(edge_variance),
            "combined_signal": float(combined_signal)
        },
        "heatmap_path": heatmap_path,
        "model_version": "video-forensic-v0.2"
    }


def generate_heatmap(brightness_values, edge_values):
    """
    Generates and saves a forensic heatmap plot
    showing brightness and edge signal patterns.
    """

    heatmap_filename = f"heatmap_{uuid.uuid4()}.png"
    heatmap_path = os.path.join("/tmp", heatmap_filename)

    plt.figure(figsize=(10, 5))

    plt.plot(brightness_values, label="Brightness Pattern")
    plt.plot(edge_values, label="Edge Density Pattern")

    plt.title("DeepShieldX Video Forensic Heatmap")
    plt.xlabel("Frame Index")
    plt.ylabel("Signal Strength")
    plt.legend()

    plt.tight_layout()
    plt.savefig(heatmap_path)
    plt.close()

    return heatmap_path
