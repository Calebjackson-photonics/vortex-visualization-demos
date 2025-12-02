import numpy as np
import matplotlib.pyplot as plt

# Create grid
x = np.linspace(-1, 1, 300)
y = np.linspace(-1, 1, 300)
X, Y = np.meshgrid(x, y)

# Create synthetic vortex phase
phase = np.arctan2(Y, X)

# Plot
plt.figure(figsize=(6, 6))
plt.imshow(phase, cmap='twilight', extent=[-1, 1, -1, 1])
plt.colorbar(label="Phase (radians)")
plt.title("Synthetic Optical Vortex Phase Pattern")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
