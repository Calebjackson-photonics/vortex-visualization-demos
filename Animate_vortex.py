import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(-1, 1, 250)
y = np.linspace(-1, 1, 250)
X, Y = np.meshgrid(x, y)

fig, ax = plt.subplots(figsize=(6,6))

def update(frame):
    phase = np.arctan2(Y, X) + frame*0.05
    ax.clear()
    ax.imshow(phase, cmap='twilight', extent=[-1,1,-1,1])
    ax.set_title("Optical Vortex Phase Evolution")
    ax.axis("off")

ani = FuncAnimation(fig, update, frames=120, interval=50)
plt.show()
