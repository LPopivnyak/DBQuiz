from flask import *

from DBManager import DBManager

app = Flask("Quiz")
db_name = "quiz.db"

@app.route("/")
def index():
    db_manager = DBManager("db_name")
    quizzes = db_manager.receive_quizzies()
    return render_template("index.html", quizzes=quizzes)

@app.route("/rickroll")
def rickroll():
    return render_template("rickroll.html")

app.run()