#derivada logaritmo
from sympy import symbols, diff, sqrt, sin, ln, exp
import numpy as np
x=symbols('x')
fx=ln(4**(7*x**2)/5*exp(3*x**5))
dx=diff(fx,x)
#print(dx.subs(x,0.055).evalf())
print(fx.subs(x,200).evalf())
print(dx)
#buscar valor de x tal que el cociente del argumento de ln sea 1
