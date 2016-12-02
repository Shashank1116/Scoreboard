import wx
import mysql.connector
from mysql.connector import errorcode

def it_conn1(mylist,T_ID,Match_ID,Name) :
	try :
		
		con = mysql.connector.connect(user ='root',password = 'root@1234',host ='127.0.0.1',database ='Scoreboard' )
		cursor = con.cursor()
		cursor.execute("USE Scoreboard")
		for i in mylist:
			cursor.execute("Select Name from Scoreboard.Bat_car where ID ='%d'"%(int(i)))
			data = cursor.fetchall()
			for row in data :
				name = str(row[0])
				cursor.execute("Insert into Scoreboard."+Name+"(ID,Name,Team_ID,Match_ID,Status) values ('%d','%s','%d','%d','%d')"%(int(i),name,T_ID,Match_ID,0))
			
		
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something went wrong")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database doesnt exist")
		else:
			print(err)
	else:	
		print("names inserted into the passed table...")
		con.commit()
