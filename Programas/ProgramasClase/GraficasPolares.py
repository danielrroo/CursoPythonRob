#Coordenadas polares

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 4000)
r=3*np.cos(6*theta)
x=r*np.sin(theta)
y=r*np.cos(theta)

plt.axis('off');
plt.axis('equal');
plt.plot(x,y)
