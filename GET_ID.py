import wx
import mysql.connector
from mysql.connector import errorcode

def get_ID(T_Name) :
	try :
		
		con = mysql.connector.connect(user ='root',password = 'root@1234',host ='127.0.0.1',database ='Scoreboard' )
		cursor = con.cursor()
		cursor.execute("USE Scoreboard")
		cursor.execute("Select Team_ID from Scoreboard.Team where T_name = '%s'"%(T_Name))
		data = cursor.fetchall()
		newlist = [];
		for row in data:
			newlist.append(row[0])
		
		t_ID = newlist[0]	 
		return t_ID

	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("something went wrong")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database doesnt exist")
		else:
			print(err)
	else:	
		print("Here have the name...")
		con.commit()