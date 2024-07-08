from sympy import symbols, Integral, sin, integrate, exp, oo

x=symbols('x')
intsen=Integral(sin(x),(x,-1,1))
print('El resultado es: ', intsen.evalf())


x=symbols('x')
print(integrate(exp(-x), (x,0,oo)))
