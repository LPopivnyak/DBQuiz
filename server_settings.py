from flask import *

app = Flask("Quiz")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/rickroll")
def rickroll():
    return render_template("rickroll.html")

app.run()