#Uso de tuplas

alumnos_calif=('Alex', 9), ('Benito', 10), ('Carlos', 8), ('Diana', 9), ('Elsa', 8)

#Obteniendo el promedio de calificaciones de todos los alumnos

promedio=0.0
suma=0.0
i=0
for cont in alumnos_calif:
    suma=suma+alumnos_calif[i][1]
    i=i+1
promedio=suma/i

print("El promedio de calificación del grupo es: ",promedio)
