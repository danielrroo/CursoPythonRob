import math
serieRaiz=[]
n=80
x=8

for i in range(6):
    x=(1/2)*(x+n/x)
    serieRaiz.append(x)

print("La raiz aproximada de {0} es {1:.20}".format(n,x))
print("La raiz aproximada de {0} es {1:.20}".format(n,math.sqrt(n)))
print("La raiz sucesión es: ", serieRaiz)
