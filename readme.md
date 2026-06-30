# 🏥 Healthcare AI System

![Python](https://img.shields.io/badge/python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-red)
![DVC](https://img.shields.io/badge/DVC-Pipeline-purple)

> **Production First Architecture. Not Slideware. — #ArchitectMindset**

An end-to-end enterprise machine learning system built on real hospital data — from raw CSVs to AWS Kubernetes deployment, with full MLOps tooling, monitoring, and governance.

---

## 🎯 What This System Does

| Model | Input | Prediction | Business Value |
|------|--------|------------|----------------|
| **Visit Risk Classifier** | Patient + Visit data | Low / Medium / High risk | Helps hospital ops teams triage and allocate staff proactively |
| **Claim Outcome Predictor** | Billing + Visit data | Paid / Pending / Rejected | Helps finance teams detect rejection-prone claims before submission |

---

## 🏗️ System Architecture

Raw Hospital Data  
(patients.csv · visits.csv · billing.csv)  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
SQL Analytics Layer (SQLite · hospital.db)  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
EDA + Feature Engineering  
(distributions · outliers · feature creation · label fixes)  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
ML Models  
(Model A — Visit Risk · Model B — Claim Outcome)  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
MLOps Layer  
- MLflow (experiment tracking)  
- DVC (data versioning + pipelines)  
- Model artifacts (joblib files)  
- Feature schema (single source of truth)  
- Prediction logs (audit trail)  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
Serving Layer  
- FastAPI (REST APIs)  
- Pydantic (validation)  
- Gradio UI (demo)  
- PSI drift monitoring  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
Cloud Deployment  
- Docker (containerization)  
- AWS ECR (image registry)  
- AWS EKS (Kubernetes cluster)  
- GitHub Actions (CI/CD pipeline)  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
Retraining Loop  
(drift detection → DVC repro → model update)

---

## 📁 Project Structure

Healthcare/  
├── data/  
├── db/  
├── notebooks/  
├── src/  
├── api/  
├── ui/  
├── monitoring/  
├── models/  
├── outputs/  
├── mlruns/  
├── mlartifacts/  
├── mlflow.db  
├── logs/  
├── dvc-storage/  
├── dvc.yaml  
├── dvc.lock  
├── report/  
├── tests/  
├── Dockerfile  
├── docker-compose.yml  
├── .github/workflows/  
├── requirements.txt  
└── README.md  

---

## 🗄️ Dataset Overview

patients.csv (5,000 rows)
- patient_id: int
- age: int
- gender: str
- city: str
- insurance_provider: str
- chronic_flag: int
- registration_date: date

visits.csv (25,000 rows)
- visit_id: int
- patient_id: int
- visit_date: date
- department: str
- visit_type: str
- length_of_stay_hours: float
- risk_score: target (Low / Medium / High)
- doctor_id: int

billing.csv (25,000 rows)
- bill_id: int
- visit_id: int
- billed_amount: float
- approved_amount: float
- claim_status: target (Paid / Pending / Rejected)
- payment_days: float
- billing_date: date

---

## 🚀 Quick Start

git clone https://github.com/chabdullah7/Health_Care_AI_ML_Pipeline.git  
cd Healthcare  

uv venv  
source .venv/Scripts/activate  
uv pip install -r requirements.txt  

---

## ▶️ Run Project

Train Models:
python -m src.training_pipeline --model risk  
python -m src.training_pipeline --model claim  

Run API:
uvicorn api.main:app --reload  

Run UI:
python ui/gradio_app.py  

API Docs:
http://localhost:8000/docs  

---

## ☁️ AWS Deployment

- Docker images pushed to AWS ECR  
- Kubernetes deployment via AWS EKS  
- CI/CD via GitHub Actions  

---

## 📊 Model Performance

| Model | Algorithm | Accuracy | F1 Score |
|------|----------|----------|---------|
| Visit Risk | XGBoost | ~95% | 0.94 |
| Claim Outcome | Random Forest | ~55% | 0.51 |

---

## 🔍 Key Engineering Highlights

- End-to-end ML lifecycle (train → deploy → monitor → retrain)
- Data leakage-safe pipeline design
- MLflow experiment tracking
- DVC pipeline versioning
- PSI drift detection
- Docker + Kubernetes deployment
- CI/CD automation with GitHub Actions

---

## 👨‍💻 Author

Abdullah  
AI/ML Engineer  

GitHub: https://github.com/chabdullah7  
LinkedIn: www.linkedin.com/in/chabdullah7
