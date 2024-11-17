from DBManager import DBManager

db_manager = DBManager("quiz.db")
db_manager.create_tables()

#db_manager.add_quiz(1,
 #                   "Квіз про Україну",
#                    "sdkjglsdgjrlsgj")

#print(db_manager.receive_quizzies())
print(db_manager.receive_questions())
#db_manager.add_question(1, 1, "Коли Україна стала незалежною?")