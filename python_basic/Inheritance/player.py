import datetime

class Player:
   def __init__ (self,fname,lname,birth_year):
    self.fname=fname
    self.lname=lname
    self.birth_year=birth_year

   def get_age(self):
     
     now=datetime.datetime.now()
     return now.year-self.birth_year

class Cricketplayer(Player):
    def __init__ (self,fname,lname,team,birth_year):
     Player. __init__(self,fname,lname,birth_year)
     self.team=team
     self.scores=[]

    def add_score(self,score):
       self.scores.append(score)

class TennisPlayer(Player):
    def __init__ (self,fname,lname,birth_year,gwinner):
     Player. __init__(self,fname,lname,birth_year)
     self.gland_slam_winner=gwinner
     self.aces=[]

    def get_avg_aces_permatch(self,aces):
      return sum(aces)/len(aces)
    
virat= Cricketplayer('Virat','kohli','india',1988)
virat.add_score(100)
virat.add_score(200)
virat.add_score(300)

print("Age of virat kohli is: ",virat.get_age())

roger=TennisPlayer('rogger','chodu',1988,28)
print("roge age:",roger.get_age())
    
    


       
