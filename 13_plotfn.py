import matplotlib.pyplot as plt
import numpy as np

# Create values for x from -10 to 10
x = np.linspace(-10, 10, 100)
y=x**2

plt.plot(x,y)
plt.show()