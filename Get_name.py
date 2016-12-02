import wx
import mysql.connector
from mysql.connector import errorcode

def name_conn1(T_ID,match_ID,Name):
	try :
		
		con = mysql.connector.connect(user ='root',password = 'root@1234',host ='127.0.0.1',database ='Scoreboard' )
		cursor = con.cursor()
		cursor.execute("USE Scoreboard")
		cursor.execute("Select Name,ID from Scoreboard."+Name+" where Team_ID ='%d' AND Match_ID = '%d' AND Status = '%d'"%(T_ID,match_ID,0))
		data1 = cursor.fetchall()
		for row in data1 :
			print(row[0],row[1])
		return data1
		
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something went wrong")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database doesnt exist")
		else:
			print(err)
	else:	
		print("Returning the names and id's")
		con.commit()
