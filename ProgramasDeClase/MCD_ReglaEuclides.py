#máximo común divisor / algoritmo de euclides
"""
a=b*q+r1   0<=r1<|b|
b=r1*q1+r2
r1=r2*q1+r2
"""

a=int(input("Dame un entero: "))
b=int(input("Dame otro entero: "))

q= a//b
r=a-b*q

#El cuerpo del while se construye con identación, no con llaves ni paréntesis
while r != 0 :
    a=b
    b=r
    print(a,b)
    q=a//b
    r=a-b*q
print("El máximo común divisor es: ", b)

#(a,b) = (|a|,|b|)
#Tarea: utilizando el algoritmo de Euclides, extender el programa para todo a,b elemento de Z con a>b
#Es decir incluyendo negativos,  
