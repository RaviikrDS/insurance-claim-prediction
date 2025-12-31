# 🏦 Insurance Claim Amount Prediction (End-to-End ML System)

An **end-to-end, production-ready Machine Learning system** for predicting insurance claim amounts using **Python, FastAPI, Streamlit, Docker, and CI/CD**.

This project demonstrates **industry-level ML engineering practices**, including clean architecture, model versioning, API-based inference, containerization, and automated CI pipelines.

---

## 📌 Business Problem

Insurance companies must estimate the **expected cost of a claim** before it is fully processed.
Accurate predictions help with:

* Premium pricing
* Risk management
* Reserve allocation
* Profitability analysis

### 🎯 Objective

> Predict the **expected insurance claim amount** given customer, policy, and accident details.

---

## 📊 Model Inputs & Output

### 🔹 Input Features

* Age
* Annual income
* Vehicle age
* Past claims count
* Accident severity (1–5)
* Policy tenure (years)

### 🔹 Output

* **Estimated claim amount** (continuous value)

---

## 🧠 Machine Learning Approach

* **Model Type**: Regression (GLM-style / Linear Regression baseline)
* **Feature Scaling**: StandardScaler
* **Artifacts**:

  * Trained model (`model.pkl`)
  * Scaler (`scaler.pkl`)
  * Metadata (`metadata.json`)

Model artifacts are versioned and loaded dynamically at application startup.

---

## 🏗️ System Architecture

```
User (Browser)
   ↓
Streamlit Frontend (UI)
   ↓
FastAPI Backend (Inference API)
   ↓
ML Model (Artifacts)
```

---

## 📂 Project Structure

```
insurance-claim-prediction/
│
├── backend/
│   ├── app/
│   │   ├── api/            # API routes
│   │   ├── services/       # Prediction & model loading logic
│   │   ├── schemas/        # Pydantic request/response schemas
│   │   ├── core/           # Config & logging
│   │   └── main.py         # FastAPI app entrypoint
│   │
│   ├── artifacts/          # Model, scaler, metadata
│   ├── tests/              # Pytest test suite
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── streamlit_app.py    # Streamlit UI
│   ├── Dockerfile
│   └── requirements.txt
│
├── docker-compose.yml      # Multi-service orchestration
├── .github/workflows/
│   └── ci.yml              # CI pipeline (pytest + docker compose)
│
└── README.md
```

---

## 🚀 How to Run Locally (Docker Recommended)

### 1️⃣ Prerequisites

* Docker Desktop
* Docker Compose (v2+)

Verify:

```bash
docker --version
docker compose version
```

---

### 2️⃣ Start the System

From project root:

```bash
docker compose up --build
```

---

### 3️⃣ Access Applications

* **FastAPI Swagger UI**
  👉 [http://localhost:8000/docs](http://localhost:8000/docs)

* **Health Check**
  👉 [http://localhost:8000/health](http://localhost:8000/health)

* **Streamlit Frontend**
  👉 [http://localhost:8501](http://localhost:8501)

---

## 🔍 API Example

### POST `/predict`

**Request**

```json
{
  "age": 40,
  "annual_income": 80000,
  "vehicle_age": 6,
  "past_claims": 1,
  "accident_severity": 4,
  "policy_tenure": 5
}
```

**Response**

```json
{
  "estimated_claim_amount": 12345.67
}
```

---

## 🧪 Testing Strategy

### ✔ Unit & Integration Tests

* Schema validation
* Predictor service tests
* API endpoint tests

Run locally:

```bash
cd backend
pytest -v
```

---

## 🔁 CI/CD Pipeline

This project includes a **production-grade CI pipeline** using **GitHub Actions**.

### CI Steps:

1. Run backend tests (`pytest`)
2. Build Docker images
3. Start full system using Docker Compose
4. Wait for backend health
5. Run inference smoke test
6. Tear down containers

### CI guarantees:

* Code quality
* Model compatibility
* Container correctness
* End-to-end system stability

---

## 🐳 Containerization

* Backend and frontend are **separate Docker images**
* Services communicate via **Docker internal networking**
* Health-based startup ordering
* Lightweight `python:3.12-slim` images

---

## 🔐 Engineering Best Practices Used

* Clean architecture & separation of concerns
* No model loading at import time
* Centralized configuration
* Structured logging
* Strong input validation
* Reproducible builds
* Health & readiness checks
* CI automation

---

## 📈 Possible Extensions

* Model retraining pipeline
* Data drift monitoring
* Authentication & rate limiting
* Cloud deployment (AWS/GCP)
* Feature store integration
* Advanced insurance GLMs

---

## 🎯 Why This Project Matters

This is **not a toy ML notebook**.

It demonstrates:

* Real ML inference service design
* Backend engineering best practices
* Production-ready CI/CD
* Full-stack ML system thinking

---

## 👨‍💻 Author

Built as part of **“Code Like a Pro”** learning journey
by an AI/ML Engineer focusing on **production-grade ML systems**.

---

## ⭐ Final Note

If you are reviewing this project:

* Start with `docker compose up`
* Explore `/docs`
* Check `.github/workflows/ci.yml`
* Review tests and architecture

This repository reflects **how ML systems are built in real companies**.

---
