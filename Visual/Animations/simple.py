import matplotlib.pyplot as plt
import matplotlib.animation as animation

bob, ax = plt.subplots()

def animate(frame):
  ax.set_xlim(0, 10)
  ax.set_ylim(0, 10)
  ax.plot(frame, frame, "ro")

def run():
  x = animation.FuncAnimation(bob, animate, frames = 10, interval = 2000)
  plt.show()

run()