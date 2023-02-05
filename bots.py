import random
from user import User
class Bots():
#testing if we even need this def statement since i have the import here (it seems fine keep commented out for now)
  #def __init__(self, name, age, genders, orientation):
    names = ["Randy", "Oaks", "Jojo", "Razika", "Jaden", "Rachel", "Jeraph", "Hades", "Preston"]
    gender = ["Female", "Male"]
    orientation = ["Straight", "Gay", "Bisexual", "Asexual"]
    #self.name = random.choice(names)
    #self.age = random.choice(ages)
    #self.gender = random.choice(gender)
    #self.orientation = random.choice(orientation)

for i in range(1, 50):
    bot{i}=User(random.choice(names),random.randint(18,25),random.choice(genders),random.choice(orientation)) 

  def __repr__(self):
    return f" Name: {self.name}\n Age: {self.age}\n Gender: {self.gender}\n Orientation: {self.orientation}\n"

Bot1 = Bots()
Bot1.__repr__()
  
botdict = {}
for x in range(1, 50):
  botdict["Bot{0}".format(x)] = Bots()
  
botdict



  
