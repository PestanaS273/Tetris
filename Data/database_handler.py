import sqlite3
import os

class database_handler:
    def __init__(self, database_name : str):
        self.conn = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
        self.conn.row_factory = sqlite3.Row

    def insertScore(self, score : int):
        cursor = self.conn.cursor()
        query = f"INSERT INTO Score (score) VALUES ('{score}');"
        cursor.execute(query)
        cursor.close()
        self.conn.commit()


    def getHighScore(self):
        cursor = self.conn.cursor()
        query = f"SELECT id_score, Max(score) as score FROM Score;"
        cursor.execute(query)
        row = cursor.fetchone()
        cursor.close()
        return str(row["score"])