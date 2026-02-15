def scan_message(text: str):
    suspicious_keywords = ["urgent", "transfer", "bank", "verify", "password"]
    flags = [word for word in suspicious_keywords if word in text.lower()]
    score = len(flags) * 0.2

    return {
        "scam": score > 0.3,
        "score": score,
        "flags": flags
    }
