from sympy import symbols, cos, sin, exp, pi
from sympy import plot_parametric

t=symbols('t')
def x(t):
    return sin(t) * (exp(cos(t)) - 2 * cos(4*t) -sin(t/12)**5)

def y(t):
    return cos(t) * (exp(cos(t)) - 2*cos(4*t) - sin(t/12)**5 )

plot_parametric(x(t), y(t), (t, -6*pi, 6*pi))
plot_parametric(x(t), y(t), (t, -50, 50))
