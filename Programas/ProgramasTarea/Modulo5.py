ClaseEquiv0 = set()
ClaseEquiv1 = set()
ClaseEquiv2 = set()

for i in range(100):
    if i % 5 == 0:
        ClaseEquiv0.add(i)
        ClaseEquiv0.add(-i)
    elif i % 5 == 1:
        ClaseEquiv1.add(i)
        ClaseEquiv1.add(-i)
    else:
        ClaseEquiv2.add(i)
        ClaseEquiv2.add(-i)

print("Clase [0] =", sorted(ClaseEquiv0))
print("Clase [1] =", sorted(ClaseEquiv1))
print("Clase [2] =", sorted(ClaseEquiv2))

print("La intersección de los tres conjuntos es: ",
      ClaseEquiv0 & ClaseEquiv1 & ClaseEquiv2)

print("La unión de los tres conjuntos es: ",
      sorted(ClaseEquiv0 | ClaseEquiv1 | ClaseEquiv2))
