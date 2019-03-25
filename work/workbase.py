import sqlite3
import datetime
import sys


def 
class database():
    def __init__(self, db='work.db'):
        with sqlite3.connect(db) as conn:
            cur = conn.cursor()
            self.connection = conn
            self.cursor = cur
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS WORK (ID INTEGER PRIMARY KEY NOT NULL, DATE TEXT, TASK TEXT)""")
        self.connection.commit()

    def insert(self, date, task):
        self.cursor.execute("INSERT INTO WORK VALUES(NULL, ?, ?)",
                            (date, task))
        self.connection.commit()

    def view(self):
        self.cursor.execute("SELECT * FROM WORK")
        return self.cursor.fetchall()

    def search(self, date=None, task=None, id=None):
        self.cursor.execute("SELECT * FROM WORK WHERE DATE=? OR TASK=? OR ID=?",
                            (date, task, id))
        return self.cursor.fetchall()

    def delete(self, id):
        self.cursor.execute("DELETE FROM WORK WHERE ID=?", (id,))
        self.connection.commit()

    def update(self, id, date=None, task=None, year=None, isbn=None):
        status_quo = self.search(id=id)[0]
        if not date:
            date = status_quo[1]
        if not task:
            task = status_quo[2]
        if not year:
            year = status_quo[3]
        if not isbn:
            isbn = status_quo[4]
        self.cursor.execute("UPDATE WORK SET DATE=?, TASK=? WHERE ID=?",
                            (date, task, id))
        self.connection.commit()

#db = database()
arg_input = sys.argv
