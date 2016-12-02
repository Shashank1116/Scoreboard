import wx
from wxpythn import conn
from database import conn1
import wx.grid as gridlib
from iterative_dat import it_conn1
from GET_ID import get_ID
from random import randint
from Get_name import name_conn1
# Parent Frame class
class MyFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self, None, wx.ID_ANY,size = (500,500))
		 
		self.n_play = wx.Button(self,1,'New Player',(400,350))
		self.n_team = wx.Button(self,2,'New Team',(400,400))
		self.play = wx.Button(self,9,'Play Match',(400,450))
		self.Bind(wx.EVT_BUTTON,self.teams,id=9)
		self.Bind(wx.EVT_BUTTON,self.teams,id=1)
		self.Bind(wx.EVT_BUTTON,self.newteam,id=2)
		self.Home = wx.Button(self,12,'Home',(0,0))
		self.Bind(wx.EVT_BUTTON,self.New,id=12)
		self.SetBackgroundColour('Green')
		self.playing_list1 = [];	
		self.playing_list2 = [];
		self.Show()
		self.check = 0
		self.count = 0
		self.sec_in = 0
		self.agla = 0
		self.count_2 =0
	#Home Button destroys the self object		
	def New(self,event):
		self.Destroy()
		next_frame = MyFrame(None,'Scoreboard')
	# ScoreBoard
	def score_b(self,event):
		self.Hide_all()
		self.show_team1.Destroy()
		self.show_team2.Destroy()
		self.Go.Destroy()
		self.static_Bat.Destroy()
		self.static_Bowl.Destroy()
		self.set_itb.Destroy()
		if self.agla == 45:
			temp = self.team1
			self.team1 = self.team2
			self.team2 = temp
			print("working")
				
		query = "Select ID,Name from c_bat where Team_ID = '%d' AND Match_ID = '%d' AND Status='%d'"%(self.team1,self.match_ID,1)
		query2= "Select ID,Name from C_bow where Team_ID ='%d' AND Match_ID = '%d' AND Status = '%d'"%(self.team2,self.match_ID,1)
		data = conn1(query)
		data2 = conn1(query2)
		print('working')
		
		self.textbox = wx.StaticText(self,label='Batting',pos= (50,30))
		self.score = wx.ListCtrl(self,20,(50,50),wx.Size(400,100),style = wx.LC_REPORT)
		self.score.InsertColumn(0,'ID',width=50)
		self.score.InsertColumn(1,'Name',width=100)
		self.score.InsertColumn(2,'Runs',width=50)
		self.score.InsertColumn(3,'Balls',width=50)
		self.score.InsertColumn(4,"1's",width=40)
		self.score.InsertColumn(5,"2's",width=40)
		self.score.InsertColumn(6,"3's",width=40)
		self.score.InsertColumn(7,"4's",width=40)
		self.score.InsertColumn(8,"6's",width=40)
		self.score.InsertColumn(9,'SR',width=40)
		self.textbox2 = wx.StaticText(self,label='Bowling',pos= (50,180))
		self.bowl =wx.ListCtrl(self,28,(50,200),wx.Size(400,50),style = wx.LC_REPORT)
		self.bowl.InsertColumn(0,'ID',width =50)
		self.bowl.InsertColumn(1,'Name',width =100)
		self.bowl.InsertColumn(2,'1',width =40)
		self.bowl.InsertColumn(3,'2',width =40)
		self.bowl.InsertColumn(4,'3',width =40)
		self.bowl.InsertColumn(5,'4',width =40)
		self.bowl.InsertColumn(6,'5',width =40)
		self.bowl.InsertColumn(7,'6',width =40)
		
		index = 0
		for row in data:
			print("Works !!")
			self.score.InsertStringItem(index,str(row[0]))
			self.score.SetStringItem(index,1,str(row[1]))
			print(row[0],row[1])
			if index == 0:
				self.ID_1 = row[0]
			else :
				self.ID_2 = row[0]	
			index = index+1	
			
		index_2 = 0
		for row in data2:
			print("Works!!")
			self.bowl.InsertStringItem(index_2,str(row[0]))	
			self.bowl_ID = int(row[0])
			self.bowl.SetStringItem(index_2,1,str(row[1]))
			print(row[0],row[1])
		self.one_1 =0
		self.one_2 =0
		self.balls_1 = 0
		self.balls_2 =0
		self.overs = 0
		self.over_count = 0
		self.one = wx.Button(self,15,'1',(0,300))
		self.Bind(wx.EVT_BUTTON,self.add_one,id=15)
		self.two_1 =0
		self.two_2 =0
		self.two = wx.Button(self,16,'2',(0,350))
		self.Bind(wx.EVT_BUTTON,self.add_two,id=16)
		self.three_1 =0
		self.three_2 =0
		self.three = wx.Button(self,17,'3',(100,300))
		self.Bind(wx.EVT_BUTTON,self.add_three,id=17)
		self.four_1 =0
		self.four_2 =0
		self.four= wx.Button(self,18,'4',(100,350))
		self.Bind(wx.EVT_BUTTON,self.add_four,id=18)
		self.six_1 =0
		self.six_2 =0
		self.six = wx.Button(self,19,'6',(200,300))
		self.Bind(wx.EVT_BUTTON,self.add_six,id=19)
		self.score.Bind(wx.EVT_LIST_ITEM_SELECTED,self.change)
		self.run_1 = 0 
		self.run_2 = 0
		self.t_runs = 0
		self.count = 1
		self.wicket = wx.Button(self,30,'Wicket',(200,350))
		self.wickets = 0
		self.tot_wickets = 0
		self.runs = 0
		self.wicket.Bind(wx.EVT_BUTTON,self.wicket_func)
		self.line1 = wx.StaticLine(self,pos =(0,440),size=(500,10)) 	
		self.run_bar = wx.StaticText(self,label = 'Runs:',pos = (0,450))
		self.run_bar1 = wx.StaticText(self,label =str(self.t_runs),pos = (50,450))
		self.over_bar = wx.StaticText(self,label ='Overs',pos = (400,450))
		self.over_bar1 = wx.StaticText(self,label = str(self.overs),pos = (450,450))
		
		
			
		
	def total(self):
		self.run_bar1.SetLabel(str(self.t_runs)) 
	def new_player(self):
		self.score.Hide()
		self.textbox.Hide()
		self.textbox2.Hide()
		query2 = "Select ID,Name from Scoreboard.c_bat where Match_ID ='%d' And Team_ID = '%d' and Status ='%d'"%(self.match_ID,self.team1,0)
		data = conn1(query2)
		self.select = wx.ListCtrl(self,32,(100,50),wx.Size(100,100),style = wx.LC_REPORT)
		self.select.InsertColumn(0,'ID',width=50)
		self.select.InsertColumn(1,'Name',width =50)
		index_c = 0
		for row in data:
			self.select.InsertStringItem(index_c,str(row[0]))
			self.select.SetStringItem(index_c,1,str(row[1]))	
			index_c = index_c +1	
		self.select.Bind(wx.EVT_LIST_ITEM_SELECTED,self.ADD_new)	
	def ADD_new(self,event):
		self.textbox.Show()
		self.textbox2.Show()
		self.select.Hide()
		self.score.Show()
		row = self.select.GetFirstSelected()
		play_ID = self.select.GetItemText(row,0)
		if self.index == 0:
			self.ID_1 = int(play_ID)
		else :
			self.ID_2 = int(play_ID)	
		play_Name = self.select.GetItemText(row,1)
		self.score.SetStringItem(self.index,0,str(play_ID))
		self.score.SetStringItem(self.index,1,str(play_Name))
		self.score.SetStringItem(self.index,2,str(0))
		self.score.SetStringItem(self.index,3,str(0))
		self.score.SetStringItem(self.index,4,str(0))
		self.score.SetStringItem(self.index,5,str(0))
		self.score.SetStringItem(self.index,6,str(0))
		self.score.SetStringItem(self.index,7,str(0))
		self.score.SetStringItem(self.index,8,str(0))
		self.score.SetStringItem(self.index,9,str(0))
		
	def inc_overs(self):
		if self.overs < int(self.mtc):
			if self.count <= 6:
				self.over_count = int(self.over_count) + 1
			else :
				self.over_count = 0
				self.overs = int(self.overs) + 1
			print("%d.%d"%(self.overs,self.over_count))
			self.over_bar1.SetLabel("%d.%d"%(self.overs,self.over_count))	
		else:
			self.AskUser("Innings Finished")	
			if self.tossw == 1:
				self.tossw = 0
			else :
				self.tossw = 1
			self.score.Destroy()
			self.bowl.Destroy()
			self.textbox.Destroy()
			self.textbox2.Destroy()	
			self.one.Destroy()
			self.two.Destroy()
			self.three.Destroy()
			self.four.Destroy()
			self.six.Destroy()
			self.wicket.Destroy()
			self.count = 0
			self.count_2 =0
			self.t_runs = 0
			self.tot_wickets = 0
			if self.sec_in == 0:
				self.n_i = wx.Button(self,45,'Next Innings',(400,10))	
				self.n_i.Bind(wx.EVT_BUTTON,self.bat_o_ball,id = 45)
				self.sec_in =1
				
			else :
				self.Stats = wx.Button(self,46,'Check Stats',(400,100))
				self.Bind(wx.EVT_BUTTON,self.Stats,id = 46)		
			
	def first_bat(self):
		self.run_1 =0
		self.one_1 =0
		self.two_1 = 0	
		self.balls_1=0
		self.three_1 =0
		self.four_1 = 0
		self.six_1 = 0
	
	def sec_bat(self):
		self.run_2 =0
		self.one_2 =0
		self.two_2 = 0	
		self.balls_2=0
		self.three_2 =0
		self.four_2 = 0
		self.six_2 = 0	
		
	def wicket_func(self,event):
		self.change_ball()
		self.wickets = self.wickets + 1
		self.tot_wickets = self.tot_wickets + 1
		print(self.tot_wickets)
		if self.index == 0:
			query = "Update Scoreboard.c_bat SET Status ='%d',Runs ='%d',balls='%d',ones ='%d',twos = '%d',threes = '%d', fours = '%d', sixes = '%d' where ID = '%d' And Match_ID = '%d'"%(2,int(self.run_1),int(self.balls_1),int(self.one_1),int(self.two_1),int(self.three_1),int(self.four_1),int(self.six_1),int(self.ID_1),int(self.match_ID))
			conn(query)
			self.first_bat()
			self.new_player()
		else:
			query = "Update Scoreboard.c_bat SET Status ='%d',Runs ='%d',balls='%d',ones ='%d',twos = '%d',threes = '%d', fours = '%d', sixes = '%d' where ID = '%d' And Match_ID = '%d'"%(2,int(self.run_2),int(self.balls_2),int(self.one_2),int(self.two_2),int(self.three_2),int(self.four_2),int(self.six_2),int(self.ID_2),int(self.match_ID))	
			conn(query)
			self.sec_bat()
			self.new_player()
		self.bowl.SetStringItem(0,self.count,str('W'))
		self.inc_overs()	
	def change_ball(self):
		self.count = self.count +1		
		if int(self.count) >= 8:
			self.get_player()
			self.count = 1
			return 0	
		else :
			return 1	
	def get_SR(self,run,balls):
		runs = run * 100
		runs_c = runs/balls
		SR = float(runs_c)
		return SR 
	
	def get_player(self):
		query = "Update Scoreboard.c_bow SET Runs = Runs +'%d',Overs = Overs + '%d',Wickets = Wickets +'%d' where ID = '%d' AND Team_ID = '%d' AND Match_ID = '%d'"%(self.runs,1,self.wickets,self.bowl_ID,self.team2,self.match_ID)			
		conn(query)
		self.runs = 0
		self.wickets = 0 
		query2 = "Select ID,Name from scoreboard.c_bow where Match_ID='%d' AND Team_ID ='%d'"%(self.match_ID,self.team2)
		data = conn1(query2)
		self.select_2 = wx.ListCtrl(self,32,(350,350),wx.Size(100,100),style = wx.LC_REPORT)
		self.select_2.InsertColumn(0,'ID',width=50)
		self.select_2.InsertColumn(1,'Name',width =50)
		index_c = 0
		for row in data:
			if int(row[0]) != self.bowl_ID:
				self.select_2.InsertStringItem(index_c,str(row[0]))
				self.select_2.SetStringItem(index_c,1,str(row[1]))	
				index_c = index_c +1	
		self.select_2.Bind(wx.EVT_LIST_ITEM_SELECTED,self.Get_bowl)
		self.bowl.SetStringItem(0,2,str(0))
		self.bowl.SetStringItem(0,3,str(0))
		self.bowl.SetStringItem(0,4,str(0))
		self.bowl.SetStringItem(0,5,str(0))
		self.bowl.SetStringItem(0,6,str(0))
		self.bowl.SetStringItem(0,7,str(0))
	
	def Get_bowl(self,event):
		self.select_2.Hide()
		row = self.select_2.GetFirstSelected()
		play_ID = self.select_2.GetItemText(row,0)
		play_name = self.select_2.GetItemText(row,1)
		self.bowl.SetStringItem(0,0,str(play_ID))
		self.bowl.SetStringItem(0,1,str(play_name))
		self.bowl_ID = int(play_ID) 	
	def change(self,event):
		ch = self.score.GetFirstSelected()	
		self.index = ch
		print(self.index)
	
	def add_one(self,event):
		flag = self.change_ball()
		try:
			if flag != 0 :
				if self.index == 0:
					self.one_1 = self.one_1 + 1
					self.balls_1 = self.balls_1 +1
					self.score.SetStringItem(self.index,3,str(self.balls_1))
					self.score.SetStringItem(self.index,4,str(self.one_1))	
					self.run_1 = self.one_1 + (2*self.two_1) +(3*self.three_1) + (4*self.four_1) + (6*self.six_1)
					SR = self.get_SR(self.run_1,self.balls_1)
					self.score.SetStringItem(self.index,9,str(SR))
					self.score.SetStringItem(self.index,2,str(self.run_1))
					self.index = 1
				else:
					self.balls_2 = self.balls_2 +1
					self.score.SetStringItem(self.index,3,str(self.balls_2))
					self.one_2 = self.one_2 + 1	
					self.score.SetStringItem(self.index,4,str(self.one_2))	
					self.run_2 = self.one_2+ (2*self.two_2) +(3*self.three_2) + (4*self.four_2) + (6*self.six_2)
					SR = self.get_SR(self.run_2,self.balls_2)
					self.score.SetStringItem(self.index,9,str(SR))
					self.score.SetStringItem(self.index,2,str(self.run_2))
					self.index =0
				self.runs = self.runs + 1
				self.t_runs = self.t_runs + 1	
				self.inc_overs()
				self.bowl.SetStringItem(0,self.count,str(1))
				self.total()
		except:
			print("I don't really expect to see this!!")	
	def add_two(self,event):
		flag = self.change_ball()
		try :
			if flag != 0 :
				if self.index == 0:
					self.two_1 = self.two_1 + 1
					self.balls_1 = self.balls_1 +1
					self.score.SetStringItem(self.index,3,str(self.balls_1))
					self.score.SetStringItem(self.index,5,str(self.two_1))
					self.run_1 = self.one_1 + (2*self.two_1) +(3*self.three_1) + (4*self.four_1) + (6*self.six_1)
					SR = self.get_SR(self.run_1,self.balls_1)
					self.score.SetStringItem(self.index,9,str(SR))
					self.score.SetStringItem(self.index,2,str(self.run_1))	
				else:
					self.two_2 = self.two_2 + 1	
					self.balls_2 = self.balls_2 +1
					self.score.SetStringItem(self.index,3,str(self.balls_2))
					self.score.SetStringItem(self.index,5,str(self.two_2))
					self.run_2 = self.one_2+ (2*self.two_2) +(3*self.three_2) + (4*self.four_2) + (6*self.six_2)
					SR = self.get_SR(self.run_2,self.balls_2)
					self.score.SetStringItem(self.index,9,str(SR))
					self.score.SetStringItem(self.index,2,str(self.run_2))	
				self.runs = self.runs + 2
				self.t_runs = self.t_runs + 2
				self.inc_overs()	
				self.bowl.SetStringItem(0,self.count,str(2))
				self.total()
		except :
			print("Never wanna see this")
	def add_three(self,event):
		flag =self.change_ball()
		try:
			if flag != 0 :
				if self.index == 0:
					self.three_1 = self.three_1 + 1
					self.balls_1 = self.balls_1 +1
					self.score.SetStringItem(self.index,3,str(self.balls_1))
					self.score.SetStringItem(self.index,6,str(self.three_1))	
					self.run_1 = self.one_1 + (2*self.two_1) +(3*self.three_1) + (4*self.four_1) + (6*self.six_1)
					SR = self.get_SR(self.run_1,self.balls_1)
					self.score.SetStringItem(self.index,9,str(SR))
					self.score.SetStringItem(self.index,2,str(self.run_1))
					self.index = 1
				else:
					self.three_2 = self.three_2 + 1	
					self.balls_2 = self.balls_2 +1
					self.score.SetStringItem(self.index,3,str(self.balls_2))
					self.score.SetStringItem(self.index,6,str(self.three_2))	
					self.run_2 = self.one_2+ (2*self.two_2) +(3*self.three_2) + (4*self.four_2) + (6*self.six_2)
					SR = self.get_SR(self.run_2,self.balls_2)
					self.score.SetStringItem(self.index,9,str(SR))
					self.score.SetStringItem(self.index,2,str(self.run_2))
					self.index = 0
				self.runs = self.runs + 3	
				self.t_runs = self.t_runs + 3
				self.inc_overs()
				self.bowl.SetStringItem(0,self.count,str(3))
				self.total()
		except :
			print("None")
	def add_four(self,event):
		flag =self.change_ball()
		try:
			if flag != 0:
				if self.index == 0:
					self.four_1 = self.four_1 + 1
					self.balls_1 = self.balls_1 +1
					self.score.SetStringItem(self.index,3,str(self.balls_1))
					self.score.SetStringItem(self.index,7,str(self.four_1))	
					self.run_1 = self.one_1 + (2*self.two_1) +(3*self.three_1) + (4*self.four_1) + (6*self.six_1)
					SR = self.get_SR(self.run_1,self.balls_1)
					self.score.SetStringItem(self.index,9,str(SR))
					self.score.SetStringItem(self.index,2,str(self.run_1))
				else:
					self.four_2 = self.four_2 + 1	
					self.balls_2 = self.balls_2 +1
					self.score.SetStringItem(self.index,3,str(self.balls_2))
					self.score.SetStringItem(self.index,7,str(self.four_2))	
					self.run_2 = self.one_2+ (2*self.two_2) +(3*self.three_2) + (4*self.four_2) + (6*self.six_2)
					SR = self.get_SR(self.run_2,self.balls_2)
					self.score.SetStringItem(self.index,9,str(SR))
					self.score.SetStringItem(self.index,2,str(self.run_2))
				self.runs = self.runs + 4
				self.t_runs = self.t_runs + 4
				self.inc_overs()
				self.bowl.SetStringItem(0,self.count,str(4))	
				self.total()
		except:
			print("Never want this")
	def add_six(self,event):
		flag = self.change_ball()
		try:
			if flag != 0 :
				if self.index == 0:
					self.six_1 = self.six_1 + 1
					self.balls_1 = self.balls_1 +1
					self.score.SetStringItem(self.index,3,str(self.balls_1))
					self.score.SetStringItem(self.index,8,str(self.six_1))
					self.run_1 = self.one_1 + (2*self.two_1) +(3*self.three_1) + (4*self.four_1) + (6*self.six_1)
					SR = self.get_SR(self.run_1,self.balls_1)
					self.score.SetStringItem(self.index,9,str(SR))
					self.score.SetStringItem(self.index,2,str(self.run_1))	
				else:
					self.six_2 = self.six_2 + 1	
					self.balls_2 = self.balls_2 +1
					self.score.SetStringItem(self.index,3,str(self.balls_2))
					self.score.SetStringItem(self.index,8,str(self.six_2))
					self.run_2 = self.one_2+ (2*self.two_2) +(3*self.three_2) + (4*self.four_2) + (6*self.six_2)
					SR = self.get_SR(self.run_2,self.balls_2)
					self.score.SetStringItem(self.index,9,str(SR))
					self.score.SetStringItem(self.index,2,str(self.run_2))	
				self.runs = self.runs + 6
				self.t_runs = self.t_runs + 6
				self.inc_overs()
				self.bowl.SetStringItem(0,self.count,str(6))
				self.total()
		except:
			print("Nahi chahiye")		
	def Hide_all(self):
		self.n_play.Hide()
		self.n_team.Hide()
		self.play.Hide()
			
	# event function to add a new player called by select button in select function
	def newplay(self,event):     
		print("New Player Creating....")
		self.Hide_all()
		self.team_list.Hide()
		self.static_s.Hide()
		self.select.Hide()
		
		self.name = wx.TextCtrl(self,1,pos = (50,50),size = (100,20))
		self.st = wx.StaticText(self,label = 'Name',pos = (0,50))
		self.ID = wx.TextCtrl(self,3,pos = (50,110),size = (100,20))
		self.st2 = wx.StaticText(self,label = 'ID',pos = (0,110))
		self.button3 = wx.Button(self,3,'Add To Squad',(200,400)) 
		self.Bind(wx.EVT_BUTTON,self.addp,id=3)
	# function to add a new team called by New Team button in parent frame
	def newteam(self,event):
		self.Hide_all()
		print("New Team Creating....")	
		self.name = wx.TextCtrl(self,1,pos = (100,50),size = (100,20))
		self.st = wx.StaticText(self,label = 'Team Name',pos = (0,50))
		self.team = wx.TextCtrl(self,2,pos = (100,80),size = (100,20))
		self.st1 = wx.StaticText(self,label = 'Team ID',pos = (0,80))
		self.button3 = wx.Button(self,4,'Add Team',(200,400)) 
		self.Bind(wx.EVT_BUTTON,self.addt,id=4)
	# function to a new player calling database class in database.py
	def addp(self,event):
		name1 = self.name.GetValue()
		ID1 = int(self.ID.GetValue())
		list = "INSERT INTO Scoreboard.Bat_car(Name,ID,Team_ID) VALUES('%s','%d','%s')"%(name1,ID1,self.T_ID) 
		conn(list)			
	# Adding team on clicking Add Team	
	def addt(self,event):
		tname = self.name.GetValue()
		tid = int(self.team.GetValue())
		list = "INSERT INTO Scoreboard.Team(T_name,Team_ID) VALUES ('%s','%d')"%(tname,tid)
		conn(list)	
	# Shows a list of teams
	def teams(self,event):
		self.Hide_all()
		self.static_s = wx.StaticText(self,label = 'Click to select Your team',pos =(100,50))
		# add_o_play is an integer for checking if the team list is called to add or play
		self.add_o_play = event.GetId()	
		# team1_o_2 checks if the function is called for first team or second
		self.team1_o_2 = event.GetId()
		if self.team1_o_2 == 11:
		#hiding the previous widgets
			self.player_list.Hide()
			self.next_team.Hide()
			self.team_list.Hide()
		
		list = "SELECT T_name from Scoreboard.Team"
		data = conn1(list)
		mylist = [];
		for row in data :
			mylist.append(str(row[0]))
		self.team_list = wx.ListBox(self,7,(100,100),wx.Size(200,200),mylist)
		self.Bind(wx.EVT_LISTBOX,self.select,id=7)	
	# Gets the list of IDs of the teams
	def select(self,event):
		t = self.team_list.GetSelection()		
		self.team_name = self.team_list.GetString(t)
		query = "Select Team_ID from Scoreboard.Team where T_Name='%s'"%(self.team_name) 
		data = conn1(query)
		for row in data :
			self.T_ID = row[0]
		if self.add_o_play == 1	: 
	 		self.select = wx.Button(self,8,'Select',(200,400))
	 		self.Bind(wx.EVT_BUTTON,self.newplay,id=8)
	 	else :
	 		self.proceed = wx.Button(self,10,'Proceed',(200,400))
	 		self.Bind(wx.EVT_BUTTON,self.selectplay,id=10)
	#calls the list_box function to show the list of players from the team		
	def selectplay(self,event):
		self.static_s.Hide()
		self.team_list.Hide()
		self.proceed.Destroy()
	 	query = "Select Name,ID from Scoreboard.Bat_car where Team_ID = '%s'"%(self.T_ID) 
	 	data = conn1(query) 
	 	print(data)
		self.list_box(data)
	 	self.next_team = wx.Button(self,11,'Next Team',(200,400))
	 	self.Bind(wx.EVT_BUTTON,self.teams,id=11)
	 	if self.team1_o_2 == 9 :
	 		self.Bind(wx.EVT_LISTBOX,self.first_team,id=7)
	 	elif self.team1_o_2 == 11 :
	 		self.Bind(wx.EVT_LISTBOX,self.second_team,id =7)	
	def toss(self):
		self.toss_t = wx.StaticText(self,label =' Team I Choose Head or Tails',pos = (100,50))
		self.heads = wx.Button(self,35,'Heads',(100,150))
		self.tails = wx.Button(self,36,'Tails',(300,150))
		self.Bind(wx.EVT_BUTTON,self.decide,id =35)
		self.Bind(wx.EVT_BUTTON,self.decide,id =36)
		
		
	def decide(self,event):
		self.toss_t.Destroy()
		self.heads.Destroy()
		self.tails.Destroy()
		bin = int(randint(0,11))
		print(bin)
		if bin % 2 == 0 :
			check = 35	
		else :	
			check = 36
		Id = event.GetId()
		print(check)
		print(Id)	
		if int(check) == int(Id) :
			self.tossw = 0
			self.wait()
			print(self.tossw)
		else :
			self.tossw = 0
			self.wait()
			print(self.tossw)
	def wait(self):
		if self.tossw == 0:
			self.ann=wx.StaticText(self,label = 'Team I won the toss',pos =(100,50))
		else :
			self.ann=wx.StaticText(self,label = 'Team II won the toss',pos = (100,50))
		self.startnow = wx.Button(self,39,'Proceed',(300,300))
		self.Bind(wx.EVT_BUTTON,self.no_o_overs,id =39)
							
	def match_up(self,event):
		self.Done.Hide()
		self.player_list.Hide()
		print("Setting up match...")
		self.match_ID = int(randint(0,1000))
		print(self.match_ID)
		self.toss()
	def bat_o_ball(self,event):	
		self.match_len.Hide()
		self.match_type.Hide()
		if event.GetId() == 45:
			self.agla = 45
			self.n_i.Destroy()
		self.a = "c_bat"
		self.b="c_bow"	
		if self.tossw == 0:
			print("First Team")
			it_conn1(self.playing_list1,self.team1,self.match_ID,self.a)
			it_conn1(self.playing_list2,self.team2,self.match_ID,self.b)
			data1 = name_conn1(self.team1,self.match_ID,self.a)
			data2 = name_conn1(self.team2,self.match_ID,self.b)
			self.static_Bat = wx.StaticText(self,label='Select Batting pair',pos = (100,50))
			self.show_team1 = wx.ListCtrl(self,23,(100,100),wx.Size(150,200),style = wx.LC_REPORT)
			self.show_team1.InsertColumn(0,'Batting Order',width = 100)
			self.show_team1.InsertColumn(1,'ID',width=50)
			self.insert_listbox(data1,self.show_team1)
			self.show_team1.Bind(wx.EVT_LIST_ITEM_SELECTED,self.get_values1,id=23)
			self.static_Bowl = wx.StaticText(self,label='Select Bowler',pos = (300,50))
			self.show_team2 = wx.ListCtrl(self,24,(300,100),wx.Size(150,200),style = wx.LC_REPORT)
			self.show_team2.InsertColumn(0,'Bowling',width =100) 
			self.show_team2.InsertColumn(1,'ID',width=50)
			self.insert_listbox(data2,self.show_team2)
			self.show_team2.Bind(wx.EVT_LIST_ITEM_SELECTED,self.get_values2,id=24)
			self.Go = wx.Button(self,27,'Go',(200,400))
			self.Bind(wx.EVT_BUTTON,self.score_b,id=27)
		elif self.tossw== 1:
			print("Second Team")
			temp = self.team1
			self.team1 = self.team2
			self.team2 = temp
			it_conn1(self.playing_list1,self.team1,self.match_ID,self.a)
			it_conn1(self.playing_list2,self.team2,self.match_ID,self.b)
			data1 = name_conn1(self.team1,self.match_ID,self.a)
			data2 = name_conn1(self.team2,self.match_ID,self.b)		
			self.static_Bat = wx.StaticText(self,label='Select Batting pair',pos = (100,50))
			self.show_team1 = wx.ListCtrl(self,23,(100,100),wx.Size(150,200),style = wx.LC_REPORT)
			self.show_team1.InsertColumn(0,'Batting Order',width = 100)
			self.show_team1.InsertColumn(1,'ID',width=50)
			self.insert_listbox(data1,self.show_team1)
			self.show_team1.Bind(wx.EVT_LIST_ITEM_SELECTED,self.get_values1,id=23)
			self.static_Bowl = wx.StaticText(self,label='Select Bowler',pos = (300,50))
			self.show_team2 = wx.ListCtrl(self,24,(300,100),wx.Size(150,200),style = wx.LC_REPORT)
			self.show_team2.InsertColumn(0,'Bowling',width =100) 
			self.show_team2.InsertColumn(1,'ID',width=50)
			self.insert_listbox(data2,self.show_team2)
			self.show_team2.Bind(wx.EVT_LIST_ITEM_SELECTED,self.get_values2,id=24)
			self.Go = wx.Button(self,27,'Go',(200,400))
			self.Bind(wx.EVT_BUTTON,self.score_b,id=27)
		
	def no_o_overs(self,event):
		self.ann.Destroy()
		self.startnow.Destroy()
		self.match_len = wx.StaticText(self,label = "Select Match Type",pos = (100,50))
		self.match_type= wx.ListCtrl(self,40,(100,100),wx.Size(200,200),style = wx.LC_REPORT)
		self.match_type.InsertColumn(0,'Match Type',width = 50)
		self.match_type.InsertColumn(1,'Overs',width = 50)
		self.match_type.InsertStringItem(0,'5 Overs')
		self.match_type.SetStringItem(0,1,'5')
		self.match_type.InsertStringItem(1,'T10')
		self.match_type.SetStringItem(1,1,'10')
		self.match_type.InsertStringItem(2,'T20')
		self.match_type.SetStringItem(2,1,'20')
		self.match_type.InsertStringItem(3,'One Day')
		self.match_type.SetStringItem(3,1,'50')
		self.match_type.Bind(wx.EVT_LIST_ITEM_SELECTED,self.set_it)
		 
	def set_it(self,event):
		rows = self.match_type.GetFirstSelected()
		play = int(self.match_type.GetItemText(rows,col=1))
		print(play)
		self.mtc = play
		
		self.set_itb = wx.Button(self,41,'Go',(200,400))
		self.Bind(wx.EVT_BUTTON,self.bat_o_ball,id=41)
			
	# function to insert data into a listbox
	def insert_listbox(self,data,list_box):
		index=0
		for row in data :
			list_box.InsertStringItem(index,str(row[0]))
			list_box.SetStringItem(index,1,str(row[1]))
			index = index +1
			
	#function to the values from the listcontrol
	def get_values1(self,event):
		self.count = self.count + 1
		if self.count <= 2 :
			print("Getting values..")
			rows = self.show_team1.GetFirstSelected()
			play = int(self.show_team1.GetItemText(rows,col=1))
			play_name = str(self.show_team1.GetItemText(rows,col=0))
			query = "Update "+self.a+" SET Status = '%d' where ID = '%d'AND Team_ID = '%d' AND Match_ID = '%d'"%(int(1),int(play),int(self.team1),self.match_ID)
			conn(query)	
		else :
			print("Two Values already selected")
			self.AskUser('Two Players already selected')
			
	def AskUser(self,text):
		wx.MessageBox(text,'Info',wx.OK|wx.ICON_INFORMATION)
		
		
	def get_values2(self,event):
		if self.count_2 ==0:
			self.count_2 = self.count_2 +1
			print("Getting values..")
			rows = self.show_team2.GetFirstSelected()
			play = int(self.show_team2.GetItemText(rows,col=1))
			play_name = str(self.show_team2.GetItemText(rows,col=0))
			query = "Update "+self.b+" SET Status = '%d' where ID = '%d' AND Team_ID = '%d' AND Match_ID = '%d'"%(int(1),int(play),int(self.team2),self.match_ID)
			conn(query)
		else :
			self.AskUser('Only one bowler can be selected at a time')		
		
			
	# list_box function gets the names and adds the list to list box	
	def list_box(self,data): 
	 	self.player_list =	wx.ListCtrl(self,7,(100,100),wx.Size(200,200),style = wx.LC_REPORT)
	 	self.player_list.InsertColumn(0,'ID',width = 100)
	 	self.player_list.InsertColumn(1,'Name',width = 100)
	 	index = 0
	 	for row in data:
	 		self.player_list.InsertStringItem(index,str(row[1]))
	 		self.player_list.SetStringItem(index,1,row[0])
	 		index = index + 1
	 	if self.team1_o_2 == 9 :		
	 		self.player_list.Bind(wx.EVT_LIST_ITEM_SELECTED,self.first_team,id=7)
	 	elif self.team1_o_2 == 11 :		
	 		self.player_list.Bind(wx.EVT_LIST_ITEM_SELECTED,self.second_team,id=7)
	 		
	# calls when the players from first team are selected		
	def first_team(self,event):
		print(self.team1_o_2)
		self.team1 = int(get_ID(self.team_name))
		print(self.team1)
		self.team_list.Hide()
		rw = self.player_list.GetFirstSelected()
		playing = self.player_list.GetItemText(rw,col=0)
		self.playing_list1.append(playing)
		print(self.playing_list1)
		
	# calls when the players from second team are selected
	def second_team(self,event):
	 	print(self.team1_o_2)
	 	self.team2 = int(get_ID(self.team_name))
	 	print(self.team2)
	 	self.next_team.Hide()
	 	rw = self.player_list.GetFirstSelected()
		playing = self.player_list.GetItemText(rw,col=0)
	 	self.playing_list2.append(playing)
	 	print(self.playing_list2)	
	 	if self.check == 0:
	 		self.Done = wx.Button(self,14,'Done',(200,400))
	 		self.Bind(wx.EVT_BUTTON,self.match_up,id=14)
	 		self.check = 1
# the main function			
app = wx.App()
#declares the object of the parent frame class
frame = MyFrame(None,"ScoreBoard")	
frame.SetTitle("ScoreBoard")
app.MainLoop()
