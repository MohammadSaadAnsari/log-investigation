from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(df):
    file_name = "investigation_report.pdf"
    doc = SimpleDocTemplate(file_name)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("AI Log Investigation Report", styles["Title"]))
    elements.append(Paragraph(f"Total Records: {len(df)}", styles["Normal"]))

    anomalies = df[df["is_anomaly"] == True]
    elements.append(Paragraph(f"Anomalies Detected: {len(anomalies)}", styles["Normal"]))

    table_data = [["Source IP", "Threat", "Risk", "Reason"]]

    for _, row in anomalies.iterrows():
        table_data.append([
            row["source_ip"],
            row["inferred_threat"],
            str(row["risk_score"]),
            row["reason"]
        ])

    elements.append(Table(table_data))
    doc.build(elements)

    return file_name
