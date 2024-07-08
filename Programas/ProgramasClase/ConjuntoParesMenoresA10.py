U = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
Uf = {x for x in range(1,21)}
conjuntovacio = set()
print(U)
print(Uf)

#Obteniendo numeros pares menores a 10
A = {x for x in Uf if x%2 == 0 and x < 10}
print(A)

B={x for x in Uf if x%2!=0 and x<10}
print(B)

