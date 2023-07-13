import numpy as np
import matplotlib.pyplot as plt

# Generate values of theta from 0 to 360 degrees (in radians)
theta = np.linspace(0, 2*np.pi, 100)

dot_product = np.abs(np.cos(theta))
cross_product = np.abs(np.sin(theta))

plt.plot(theta, dot_product, label='Magnitude of Dot Product')
plt.plot(theta, cross_product, label='Magnitude of Cross Product')

plt.title('Comparison of Dot Product and Cross Product')
plt.xlabel('Theta (radians)')
plt.ylabel('Magnitude')
plt.legend()
plt.grid(True)

# Display the graph
plt.savefig('/sdcard/Documents/Python/figs//fig')
plt.show()
