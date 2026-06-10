import random
import time
import pandas as pd
from datetime import datetime

telemetry_file = "../data/telemetry.csv"

while True:

    signal_strength = random.randint(80, 100)

    power_level = random.randint(70, 95)

    temperature = random.randint(20, 35)

    cpu_usage = random.randint(30, 70)

    latitude = round(random.uniform(24.80, 24.90), 6)

    longitude = round(random.uniform(67.00, 67.10), 6)

    communication_status = "NORMAL"

    telemetry = {
        "timestamp": datetime.now(),
        "signal_strength": signal_strength,
        "power_level": power_level,
        "temperature": temperature,
        "cpu_usage": cpu_usage,
        "latitude": latitude,
        "longitude": longitude,
        "communication_status": communication_status
    }

    print(telemetry)

    df = pd.DataFrame([telemetry])

    df.to_csv(
        telemetry_file,
        mode="a",
        header=False,
        index=False
    )

    time.sleep(5)


    #------------------------------------------------------------------------------------

    import random
    import time
    import pandas as pd
    from datetime import datetime

    telemetry_file = "../data/telemetry.csv"

    while True:

        attack_probability = random.randint(1, 100)

        # ========================
        # NORMAL TELEMETRY
        # ========================

        signal_strength = random.randint(85, 100)

        power_level = random.randint(70, 90)

        temperature = random.randint(20, 35)

        cpu_usage = random.randint(30, 60)

        latitude = round(random.uniform(24.80, 24.90), 6)

        longitude = round(random.uniform(67.00, 67.10), 6)

        communication_status = "NORMAL"

        attack_type = "NORMAL"

        # ========================
        # RF JAMMING SIMULATION
        # ========================

        if attack_probability <= 10:

            signal_strength = random.randint(5, 25)

            communication_status = "DEGRADED"

            attack_type = "RF_JAMMING"

        # ========================
        # GPS SPOOFING SIMULATION
        # ========================

        elif attack_probability <= 20:

            latitude = round(random.uniform(40.0, 60.0), 6)

            longitude = round(random.uniform(30.0, 50.0), 6)

            communication_status = "SUSPICIOUS"

            attack_type = "GPS_SPOOFING"

        telemetry = {
            "timestamp": datetime.now(),
            "signal_strength": signal_strength,
            "power_level": power_level,
            "temperature": temperature,
            "cpu_usage": cpu_usage,
            "latitude": latitude,
            "longitude": longitude,
            "communication_status": communication_status,
            "attack_type": attack_type
        }

        print(telemetry)

        df = pd.DataFrame([telemetry])

        df.to_csv(
            telemetry_file,
            mode="a",
            header=False,
            index=False
        )

        time.sleep(5)

