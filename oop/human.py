class Human:

  MAX_ENERGY = 100

  def __init__(self, name = "Human", age = 0):
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  def __repr__(self):
      return f'name:{self.name}, age:{self.age}, energy:{self.energy}'

  def __str__(self):
      return f'Human {self.name} is {self.age} years old and has{self.energy} energy left'

  def display(self):
    print(f"I am {self.name}")

  def grow(self):
    self.age += 1

  def eat(self, amount):
    self.energy += amount
    if self.energy > Human.MAX_ENERGY:
      self.energy = Human.MAX_ENERGY

  def move(self, distance):
    self.energy -= distance
    if self.energy < 0:
      self.energy = 0

if __name__ == "__main__":
  human = Human()
  human.display()
  print(human)
  human.move(27)
  print(human)
  human.eat(11)
  human.eat(2)
  print(human)