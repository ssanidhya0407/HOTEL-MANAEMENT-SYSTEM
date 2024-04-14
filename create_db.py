import sqlite3
def create_db():
    con=sqlite3.connect(database=r'rms.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(empID INTEGER PRIMARY KEY AUTOINCREMENT,name text,DOJ text,salary text,email text,pswd text,gender text,dsgntn text,branch text)")
    con.commit()


create_db()

