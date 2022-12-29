import sqlite3
from hashids import Hashids
from datetime import datetime
from string import ascii_lowercase , digits

con = sqlite3.connect("url_database.db")
cur = con.cursor()

def add_link(link):
    

    con = sqlite3.connect("url_database.db")
    cur = con.cursor()
    try:
        alphabet = ascii_lowercase + digits
        hashids = Hashids(salt="this line is helpful in encoding" , alphabet=alphabet)
        hash_link = hashids.encode(int(datetime.today().timestamp()))
        with con:
            cur.execute("""INSERT INTO link VALUES ( ?, ?)""", (link,hash_link))
        
        return hash_link 
    except:
        with con :
            res = cur.execute("""SELECT output_link FROM link WHERE input_link = ?""",(link,))
        
        return res.fetchone()[0]

def retrieve_link(code):
    con = sqlite3.connect("url_database.db")
    cur = con.cursor()

    with con :
        res = cur.execute("""SELECT input_link FROM link WHERE output_link = ?""" , (code,))
    return res.fetchone()[0]