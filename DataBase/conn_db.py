import sqlite3
from datetime import datetime as dt


def to_connect():
    conn = sqlite3.connect('DataBase/bikes.db')
    curr = conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS bike (id INTEGER PRIMARY KEY ,name TEXT,number_of_bikes INTEGER,rented_time TEXT,return_time TEXT,cost INTEGER) ")
    conn.commit()
    conn.close()


def to_insert(name, number_of_bikes, rented_time):
    cost = 0
    return_time = 'Not Returned'
    conn = sqlite3.connect('DataBase/bikes.db')
    curr = conn.cursor()
    curr.execute("INSERT INTO bike VALUES(null,?,?,?,?,?)",
                (name, number_of_bikes, rented_time, return_time, cost))
    conn.commit()
    conn.close()
    print('Value added')


def to_view():
    conn = sqlite3.connect('DataBase/bikes.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bike")
    row = cur.fetchall()
    conn.close()
    return row


def to_search(name, id):
    conn = sqlite3.connect('DataBase/bikes.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bike WHERE name=? AND id=?", (name, id))
    row = cur.fetchall()
    conn.close()
    return row

def to_search_name(name):
    conn = sqlite3.connect('DataBase/bikes.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bike WHERE name=?", (name,))
    row = cur.fetchall()
    conn.close()
    return row

def to_search_id_in_db(name="", number_of_bikes=""):
    conn = sqlite3.connect('DataBase/bikes.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bike WHERE name=? AND number_of_bikes=?",
                (name, number_of_bikes))
    row = cur.fetchall()
    conn.close()
    return row


def to_update_return_time(id, return_time):
    conn = sqlite3.connect('DataBase/bikes.db')
    cur = conn.cursor()
    cur.execute("UPDATE bike SET return_time=? WHERE id=?", (return_time, id))
    conn.commit()
    conn.close()


def to_update_cost(id, cost):
    conn = sqlite3.connect('DataBase/bikes.db')
    cur = conn.cursor()
    cur.execute("UPDATE bike SET cost=? WHERE id=?", (cost, id))
    conn.commit()
    conn.close()


to_connect()
# print(to_search_id_in_db('ali',234)[0][0])
# print(to_search_name('haris')[0][1])
# dublicate_name = to_search_name('harisdf')[0][1]
# print(dublicate_name)