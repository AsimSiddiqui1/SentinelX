def generate_alert(
    incident_id,
    attack,
    severity,
    target
):

    return f"""
==============================
      SOC ALERT
==============================

Incident ID : {incident_id}

Attack      : {attack}
Severity    : {severity}

Target      : {target['id']}
Asset Type  : {target['type']}

Status      : OPEN

SOC Action Required

==============================
"""
