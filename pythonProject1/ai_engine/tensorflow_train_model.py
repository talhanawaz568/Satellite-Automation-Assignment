import pandas as pd

from sklearn.model_selection import (
    train_test_split
)

from sklearn.preprocessing import (
    LabelEncoder,
    StandardScaler
)

import tensorflow as tf

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import (
    Dense
)

# Load Dataset

data = pd.read_csv(
    "../data/telemetry.csv"
)

# Remove Empty Attack Records

data = data.dropna(
    subset=["attack_type"]
)

# Encode Severity

severity_encoder = LabelEncoder()

data["severity"] = (
    severity_encoder.fit_transform(
        data["severity"]
    )
)

# Encode Command Source

command_encoder = LabelEncoder()

data["command_source"] = (
    command_encoder.fit_transform(
        data["command_source"]
    )
)

# Encode Attack Type

attack_encoder = LabelEncoder()

data["attack_type"] = (
    attack_encoder.fit_transform(
        data["attack_type"]
    )
)

# Features

X = data[[

    "signal_strength",

    "power_level",

    "temperature",

    "cpu_usage",

    "latitude",

    "longitude",

    "severity",

    "command_source"

]]

# Feature Scaling

scaler = StandardScaler()

X = scaler.fit_transform(
    X
)

# Target

y = data["attack_type"]

# Split Dataset

X_train, X_test, y_train, y_test = (

    train_test_split(

        X,

        y,

        test_size=0.2,

        random_state=42
    )
)

# Neural Network

model = Sequential([

    Dense(
        64,
        activation="relu",
        input_shape=(8,)
    ),

    Dense(
        32,
        activation="relu"
    ),

    Dense(
        len(
            attack_encoder.classes_
        ),
        activation="softmax"
    )

])

# Compile Model

model.compile(

    optimizer="adam",

    loss="sparse_categorical_crossentropy",

    metrics=["accuracy"]

)

# Train Model

history = model.fit(

    X_train,

    y_train,

    epochs=40,

    validation_split=0.2,

    verbose=1
)

# Evaluate

loss, accuracy = model.evaluate(

    X_test,

    y_test
)

print(
    "\nTensorFlow Accuracy:",
    accuracy
)

# Save Model

model.save(
    "satellite_tf_model.keras"
)

print(
    "\nTensorFlow Model Saved"
)

print(
    "\nAttack Classes:"
)

print(
    attack_encoder.classes_
)