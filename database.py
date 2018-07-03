#Import packages
import sqlite3

'''
The class conn has two methods.For importing seperate methods use the
folling syntax: conn.databaseConnection.
databaseConnection creates the table "login" if it does't exists. And inserts the value 
of username and password.
checkUserPassword checks the username and password entered by the user and returns true if it matches.
'''
class conn:
	'''Creates the table sctructure to store user login. '''
	def databaseConnection():
	    global connection, cursor
	    connection = sqlite3.connect("database.db")
	    cursor = connection.cursor()
	    cursor.execute("CREATE TABLE IF NOT EXISTS `login` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")       
	    cursor.execute("SELECT * FROM `login` WHERE `username` = 'admin' AND `password` = 'admin'")
	    if cursor.fetchone() is None:
	        cursor.execute("INSERT INTO `login` (username, password) VALUES('admin', 'admin')")
	        connection.commit()

	def checkUserPassword(username,password):
		
		#create cursor to fetch records and create connection
		global connection, cursor
		connection = sqlite3.connect("database.db")
		cursor = connection.cursor()
		auth = cursor.execute("SELECT `mem_id` FROM `login` WHERE `username` = ? AND `password` = ?",(username,password))
		
		if cursor.fetchone() is None:
			return False
		else:
			return True
			cursor.close()
			connection.close()
