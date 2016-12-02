import wx
import mysql.connector
from mysql.connector import errorcode

def conn(list) :
	try :
		
		con = mysql.connector.connect(user ='root',password = 'root@1234',host ='127.0.0.1',database ='Scoreboard' )
		cursor = con.cursor()
		cursor.execute("USE Scoreboard")
		cursor.execute(list)
		con.commit()
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("something went wrong")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database doesnt exist")
		else:
			print(err)
	else:	
		
		print("Passed query executed..!!")