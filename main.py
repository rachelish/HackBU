from bots import Bots  
#import Bots
from user import User
from comparison import Compare


def main():
  global User1
  user = User(input("Enter your name: "), int(input("Enter your age: ")), input("Enter your gender (M/F): "), input("Enter your sexual orientation: "))
  Bot1 = Bots()


main()
