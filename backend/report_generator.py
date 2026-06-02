from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(data, filename):

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph("SentinelX Incident Report", styles["Title"])
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Incident ID: {data['incident_id']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Attack: {data['attack']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Severity: {data['severity']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"MITRE: {data['mitre']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Risk Score: {data['risk_score']}",
            styles["Normal"]
        )
    )

    pdf.build(content)
