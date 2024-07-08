from sympy import sqrt, sin, symbols
from sympy import plot_implicit

x, y = symbols('x y')
plot_implicit(sin(x**5)+(x-2*y**2) > 0, (x, -2, 4), (y, -2, 2));
