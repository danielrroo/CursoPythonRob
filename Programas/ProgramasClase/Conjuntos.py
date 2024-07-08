#Conjuntos numéricos

U={2,4,6,8,10,12,14}
A=set([2,4,6,8,10])
B={2,6,12}
C={3,5}
D={}

U={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

Uf={x for x in range(1,21)} #desde 2 hasta 20

conjuntovacio=set()

print(U)

print(Uf)

#Numeros pares
A={x for x in Uf if x%2 == 0 and x<10}
print (sorted(A))

#Numeros impares 
B={x for x in Uf if x%2 != 0 and x<10}
print (B)

#Numeros menores a 10
E={x for x in Uf if x<10}
print(E)

#Numeros mayores a 2 y menores iguales a 6
G={x for x in Uf if 2<x and x<=6}
print(G)

#(Ecomplemento)complemento intersec (A-G)complemento

Ec=Uf-E
Ecc=Uf-Ec
AminG=A-G
AminGc = Uf -AminG
resultado= AminGc and Ecc

print(Ecc)
print(AminG)
print(AminGc)
print(resultado)


