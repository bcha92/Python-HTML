from flask import Flask, render_template
from datetime import datetime
import re

# Main Flask App
app = Flask(__name__)

# Homepage "/"
@app.route("/")
def home():
    return "Hello Flask!"

# "/hello/<name>" Route
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "index.html", name=name, date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")