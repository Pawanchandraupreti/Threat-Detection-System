import pandas as pd

from sklearn.ensemble import IsolationForest

# Load log data (example: CSV exported from Elasticsearch)
logs = pd.read_csv("sample_logs/auth_attempts.csv")
X = logs[["login_attempts", "src_ip_count"]]  # Features for anomaly detection

# Train ML model
model = IsolationForest(contamination=0.01, random_state=42)
model.fit(X)
logs["anomaly"] = model.predict(X)

# Save detected anomalies
anomalies = logs[logs["anomaly"] == -1]
anomalies.to_csv("detected_anomalies.csv")
print(f"Detected {len(anomalies)} anomalies!")


