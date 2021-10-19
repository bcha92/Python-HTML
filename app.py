from flask import Flask, render_template
from datetime import datetime

# Main Flask App
app = Flask(__name__)

# Homepage "/"
@app.route("/")
def home():
    return render_template("extend.html",
    title="FLASK HOME",
    subtitle="Home Page",
    content="This site was generated using VSCode Python FLASK Library"
    )

# "/about/" Route
@app.route("/about")
def about():
    return render_template("extend.html",
    title="FLASK ABOUT",
    subtitle="About",
    content="Some neat tricks with Flask",
    subcontent="Date and time right now: " + datetime.now().strftime("%A, %d %B, %Y at %X")
    )

# "/api/data" Route (renders json file)
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("/raw")
def raw():
    return """
    <div>
        <h1>RAW PAGE</h1>
        <p>Custom Generated Page for </p>
    </div>
    """