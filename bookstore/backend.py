import sqlite3

class database():
    def __init__(self, db='books.db'):
        with sqlite3.connect(db) as conn:
            cur = conn.cursor()
            self.connection = conn
            self.cursor = cur
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS BOOK (ID INTEGER PRIMARY KEY NOT NULL, TITLE TEXT, AUTHOR TEXT, YEAR INTEGER, ISBN INTEGER)""")
        self.connection.commit()

    def insert(self, title, author, year, isbn):
        self.cursor.execute("INSERT INTO BOOK VALUES(NULL, ?, ?, ?, ?)",
                            (title, author, year, isbn))
        self.connection.commit()

    def view(self):
        self.cursor.execute("SELECT * FROM BOOK")
        return self.cursor.fetchall()

    def search(self, title=None, author=None, year=None, isbn=None, id=None):
        self.cursor.execute("SELECT * FROM BOOK WHERE TITLE=? OR AUTHOR=? OR YEAR=? OR ISBN=? OR ID=?",
                            (title, author, year, isbn, id))
        return self.cursor.fetchall()

    def delete(self, id):
        self.cursor.execute("DELETE FROM BOOK WHERE ID=?", (id,))
        self.connection.commit()

    def update(self, id, title=None, author=None, year=None, isbn=None):
        status_quo = self.search(id=id)[0]
        if not title:
            title = status_quo[1]
        if not author:
            author = status_quo[2]
        if not year:
            year = status_quo[3]
        if not isbn:
            isbn = status_quo[4]
        self.cursor.execute("UPDATE BOOK SET TITLE=?, AUTHOR=?, YEAR=?, ISBN=? WHERE ID=?",
                            (title, author, year, isbn, id))
        self.connection.commit()

db = database()
