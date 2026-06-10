from datetime import datetime
import csv


def log_mitigation(
        attack,
        action,
        result
):

    with open(
            "../data/mitigation_log.csv",
            "a",
            newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(

            [
                datetime.now(),
                attack,
                action,
                result
            ]
        )


def mitigate_rf_jamming(
        row
):

    print(
        "\n[MITIGATION]"
    )

    print(
        "Frequency Hopping Activated"
    )

    print(
        "Spread Spectrum Activated"
    )

    row["signal_strength"] = -45

    log_mitigation(

        "RF_JAMMING",

        "Frequency Hopping + Spread Spectrum",

        "Signal Recovered"
    )

    return row


def mitigate_gps_spoofing(

        row,
        trusted_lat,
        trusted_lon
):

    print(
        "\n[MITIGATION]"
    )

    print(
        "GPS Validation Activated"
    )

    row["latitude"] = trusted_lat

    row["longitude"] = trusted_lon

    log_mitigation(

        "GPS_SPOOFING",

        "Restore Trusted Coordinates",

        "Navigation Restored"
    )

    return row


def mitigate_unauthorized_command(
        row
):

    print(
        "\n[MITIGATION]"
    )

    print(
        "Account Isolated"
    )

    row["command_source"] = (
        "AUTHORIZED"
    )

    log_mitigation(

        "UNAUTHORIZED_COMMAND",

        "Account Isolation",

        "Access Blocked"
    )

    return row