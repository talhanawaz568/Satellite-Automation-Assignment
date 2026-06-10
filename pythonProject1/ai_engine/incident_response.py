import datetime

def create_incident(
        attack_type,
        severity,
        incident_id):

    timestamp = datetime.datetime.now()

    incident = f"""
=================================
INCIDENT CREATED
=================================
Time: {timestamp}
Incident ID: {incident_id}
Attack Type: {attack_type}
Severity: {severity}
=================================
"""

    print(incident)

    with open(
            "../logs/incident_log.txt",
            "a"
    ) as file:

        file.write(incident)