import pandas as pd

data = pd.read_csv(
    "../data/telemetry.csv"
)

print(
    data["attack_type"]
    .value_counts(
        dropna=False
    )
)