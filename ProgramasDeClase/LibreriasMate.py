import math
import numpy
import sympy

print(math.sin(math.pi/3))

print(numpy.sin(numpy.pi/3))

ls = numpy.linspace(0, 10*numpy.pi, 100)
ar = numpy.arange(0, 10*numpy.pi, 0.1)
print(ls)
print(ar)

# Esto es un error
#math.sin(ls)

math.sin(ls[5])

sympy.sin(sympy.pi/3)

sympy.sin(sympy.pi/5)

import matplotlib.pyplot as plt
res = numpy.sin(ar)
plt.plot(ar, res)
plt.show()




