import random
from planet import Planet
from human import Human
from robot import Robot
import matplotlib.pyplot as plt

class Universe:


  def __init__(self):
    self.planets = []

  def generate(self):
    p = Planet()

    for i in range(random.randint(1,20)):
      r = Robot(f"Robot #{i}")
      p.add_robot(r)

    for i in range(random.randint(1,20)):
      h = Human(f"Human #{i}")
      p.add_human(h)

    self.planets.append(p)

  def show_populations(self):
    num_planets = len(self.planets)

    fig, axs = plt.subplots(1, num_planets)

    for i in range(num_planets):
      planet = self.planets[i]

    # num_humans = 0
    # num_robots = 0

    # for i in planet.inhabitants:
    #   if isinstance(i, Human):
    #     num_humans += 1
    #   if isinstance (i, Robot):
    #     num_robots += 1
      
      num_humans = len(planet.inhabitants["humans"])
      num_robots = len(planet.inhabitants["robots"])

      if num_planets == 1:
        axs.bar(["Humans", "Robots"], [num_humans, num_robots])
      else:
        axs[i].bar(["Humans", "Robots"], [num_humans, num_robots])
      plt.tight_layout()
      plt.show()

if __name__ == "__main__":
  u = Universe()
  u.generate()
  u.generate()
  u.generate()
  u.show_populations()