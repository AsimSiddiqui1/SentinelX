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

    pdf.build(content)
