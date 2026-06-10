from mitigation_engine import (
    mitigate_rf_jamming,
    mitigate_gps_spoofing,
    mitigate_unauthorized_command
)
from incident_response import create_incident
import pandas as pd
import joblib
import time

from sklearn.preprocessing import LabelEncoder

model = joblib.load(
    "satellite_ai_model.pkl"
)

severity_encoder = LabelEncoder()
severity_encoder.fit(
    ["LOW", "HIGH", "CRITICAL"]
)

command_encoder = LabelEncoder()
command_encoder.fit(
    ["AUTHORIZED", "ATTACKER"]
)

last_row_count = 0

while True:

    data = pd.read_csv(
        "../data/telemetry.csv"
    )

    current_rows = len(data)

    if current_rows > last_row_count:

        latest = data.iloc[-1]

        severity = severity_encoder.transform(
            [latest["severity"]]
        )[0]

        command_source = command_encoder.transform(
            [latest["command_source"]]
        )[0]

        features = [[

            latest["signal_strength"],

            latest["power_level"],

            latest["temperature"],

            latest["cpu_usage"],

            latest["latitude"],

            latest["longitude"],

            severity,

            command_source
        ]]

        prediction = model.predict(features)

        attack = prediction[0]
        if attack == "RF_JAMMING":

            latest = mitigate_rf_jamming(
                latest
            )

        elif attack == "GPS_SPOOFING":

            latest = mitigate_gps_spoofing(

                latest,

                trusted_lat=33.6844,

                trusted_lon=73.0479
            )

        elif attack == (
                "UNAUTHORIZED_COMMAND"
        ):

            latest = (
                mitigate_unauthorized_command(
                    latest
                )
            )
        print(
            "\nUPDATED TELEMETRY"
        )

        print(
            latest
        )

        if attack != "NORMAL":
            create_incident(
                attack,
                latest["severity"],
                latest["incident_id"]
            )

        print(
            "\nAI DETECTION RESULT"
        )

        print(
            "Attack Type:",
            prediction[0]
        )

        print(
            "Severity:",
            latest["severity"]
        )

        print(
            "Incident:",
            latest["incident_id"]
        )

        print(
            "-" * 40
        )

        last_row_count = current_rows

    time.sleep(3)