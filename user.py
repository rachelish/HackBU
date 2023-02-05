class User():

  def __init__(self):
    name = input("Please enter your name. ")
    age = int(input("Please enter your age. "))
    gender = input("Please enter your gender. (M/F/Other) ")
    self.name = name
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

  def pronouns(self):
    while True:
      pronounTypes = {"He/Him": 0, "She/Her": 1, "They/Them": 2, "Other": 3}
      print(pronounTypes)
      pnouns = input(
        "Please select your pronouns: He/Him, She/Her, They/Them, Other"
      ).lower()
      if pnouns == "he/him":
        pnouns = "He/Him"
        break
      elif pnouns == "she/her":
        pnouns = "She/Her"
        break
      elif pnouns == "they/them":
        pnouns = "They/Them"
        break
      elif pnouns == "other":
        pnouns = input("Please enter your preferred pronouns!")
        break
      else:
        print("ERR: Please enter one of the presented options. ")
        continue

  def bio(self):
    print(
      f" Name: {self.name}\n Age: {self.age}\n Gender: {self.gender}\n Orientation: {orientation} \n Pronouns: \n{pnouns}"
    )

