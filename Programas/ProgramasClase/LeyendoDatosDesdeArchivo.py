import os #Sirve para ubicarme en cierto directorio
import pandas as pd
import numpy as np
#os.chdir("")
#frm=pd.read_csv('datos5.txt') #archivo
frm=pd.read_csv('datos1.txt', header=None) #archivo
print("Tipos de datos: \n",frm.dtypes)#Imprime el tipo de datos de la info que leyó

print("Últimos valores: \n",frm.tail())

print("Columna del archivo: \n", frm.columns)

#print(frm.columns)
'''
print(frm[' Peso'].min())
print(frm[' Peso'].max())
print(frm[' Peso'].mean())
print(frm[' Peso'].std())
print(frm[' Peso'].count())
'''



