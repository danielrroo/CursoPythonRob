entero1 = int (input('Dame un entero: '))
entero2 = int (input('Dame otro entero: '))

"""
Operaciones
varias
"""

#Operaciones con enteros
print("Suma: ")
print(entero1 + entero2)

print("División: ")
print(entero1/entero2)

print("Resta: ")
print(entero1-entero2)

print("Multiplicación: ")
print(entero1*entero2)

print("Potencia: ")
print(entero1**entero2)

print("El cociencte o div entera ", entero1//entero2)

print("Operacion modlo residuo ", entero1%entero2)

#Operaciones con float
f1=float((input('Dame un primer número decimal')))
f2=float((input('Segundo decimal')))

print("Suma: ")
print(f1 + f2)

print("División: ")
print(f1/f2)

print("Resta: ")
print(f1-f2)

print("Multiplicación: ")
print(f1*f2)

print("Potencia: ")
print(f1**f2)

print("El cociencte o div entera ", f1//f2)

print("Operacion modlo residuo ", f1%f2)

#Operaciones con Decimal
cantidad=12.31
print("Cantidad es: ",cantidad)
print(f'{cantidad:.20f}')

from decimal import Decimal
cantidad = Decimal(12.31)
print(cantidad)
print(f'{cantidad:.20f}')


"""
f1=Decimal((input('Dame un primer número decimal')))
f2=float((input('Segundo decimal')))

print("Suma: ")
print(f1 + f2)

print("División: ")
print(f1/f2)

print("Resta: ")
print(f1-f2)

print("Multiplicación: ")
print(f1*f2)

print("Potencia: ")
print(f1**f2)

print("El cociencte o div entera ", f1//f2)

print("Operacion modlo residuo ", f1%f2)
"""
