import re
from urllib.parse import urlparse

def inspect_url(url: str):
    suspicious_keywords = ["login", "verify", "bank", "secure", "update"]
    parsed = urlparse(url)

    flags = []

    if not parsed.scheme.startswith("http"):
        flags.append("invalid_scheme")

    if any(word in url.lower() for word in suspicious_keywords):
        flags.append("suspicious_keywords")

    if "@" in url:
        flags.append("obfuscated_url")

    if re.search(r"\d+\.\d+\.\d+\.\d+", parsed.netloc):
        flags.append("ip_address_domain")

    score = len(flags) * 0.25

    return {
        "malicious": score > 0.5,
        "confidence": score,
        "flags": flags,
        "model_version": "url-stub-v0.1"
    }
