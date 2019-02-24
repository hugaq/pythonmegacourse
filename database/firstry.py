import psycopg2


def create_table():
    with sqlite3.connect('lite.db') as conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS STORE (ITEM TEXT, QUANTITY INTEGER, PRICE REAL)')
        conn.commit()

def insert(item, quantity, price):
    with sqlite3.connect('lite.db') as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO STORE VALUES (?, ?, ?)', (item, quantity, price))
        conn.commit()

def view():
    with sqlite3.connect('lite.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM STORE')
        return cur.fetchall()


insert('Coffee Cup', 5, 22.2)
print(view())
