from human import Human
from robot import Robot

class Planet:

  def __init__(self):
    self.humans = []
    self.robots = []

  def __str__(self):
    return f"On this planet, we have humans:{self.humans} and also robots:{self.robots}"

  def __repr__(self):
    return f"humans:{self.humans}, robots:{self.robots}"

  def add_human(self, human):
    self.humans.append(human)

  def remove_human(self, human):
    if human in self.humans:
      self.humans.remove(human)

  def add_robot(self, robo):
    self.robots.append(robo)

  def remove_robot(self, robo):
    if robo in self.robots:
      self.robots.remove(robo)

if __name__ == "__main__":
  Beep = Robot("Beep")
  Stefan = Human("Stefan", 22)
  p1 = Human("Anca")
  p2 = Human("Larry")
  r1 = Robot("RoboCop")
  r2 = Robot("Terminator", 40)
  Earth = Planet()
  print(Earth)
  Earth.add_human(Stefan)
  Earth.add_human(p1)
  Earth.add_human(p2)
  Earth.add_robot(r1)
  Earth.add_robot(r2)
  Earth.add_robot(Beep)
  
