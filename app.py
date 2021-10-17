from flask import Flask, render_template
from datetime import datetime
import re

# Main Flask App
app = Flask(__name__)

# Homepage "/"
@app.route("/")
def home():
    return render_template("home.html")

# "/hello/<name>" Route
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "index.html", name=name, date=datetime.now()
    )

# "/api/data" Route (renders json file)
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

# "/about/" Route
@app.route("/about/")
def about():
    return render_template("about.html")
