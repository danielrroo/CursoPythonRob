#Graficación de Funciones explícitas, implícitas
#paramétricas, polares con sympy y mathplot

from sympy import symbols, sin
from sympy.plotting import plot
x=symbols('x')

fx=0
for i in range(4):
    fx=fx+sin(i*x)

print(fx)
plot(fx)
