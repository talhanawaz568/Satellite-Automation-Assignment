import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import classification_report

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

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(classification_report(y_test, predictions))