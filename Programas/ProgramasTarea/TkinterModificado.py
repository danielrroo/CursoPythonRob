"""
Tema: Diccionarios y Entorno Gráfico con Tkinter

Referencia: Charatan, Programming in Two Semesters
            pag 220    
            https://python-forum.io/thread-30362.html   
            
@author: Roberto Méndez Méndez
modificado: Wed Jun 21 2024
"""

from tkinter import Tk, Label, Entry


# Diccionario
calificaciones = {'Pedro' : 8.0 , 'Juan' : 7.8 , 'Yesica' : 8.9 ,
                  'Alexis' : 9.2, 'María' : 9.5, 'Pilar' : 10, 'Amador' : 9.8, }


# Creo la ventana
ventana = Tk()
ventana.title("Consulta de Calificacines")
ventana.eval('tk::PlaceWindow . center')

#Creo los elementos a poner en la ventana 
texto = Label(ventana,  font=('Helvetica 16 bold'), text = '¿Cuál es tu nombre?')
entrada = Entry(ventana, font=('Helvetica 16 bold'),background='#d3f8dd', width=25)
score = Label(ventana,font=('Helvetica 16 bold'),text='')


# Pongo los elementos en la ventana
texto.pack(side = 'left', padx=(20,5), pady=10)
entrada.pack(side='left', padx=(2,20), pady=10)
score.pack(side='bottom', padx= (0,10),pady=(100,5))

# Toma el dato de la entrada después de dar enter
# e imprime el nombre en consola
def mi_entrada(event):
    nombre = entrada.get()
    resultado = calificaciones[nombre]
    score.configure(text = 'Tu calificación es: '+ str(resultado))

# Enlaza el recuadro de entrada con dar Return    
entrada.bind('<Return>', mi_entrada)

ventana.mainloop()
