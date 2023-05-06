# se importa la libreria tkinter con todas sus funciones
from tkinter import *

#----------------------
# funciones de la app
#----------------------

#----------------
# ventana principal
#------------------

# se declara una variable ventana_principal,
# que adquiere las caracteristicas de un objeto tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Sistemas UIS Socorro")

# tamano de la ventana 
ventana_principal.geometry("500x500")

# deshabilitar boton maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana

ventana_principal.config(bg="white")

#----------------------
# frame entrada datos
#---------------------


frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="red", width=140, height=230)
frame_entrada.place(x = 0, y = 0)

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="red", width=320, height=230)
frame_entrada.place(x = 230, y = 0)

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="blue", width=500, height=50)
frame_entrada.place(x = 0, y = 250)

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="blue", width=50, height=500)
frame_entrada.place(x = 160, y = 0)

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="red", width=140, height=200)
frame_entrada.place(x = 0, y = 320)


frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="red", width=300, height=200)
frame_entrada.place(x = 230, y = 320)























#run
# SE EJERCUTA LA FUNCION (METODO) MAINLOOP() DE LA CLASE TK()
#  a traves de la instancia ventana_principal. este metodo despliega una ventana
# simple en pantalla y queda a la espera de lo que el usuario haga. cada accion del usuario se
# conoce como evento. el mainloop() es un bucle infinito. 
ventana_principal.mainloop()