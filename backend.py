import sqlite3

def connect():
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title text , number integer)")
	conn.commit()
	conn.close

def insert(title,number):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO book VALUES (NULL,?,?)",(title,number))
	conn.commit()
	conn.close
	
def view ():
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM book")
	rows=cur.fetchall()
	conn.close
	return rows
	
def delete(id):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM book WHERE id=?",(id,))
	conn.commit()
	conn.close
	
def update(id,title,number):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("UPDATE book SET title=?,number=? WHERE id=?",(title,number,id))
	conn.commit()
	conn.close	
connect()
#insert("me",925)
#insert("yy",900)
#delete(1)
update (3,"kkk",222)
print view()

	
	
	
	
	