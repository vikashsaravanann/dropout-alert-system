🚀 PS-1: Early Alert System for Girl Student Dropout Risk
!(https://www.google.com/search?q=https://img.shields.io/badge/Status-Prototype-green)!(https://img.shields.io/badge/AI-XGBoost-blue)

📖 Project Overview
A machine-learning powered Android application designed for rural Indian schools to predict dropout risks among girl students. The system operates offline-first, performing inference on the edge device to overcome connectivity barriers. It integrates with Renault Nissan's CSR initiatives (Blossom Bus) to provide logistical interventions.

💡 Key Features
Edge AI Inference: Uses TFLite/ONNX to run XGBoost models locally on Android devices.

Explainable AI (XAI): SHAP values provide teachers with the reason behind a risk alert (e.g., "Frequent Health Absences").

CSR Resource Optimization: Geospatial clustering of high-risk students to optimize school bus routes.

Privacy Preserving: PII data remains local; only model weights/anonymized stats are synced.

🛠️ Tech Stack
ML Core: Python, XGBoost, SHAP, Scikit-learn.

Mobile App: Flutter (Dart) with tflite_flutter plugin.

Backend: FastAPI (Python), PostgreSQL.

Infrastructure: Docker, Google Maps API (for Route Optimization).

📊 Dataset & Modeling
We utilized the UDISE+ and synthetic rural education datasets to train our model.

Target Variable: Dropout (Binary: 0/1).

Key Features: attendance_pattern, distance_to_school, toilet_availability, parental_income, academic_velocity.
