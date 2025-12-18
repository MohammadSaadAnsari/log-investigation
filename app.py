from flask import Flask, render_template, request, send_file
import pandas as pd
import json
from reports import generate_pdf_report

USE_MOCK = True

app = Flask(__name__)

def load_data(file=None):
    if USE_MOCK:
        with open("mock_data.json") as f:
            return pd.DataFrame(json.load(f))
    else:
        return pd.read_csv(file)

@app.route("/", methods=["GET", "POST"])
def index():
    df = pd.DataFrame()
    filtered = pd.DataFrame()
    error = None

    try:
        if request.method == "POST":
            df = load_data(request.files.get("logfile"))

            # Filters
            source_ip = request.form.get("source_ip")
            protocol = request.form.get("protocol")
            threat = request.form.get("inferred_threat")

            filtered = df.copy()

            if source_ip:
                filtered = filtered[filtered["source_ip"] == source_ip]
            if protocol:
                filtered = filtered[filtered["protocol"] == protocol]
            if threat:
                filtered = filtered[filtered["inferred_threat"] == threat]

    except Exception as e:
        error = str(e)

    return render_template(
        "index.html",
        results=filtered.to_dict(orient="records"),
        ips=df["source_ip"].unique().tolist() if not df.empty else [],
        protocols=df["protocol"].unique().tolist() if not df.empty else [],
        threats=df["inferred_threat"].unique().tolist() if not df.empty else [],
        error=error
    )

@app.route("/export/csv", methods=["POST"])
def export_csv():
    df = load_data()
    df.to_csv("export.csv", index=False)
    return send_file("export.csv", as_attachment=True)

@app.route("/export/pdf", methods=["POST"])
def export_pdf():
    df = load_data()
    pdf_path = generate_pdf_report(df)
    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
