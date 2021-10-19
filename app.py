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

# "/raw" RAW (renders html raw format)
@app.route("/raw")
def raw():
    return """
    <!DOCTYPE HTML>
    <html>
        <head>
            <meta charset="utf-8">
            <title>RAW</title>
            <link rel="stylesheet" type="text/css" href="/static/styles.css">
        </head>
        <body>
            <header class="flex">
                <a href="/" class="nav title">FLASK</a>
                <a href="/" class="nav">Home</a>
                <a href="/about" class="nav">About</a>
                <a href="/api/data" class="nav">Data</a>
                <a href="/raw" class="nav">RAW</a>
            </header>
            <div class="root flex">
                <h2>RAW PAGE</h2>
                <p>Custom Generated HTML Page for "/raw" extension using "app.py" only</p>
                <h3>See the Difference</h3>
                <p class="believe">
                    <span class="see">Anything is possible!</span> Just unleash your creativity and go with it!
                </p>
                <p>Sometimes, it only takes a bit of courage to try something new!</p>
            </div>
        </body>
    </html>
    """