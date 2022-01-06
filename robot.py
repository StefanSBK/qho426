class Robot:

  MAX_ENERGY = 100

  def __init__(self):
    self.name = "Beep"
    self.age = 0
    self.energy = 0

  def __repr__(self):
      return f'name:{self.name}, age:{self.age}, energy:{self.energy}'

  def __str__(self):
      return f'Robot {self.name} is {self.age} years old and has{self.energy} energy left'

  def display(self):
    print(f"I am {self.name}")

if __name__ == "__main__":
  human = Robot()
  human.display()
  print(human)
  print(repr(human))