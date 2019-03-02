import psycopg2


def create_table():
    with psycopg2.connect("dbname='dbname' user='user' password='password' host='host' port='5432'") as conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS STORE (ITEM TEXT, QUANTITY INTEGER, PRICE REAL)')
        conn.commit()

def insert(item, quantity, price):
    with psycopg2.connect('lite.db') as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO STORE VALUES (?, ?, ?)', (item, quantity, price))
        conn.commit()

def view():
    with psycopg2.connect('lite.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM STORE')
        return cur.fetchall()

"""
insert('Coffee Cup', 5, 22.2)
print(view())
"""
