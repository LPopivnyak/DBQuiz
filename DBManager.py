import sqlite3


class DBManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)

    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Quizzies (
            id INT PRIMARY KEY,
            title VARCHAR(255),
            description TEXT
        );
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Questions (
            id INT PRIMARY KEY,
            quiz_id INT,
            content TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Options (
            id INT PRIMARY KEY,
            question_id INT,
            content TEXT,
            Is_correct BOOLEAN
        );
        """)

        self.connection.commit()



    def add_quiz(self, id, title, description):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Quizzies(id, title, description) VALUES (?, ?, ?)", [id, title, description])
        self.connection.commit()
        cursor.close()

    def add_question(self, id, Quiz_id, content):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Questions(id, Quiz_id, content) VALUES (?, ?, ?)", [id, Quiz_id, content])
        self.connection.commit()
        cursor.close()

    def add_options(self, id, Question_id, content):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Questions(id, Question_id, content) VALUES (?, ?, ?)", [id, Question_id, content])
        self.connection.commit()
        cursor.close()


    def receive_quizzies(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Quizzies")
        res = cursor.fetchall()
        cursor.close()
        return res

    def receive_questions(self, quiz_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Questions WHERE quiz_id = ?", [quiz_id])
        res = cursor.fetchall()
        cursor.close()
        return res

    def receive_options(self, question_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Questions WHERE quiz_id = ?", [question_id])
        res = cursor.fetchall()
        cursor.close()
        return res