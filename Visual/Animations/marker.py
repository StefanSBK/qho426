import matplotlib.pyplot as plt
import matplotlib.animation as animation

bob, ax = plt.subplots()

def animate(frame):
  ax.cla()
  ax.set_xlim(0, 15)
  ax.set_ylim(0, 15)
  ax.plot(frame, 5, "bo")

def run():
  x = animation.FuncAnimation(bob, animate, frames = 12, interval = 100, repeat = False)
  plt.show()

run()