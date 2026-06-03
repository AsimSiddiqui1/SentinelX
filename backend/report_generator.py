import matplotlib.pyplot as plt
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(data, filename, incident_history):

    critical = 0
    high = 0
    medium = 0
    low = 0
    
    for incident in incident_history:

        severity = incident.get("severity", "")
    
        if severity == "Critical":
            critical += 1
    
        elif severity == "High":
            high += 1
    
        elif severity == "Medium":
            medium += 1
    
        elif severity == "Low":
            low += 1
        
    labels = []
    sizes = []
    colors = []
    
    if critical > 0:
        labels.append(f"Critical ({critical})")
        sizes.append(critical)
        colors.append("#E53935")
    
    if high > 0:
        labels.append(f"High ({high})")
        sizes.append(high)
        colors.append("#FB6A00")
    
    if medium > 0:
        labels.append(f"Medium ({medium})")
        sizes.append(medium)
        colors.append("#D4A000")
    
    if low > 0:
        labels.append(f"Low ({low})")
        sizes.append(low)
        colors.append("#1FA640")
    
    if len(sizes) == 0:
        labels = ["No Incidents"]
        sizes = [1]
        colors = ["#808080"]
    
    plt.figure(figsize=(4,4))
    
    plt.pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct="%1.0f%%",
        wedgeprops={"edgecolor": "white", "linewidth": 2}
    )
    plt.title("Severity Distribution")
    plt.savefig("severity_chart.png")
    plt.close()

    pdf = SimpleDocTemplate(filename)


    styles = getSampleStyleSheet()

    content = []

    # Logo
    try:
        logo = Image(
            "backend/assets/sentinelx_logo.png",
            width=100,
            height=100
        )
        content.append(logo)
        content.append(Spacer(1, 15))
    except:
        pass

    # Title
    content.append(
        Paragraph(
            "SentinelX Incident Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    # Executive Summary
    content.append(
        Paragraph("Executive Summary", styles["Heading1"])
    )

    content.append(
        Paragraph(
            f"Incident ID: {data.get('incident_id', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Attack Type: {data.get('attack', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Severity: {data.get('severity', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"MITRE Technique: {data.get('mitre', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Risk Score: {data.get('risk_score', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Target Asset: {data.get('asset', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Executive Summary",
            styles["Heading1"]
        )
    )
    
    content.append(
        Paragraph(
            f"""
            A {data.get('severity','N/A')} severity
            {data.get('attack','N/A')} incident was detected
            against {data.get('asset','N/A')}.
    
            Risk Score:
            {data.get('risk_score','N/A')}/100
    
            Immediate investigation and containment
            actions are recommended.
            """,
            styles["Normal"]
        )
    )
    
    content.append(Spacer(1, 20))

    mitre_id = data.get("mitre", "N/A")

    technique_name = "Unknown"
    tactic = "Unknown"
    
    if mitre_id == "T1566":
        technique_name = "Phishing"
        tactic = "Initial Access"
    
    elif mitre_id == "T1110":
        technique_name = "Brute Force"
        tactic = "Credential Access"
    
    elif mitre_id == "T1486":
        technique_name = "Data Encrypted for Impact"
        tactic = "Impact"
    
    content.append(
        Paragraph(
            "MITRE ATT&CK Mapping",
            styles["Heading1"]
        )
    )
    
    content.append(
        Paragraph(
            f"Technique ID: {mitre_id}",
            styles["Normal"]
        )
    )
    
    content.append(
        Paragraph(
            f"Technique Name: {technique_name}",
            styles["Normal"]
        )
    )
    
    content.append(
        Paragraph(
            f"Tactic: {tactic}",
            styles["Normal"]
        )
    )
    
    content.append(Spacer(1, 20))

    # Threat Intelligence
    content.append(
        Paragraph("Threat Intelligence", styles["Heading1"])
    )

    content.append(
        Paragraph(
            f"Suspicious IP: {data.get('ioc_ip', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Malicious Domain: {data.get('ioc_domain', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))

    # Gemini Analysis
    content.append(
        Paragraph("Gemini SOC Analyst", styles["Heading1"])
    )

    content.append(
        Paragraph(
            f"Summary: {data.get('ai_summary', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 5))

    content.append(
        Paragraph(
            f"Business Impact: {data.get('business_impact', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 5))

    content.append(
        Paragraph(
            f"Confidence: {data.get('confidence', 'N/A')}%",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 5))

    content.append(
        Paragraph(
            f"Verdict: {data.get('verdict', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 15))

    # Recommendations
    content.append(
        Paragraph("Recommendations", styles["Heading2"])
    )

    for rec in data.get("recommendations", []):
        content.append(
            Paragraph(
                f"• {rec}",
                styles["Normal"]
            )
        )

    content.append(Spacer(1, 20))

    # Generated Logs
    content.append(
        Paragraph("Generated Logs", styles["Heading1"])
    )

    for log in data.get("logs", []):
        content.append(
            Paragraph(
                f"• {log}",
                styles["Normal"]
            )
        )

    content.append(Spacer(1, 20))

    # Timeline
    content.append(
        Paragraph("Incident Timeline", styles["Heading1"])
    )

    for event in data.get("timeline", []):
        content.append(
            Paragraph(
                f"• {event}",
                styles["Normal"]
            )
        )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Generated by SentinelX AI-Powered SOC Platform",
            styles["Italic"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Security Analytics",
            styles["Heading1"]
        )
    )
    
    chart = Image(
        "severity_chart.png",
        width=250,
        height=250
    )

    content.append(chart)

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Dashboard Statistics",
            styles["Heading2"]
        )
    )
    
    content.append(
        Paragraph(
            f"Critical Incidents: {critical}",
            styles["Normal"]
        )
    )
    
    content.append(
        Paragraph(
            f"High Incidents: {high}",
            styles["Normal"]
        )
    )
    
    content.append(
        Paragraph(
            f"Medium Incidents: {medium}",
            styles["Normal"]
        )
    )
    
    content.append(
        Paragraph(
            f"Low Incidents: {low}",
            styles["Normal"]
        )
    )
        
    severity = data.get("severity", "N/A")
    
    if severity == "Critical":
        severity_text = "🔴 CRITICAL"
    
    elif severity == "High":
        severity_text = "🟠 HIGH"
    
    elif severity == "Medium":
        severity_text = "🟡 MEDIUM"
    
    else:
        severity_text = "🟢 LOW"
    
    content.append(
        Paragraph(
            f"Severity: {severity_text}",
            styles["Normal"]
        )
    )
    
    risk = int(data.get("risk_score", 0))
    
    filled = int(risk / 5)
    
    risk_bar = "█" * filled + "░" * (20 - filled)
    
    content.append(
        Paragraph(
            f"Risk Score: {risk}",
            styles["Normal"]
        )
    )
    
    content.append(
        Paragraph(
            f"Risk Meter: {risk_bar} {risk}/100",
            styles["Normal"]
        )
    )

    pdf.build(content)
