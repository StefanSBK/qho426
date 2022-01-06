# The class Person wich will be a blueprint/template for my objects to store information about humans
class Person:

  #Class attribute -> constant, which is visible to all objects of the class
  MAX_ENERGY = 100

  #Static Method -> Utility Function, wich does not require an object to exist
  @staticmethod
  def is_mature(age):
    if age >= 35:
      return True
    else:
      return False

# Initializer constructur -> Function called straight away when object is created
  def __init__(self, name = "", age = 1, job = "None", weight = 5, energy = 100):
    # This will be instance Attribute (features of each object)
    self.name = name
    self.age = age
    self.job = job
    self.weight = weight
    if energy > Person.MAX_ENERGY:
      self.energy = Person.MAX_ENERGY
    else:
      self.energy = energy
  #"Dunder" = Double Underscore
  #Magic method __str__ which is invoked by print() function automatically
  def __str__(self):
    return f"Name:{self.name}\nAge:{self.age}\nJob:{self.job}\nWeight:{self.weight}\nEnergy{self.energy}\n"
  
  
  # Instance method that works on each object of the class
  def hello(self):
    print(f"Hello! My name is {self.name}, I'm {self.age} years old. I work as {self.job}. I weight {self.weight} kg and my energy is currently {self.energy}. Nice to meet you!")

  def grow(self, years):
    self.age += years

  def eat(self, food, w):
    print(f"{self.name} eaten {food}")
    self.weight += w
    print(f"They now weight {self.weight}kg")

if __name__ == "__main__":
    p1 = Person("Alessandro", 28, "MacGyver", 68, 999)
    p2 = Person("Dawid", job = "Clerck")
    # p2.hello()
    # p1.hello()
    # p1.job = "IT Consultant"
    # p1.energy = 25
    # p1.age += 1
    # p1.hello()
    # p2.eat("Lasagne", 3)
    # p2.grow(20)
    # p2.hello()

    print(p1)
    print(p2)
    p1.hello()
    print(f"{Person.is_mature(50)}")
    print(f"{Person.is_mature(22)}")
    print(f"{Person.is_mature(p2.age)}")