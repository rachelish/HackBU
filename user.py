class User():

  def __init__(self,name,age,gender,orientation):
    self.name= name
    self.age = age
    self.gender = gender
    self.orientation = orientation

  def orientation(self):
    while True:
      ori = input("Please select the letter of your sexual orientation: S(straight)/G(gay)/B(bisexual)/A(asexual)/P(pansexual) ").lower()
      global orientation
      if ori == "s":
        orientation = "Straight"
        print(orientation)
        return "Straight"
      elif ori == "g":
        orientation = "Gay"
        print(orientation)
        return "Gay"
      elif ori == "b":
        orientation = "bisexual"
        print(orientation)
        return "Bisexual"
      elif ori == "a":
        orientation = "Asexual"
        print(orientation)
        return "Asexual"
      elif ori == "p":
        orientation = "Pansexual"
        print(orientation)
        return "Pansexual"
      else:
        print("ERR: Please input a valid letter. ")
        continue

  def bio(self):
    print(
      f" Name: {self.name}\n Age: {self.age}\n Gender: {self.gender}\n Orientation: {orientation} \n Pronouns: \n{pnouns}"
    )

