"""
Purpose: record working hours in a simple and easy manner and eventually depict
         them visually.

Input: Either via commandline or from within the program. In both cases without
       GUI. Date can be given at the beginning, if this is not done, current date
       and time will be inserted.
"""
import sqlite3
import datetime
import sys


def time_padding(timepiece):
    timepieces = timepiece.split(':')
    for i in range(2):
        if len(timepieces[i]) == 1:
            timepieces[i] = '0'+timepieces[i]
    return ':'.join(timepieces)

def date_padding(datepiece):
    datepieces = datepiece.split('.')
    for i in range(len(datepieces)):
        if len(datepieces[i]) == 1:
            datepieces[i] = '0'+datepieces[i]
    if len(datepieces) == 1:
        datepieces.append(datetime.datetime.now().strftime('%m.%y'))
    elif len(datepieces) == 2:
        datepieces.append(datetime.datetime.now().strftime('%y'))
    return '.'.join(datepieces)

def determine_datetime(timestamp):
    pit = datetime.datetime.now().strftime('%d.%m.%y %H:%M').split(' ')
    return_dict = {'time':pit[1], 'date':pit[0]}
    if timestamp:
        parts = timestamp.split(' ')
        for part in parts:
            if ':' in part:
                return_dict['time'] = time_padding(part)
            else:
                return_dict['date'] = date_padding(part)
    return f"{return_dict['date']} {return_dict['time']}"


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
print(determine_datetime(arg_input[1]))
