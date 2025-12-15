from flask import Flask, render_template, request
import pandas as pd
import json

# Toggle this later when ML is ready
USE_MOCK = True

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    error = None

    if request.method == "POST":
        try:
            if USE_MOCK:
                with open("mock_data.json", "r") as f:
                    results = json.load(f)
            else:
                file = request.files["logfile"]
                df = pd.read_csv(file)
                results = df.to_dict(orient="records")
        except Exception as e:
            error = str(e)

    return render_template("index.html", results=results, error=error)

if __name__ == "__main__":
    app.run(debug=True)
