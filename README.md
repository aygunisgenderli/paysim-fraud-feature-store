
# PaySim Fraud Detection - Reusable Feature Store using Feast

This project implements a production-grade, reusable feature store infrastructure for training and serving machine learning models using **Feast**, **Apache Parquet**, and **Redis**. 

The architecture guarantees consistent feature engineering logic across both offline training (batch) and online low-latency inference (real-time serving), eliminating training-serving skew.

## 🚀 System Architecture & Stack
- **Offline Store:** Apache Parquet format (Batch feature storage)
- **Online Store:** Redis In-Memory Database (Ultra-low latency inference serving)
- **Feature Store Framework:** Feast Architecture

## 🛠️ Project Structure
```text
feature_repo/
├── data/
│   └── paysim_features.parquet   # Local batch storage (Synthetic PaySim data)
├── definitions.py                # Defined entities and feature views
├── feature_store.yaml            # Feast infrastructure configuration (Redis + File)
├── note.md                       # Technical report on engineering trade-offs
└── Week5Task.ipynb               # Step-by-step Colab workflow
