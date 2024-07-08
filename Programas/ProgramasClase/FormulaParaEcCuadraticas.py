import math
import cmath

valores=input("Dame los coeficientes a b c de la ec de 2do grado ax2+bx+c=0 :" )

a,b,c = valores.rsplit()

a = float(a)
b = float(b)
c = float(c)

if b**2 - 4*a*c>=0:
        x1= (-b + math.sqrt(b**2-4*a*c))/(2*a)
        x2= (-b - math.sqrt(b**2-4*a*c))/(2*a)
        print(x1)
        print(x2)
else:
        x1= (-b + cmath.sqrt(b**2-4*a*c))/(2*a)
        x2= (-b - cmath.sqrt(b**2-4*a*c))/(2*a)
        print(x1)
        print(x2)

