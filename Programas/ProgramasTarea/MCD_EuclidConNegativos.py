a = int(input("Dame el primer entero: "))
b = int(input("Dame el segundo entero: "))


if a<0:
    a=a-2*a
    print(a)
else:
    a=a
if b<0:
    b=b-2*b
    print(b)
else:
    b=b


q = a//b
r = a - b*q
while r != 0 :
  a = b
  b = r
  print(a, b)
  q = a//b
  r = a - b*q
print("El máximo común divisor es: ", b)
