import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db") #connecting to the database
    cur = conn.cursor() #creating a cursor

    cur.execute("CREATE TABLE IF NOT EXISTS store(item VARCHAR(255), quantity INT, price REAL)")

    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = sqlite3.connect("lite.db") #connecting to the database
    cur = conn.cursor() #creating a cursor
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

insert("Frooti",10,100)

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows= cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store WHERE item = ?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ?, price =? WHERE item = ?",(quantity,price,item))
    conn.commit()
    conn.close()



update(12,40,"Munch")

print(view())
#delete("Munch")
