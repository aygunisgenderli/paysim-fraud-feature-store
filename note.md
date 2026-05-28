# Feature Store Design and Trade-offs (PaySim Fraud Project)

## 1. Architecture Overview
- **Offline Store:** Apache Parquet format (`data/paysim_features.parquet`). Used for batch storage, data analysis, and point-in-time historical queries for ML model training.
- **Online Store:** Redis In-Memory Database (`redis://localhost:6379`). Used for low-latency, ultra-fast online feature serving during inference.
- **Feature Store Framework:** Feast (Feature Store for Machine Learning).

## 2. Defined Entities & Features
- **Entity:** `customer_id` (mapped via `nameOrig` join key).
- **Feature View:** `customer_transaction_stats`
  - `amount` (Float32)
  - `oldbalanceOrg` (Float32)
  - `newbalanceOrig` (Float32)
  - `transaction_count` (Int64)

## 3. Core Trade-offs & Engineering Decisions
- **Storage Cost vs. Latency:** Moving from SQLite to Redis increases operational/infrastructure costs, but drastically reduces online inference latency from milliseconds to microseconds, which is a hard requirement for real-time banking fraud detection.
- **Feature Freshness (TTL):** Managed with a 30-day Time-To-Live (TTL) policy. This limits storage footprint in Redis and ensures old, stale behavioral data does not negatively impact model accuracy.
- **Consistency:** Feast guarantees that the exact same feature engineering logic is applied during training (Offline) and serving (Online), eliminating the notorious "Training-Serving Skew".