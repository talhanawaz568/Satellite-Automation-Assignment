import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from sklearn.preprocessing import LabelEncoder

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

model = RandomForestClassifier()

model.fit(X, y)

for feature, importance in zip(
        X.columns,
        model.feature_importances_):

    print(feature, ":", importance)