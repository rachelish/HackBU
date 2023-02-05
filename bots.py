import random
from user import User
#from locations imporT


class Bots():
  names = [
    "Randy", "Oaks", "JoJo", "Razika", "Jaden", "Rachel", "Jeraph", "Hades",
    "Preston"
  ]
  gender = ["female", "male"]
  ori = ["straight", "gay", "bisexual", "asexual"]
  #location = random.choice()

botList = []
for i in range(50):
  bot = User(random.choice(Bots.names), random.randint(18, 25),
             random.choice(Bots.gender), random.choice(Bots.ori))
  botList.append(bot)

#u iterated thru bots class instead of botList so it hated u
#now the issue is sumn inside the loop
#
#just testing to see if the bots are working properly but cant get to run :(
#wait a sec this works
#raz we can do that right
  #idk what that is is it supposed to be built in
  #cant we jsut print the info instead of creating a function for displaying
  # yes we can lol
  #
  # it took the hash number instead ofthe actual number
  #we can honestly out this all in main.py if needed
      
