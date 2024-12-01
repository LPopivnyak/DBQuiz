from flask import *

from DBManager import DBManager

app = Flask("Quiz")
db_name = "quiz.db"
app.secret_key = "12345677890"

@app.route("/")
def index():
    db_manager = DBManager(db_name)
    quizzes = db_manager.receive_quizzies()
    return render_template("index.html", quizzes=quizzes)

@app.route("/rickroll")
def rickroll():
    return render_template("rickroll.html")

@app.route("/quizzies/<int:quiz_id>")
def get_questions(quiz_id):
    db_manager = DBManager(db_name)
    questions = db_manager.receive_questions(quiz_id)

    session["questions"] = questions
    session["true_ans"] = 0
    session["quest_index"] = 0
    return redirect(url_for("show_questions", quiz_id=quiz_id))

@app.route("/quizzies/<int:quiz_id>/questions")
def show_questions(quiz_id):
    number = session["quest_index"]
    q = session["questions"][number]
    db_manager = DBManager(db_name)
    options = db_manager.receive_options(q[0])

    return render_template("question.html", question=q, options=options, quiz_id=quiz_id)

@app.route("/quizzies/<int:quiz_id>/answer", methods=["POST"])
def answer_func(quiz_id):
    session["quest_index"] += 1

    if len(session["questions"]) <= session["quest_index"]:
        return redirect(url_for("result", quiz_id=quiz_id))
    else:
        return redirect(url_for("show_question", quiz_id=quiz_id))

@app.route("/quizzies/<int:quiz_id>/result")
def result(quiz_id):
    return "РЕЗУЛЬТАТ"


app.run()