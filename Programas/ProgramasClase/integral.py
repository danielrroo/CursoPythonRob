#integral
from sympy import symbols, integrate, sin, exp
from sympy.plotting import plot
x=symbols('x')
integ=integrate(sin(x), x, (x,-1,1))
print(integ)

plot(sin(x),(x,-1,1))
