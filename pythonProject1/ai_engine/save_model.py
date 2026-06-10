import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from sklearn.preprocessing import LabelEncoder

import joblib

data = pd.read_csv("../data/telemetry.csv")

severity_encoder = LabelEncoder()

command_encoder = LabelEncoder()

data["severity"] = severity_encoder.fit_transform(
    data["severity"]
)

data["command_source"] = command_encoder.fit_transform(
    data["command_source"]
)

X = data[
    [
        "signal_strength",
        "power_level",
        "temperature",
        "cpu_usage",
        "latitude",
        "longitude",
        "severity",
        "command_source"
    ]
]

y = data["attack_type"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "satellite_ai_model.pkl")

print("Model Saved Successfully")