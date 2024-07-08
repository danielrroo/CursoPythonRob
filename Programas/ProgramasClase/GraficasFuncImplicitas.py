from sympy import symbols, Eq
from sympy import plot_implicit
x, y = symbols('x y')
plot_implicit(Eq(x**4 - (x**2 - y**3),0), (x,-1.5,1.5), (y, -1.5, 1.5));

