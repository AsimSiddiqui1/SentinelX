def generate_report(
    incident_id,
    attack,
    target,
    severity,
    mitre,
    logs,
    timeline
):

    report = f"""
==================================
      INCIDENT REPORT
==================================

Incident ID:
{incident_id}

Attack Type:
{attack}

MITRE Technique:
{mitre}

Severity:
{severity}

Target Asset:
{target['id']}

Asset Type:
{target['type']}

Criticality:
{target['criticality']}

Generated Logs:
"""

    for log in logs:
        report += f"\n- {log}"

    report += "\n\nTimeline:"

    for event in timeline:
        report += f"\n- {event}"

    report += """

==================================
End of Report
==================================
"""

    return report

def save_report(report, incident_id):

    filename = f"reports/{incident_id}.txt"

    with open(filename, "w") as file:
        file.write(report)

    return filename
