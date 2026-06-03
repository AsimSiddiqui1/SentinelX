from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(data, filename):

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []
    logo = Image(
    "backend/assets/sentinelx_logo.png",
    width=100,
    height=100
    )
    
    content.append(logo)
    content.append(Spacer(1, 20))

    content.append(
        Paragraph("SentinelX Incident Report", styles["Title"])
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Incident ID: {data.get('incident_id', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Attack: {data.get('attack', 'N/A')}",
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
            f"MITRE: {data.get('mitre', 'N/A')}",
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
    
    content.append(
        Paragraph("Threat Intelligence", styles["Heading2"])
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

    content.append(
        Paragraph("Gemini SOC Analyst", styles["Heading2"])
    )
    
    content.append(
        Paragraph(
            f"Summary: {data.get('ai_summary', 'N/A')}",
            styles["Normal"]
        )
    )
    
    content.append(
        Paragraph(
            f"Business Impact: {data.get('business_impact', 'N/A')}",
            styles["Normal"]
        )
    )
    
    content.append(
        Paragraph(
            f"Confidence: {data.get('confidence', 'N/A')}%",
            styles["Normal"]
        )
    )
    
    content.append(
        Paragraph(
            f"Verdict: {data.get('verdict', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph("Recommendations", styles["Heading3"])
    )
    
    for rec in data.get("recommendations", []):
        content.append(
            Paragraph(f"• {rec}", styles["Normal"])
        )
        pdf.build(content)
