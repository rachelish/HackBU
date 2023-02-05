import random

class Bots():

  def __init__(self):
    names = ["Randy", "Oaks", "Jojo", "Razika", "Jaden", "Rachel", "Jeraph", "Hades", "Preston"]
    ages = [18, 19, 20, 21, 22, 23, 24, 25]
    gender = ["Nonbinary", "Female", "Male"]
    orientation = ["Straight", "Gay", "Bisexual", "Asexual"]
    self.name = random.choice(names)
    self.age = random.choice(ages)
    self.gender = random.choice(gender)
    self.orientation = random.choice(orientation)

  def __repr__(self):
    return f" Name: {self.name}\n Age: {self.age}\n Gender: {self.gender}\n Orientation: {self.orientation}\n"

Bot1 = Bots()
Bot1.__repr__()
  
botdict = {}
for x in range(1, 50):
  botdict["Bot {0}".format(x)] = Bots()
  
botdict

def compare():
  if User1.orientation == "s" and User1.gender == "m":
    for x in Bot1.botdict:
        if "Female" in Bot1.botdict[bot]:
          if  "Gay" not in Bot1.botdict[bot]:
            print (Bot1.botdict[bot])
        else:
          pass
  if User1.orientation == "s" and User1.gender == "f":
    for x in Bot1.botdict:
        if "Male" in Bot1.botdict[bot]:
          if  "Gay" not in botdict[bot]:
            print (Bot1.botdict[bot])
        else:
          pass
  
  

compare()
  
