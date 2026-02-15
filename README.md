# DeepShieldX

**Real-Time Deepfake & Scam Detection Shield**  

DeepShieldX is an MVP that provides a personal shield for users and an enterprise API for detecting:

- AI-generated voices
- Deepfake videos
- Fraudulent images
- Scam messages
- Suspicious URLs

It alerts users **before they get fooled**, logs scans, and is fully modular for future AI integration.

---

## Features (MVP)

- Voice deepfake detection (stub)
- Video deepfake detection (stub)
- Image deepfake detection (stub)
- Message scam detection
- URL phishing detection
- Heatmap / forensic artifacts
- Postgres scan logging
- API key authentication
- Dockerized microservices
- Ready for web/mobile integration

---

## Architecture


- **API Gateway**: Routes requests to AI Engine, authenticates with API keys.
- **AI Engine**: Processes uploaded audio/video/images/text/URLs. Returns deepfake/scam probabilities.
- **Postgres**: Logs every scan for analytics.
- **Docker**: Runs AI Engine, API Gateway, and Postgres together.

---

## Local Setup (MVP)

1. Clone the repo:

```bash
git clone https://github.com/DuruObi/DeepShieldX.git
cd DeepShieldX
