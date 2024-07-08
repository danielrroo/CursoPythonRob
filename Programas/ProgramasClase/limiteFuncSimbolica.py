#Derivadas
from sympy import symbols, diff, sqrt, sin
x=symbols('x')
dx=diff(sin(x)/x,x)
dx.subs(x,4).evalf()
print(dx)
