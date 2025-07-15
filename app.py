from flask import Flask, render_template, request, send_file
import pandas as pd
from scraper.basic_scraper import fetch_basic_info

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    if request.method == "POST":
        urls = request.form["urls"].split()
        results = [fetch_basic_info(url) for url in urls]
        pd.DataFrame(results).to_csv("data/output.csv", index=False)
        data = results
    return render_template("index.html", data=data)

@app.route("/download")
def download():
    return send_file("data/output.csv", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
