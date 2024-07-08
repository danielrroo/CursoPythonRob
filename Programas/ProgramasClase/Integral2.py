#Integral de una func particular
from sympy import symbols, integrate, sin, exp, sqrt
from sympy.plotting import plot
x=symbols('x')
integ=integrate((1-x)/(sqrt(2-x)), x)
print(integ)
