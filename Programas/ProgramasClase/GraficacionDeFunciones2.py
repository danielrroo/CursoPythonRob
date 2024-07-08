from sympy import sin, symbols, Abs
from sympy.plotting import plot
def f(x):
    return Abs(Abs(x)-1)
x=symbols('x')

plot(f(x))
plot(f(f(f(x))));
plot(f(x)*f(x), (x,-5,5), line_color='red')
#plot(f(x)*f(x))
