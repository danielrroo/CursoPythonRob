ejemplo1 = [1,2,3,4,5]
print(ejemplo1)

ejemplo2 = ["a",2.34,'Algo',5,True]
print(ejemplo2)

a = []
for x in range(100):
  if x%2 == 0:
    a.append(x)
print(a)

'''El método index()
devuelve el índice más bajo
de la lista en el que aparece
el elemento buscado
'''
buscar=4

indice=a.index(buscar)

print('El número ' + str(buscar) + ' ocupa el lugar '+ str(indice) + ' en la lista a contando desde cero')

'''
La función count
sirve para contar
las veces que aparece un elemento en una lista
'''

num_apariciones=a.count(44)

print('El elemento: 44 aparece '+str(num_apariciones)+' veces en la lista a')

'''
La función remove
elimina un elemento de la lista
'''

a.remove(44)
print(a)
