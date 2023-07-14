import numpy as np
import matplotlib.pyplot as plt

# Generate values of theta from 0 to 360 degrees (in radians)
theta = np.linspace(0, 2*np.pi, 100)

dot_product = np.abs(np.cos(theta))
cross_product = np.abs(np.sin(theta))

theta_equal = theta[np.argmin(np.abs(dot_product - cross_product))]

plt.plot(theta, dot_product, label='Magnitude of Dot Product')
plt.plot(theta, cross_product, label='Magnitude of Cross Product')

# Mark the value of theta where dot product and cross product are equal
plt.scatter(theta_equal, np.abs(np.cos(theta_equal)), color='red', label='Equal Dot and Cross Product')

plt.title('Comparison of Dot Product and Cross Product')
plt.xlabel('Theta (radians)')
plt.ylabel('Magnitude')
plt.legend(loc='upper right')

a = np.round(np.abs(np.cos(theta_equal)), 2)
b = np.round(np.abs(np.sin(theta_equal)), 2)
plt.text(theta_equal, a, f'a = {a}', horizontalalignment='right', verticalalignment='bottom')
plt.text(theta_equal, b, f'b = {b}', horizontalalignment='left', verticalalignment='top')

plt.grid(True)

# Display the graph
plt.savefig('/sdcard/Documents/Python/figs/vector')
plt.show()

