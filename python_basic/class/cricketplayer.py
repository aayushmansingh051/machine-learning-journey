import datetime
class  Cricketplayer:
    def __init__ (self,f_name,l_name,age,runs,birth_year):
      self.f_name="Aayushman"
      self.l_name="Singh"
      self.age=21
      self.runs=10001
      self.birth_year=2004
      self.runs=[]

    def get_age(self):
       now=datetime.datetime.now()
       return now.year - self.birth_year
    
    def add_score(self,runs):
       self.runs.append(runs)

    def sum(self):
      
       return sum(self.runs)
       

Aayushman=Cricketplayer('A','S',19,100,2004)
Aayushman.add_score(50)
Aayushman.add_score(101)
Aayushman.add_score(303)

print(Aayushman.get_age())
print(Aayushman.runs)
print(Aayushman.sum())