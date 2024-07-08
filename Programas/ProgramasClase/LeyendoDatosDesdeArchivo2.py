import numpy as np

datosF = np.loadtxt('datos1.txt', delimiter=",")
print(datosF)

print(datosF[:,0])

datosF=datosF[:,0]
datosF.sort()
print(datosF)
pos=len(datosF)//2

if len(datosF)%2==0:
    mediana=(datosF[pos-1])+datosF[pos]/2
else:
    mediana=datosF[pos]

print("La mediana es: ", mediana)
