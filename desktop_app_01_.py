# Se importa la libreria tkinter con todas las funciones
from tkinter import *
from tkinter import messagebox

# ---------------------
# Funciones de la app
# ---------------------
def calcular():
       messagebox.showinfo("Minicalculadora 1.0", "Hizo click en el boton calcular")
       s = int(a.get()) + int(b.get())
       r = int(a.get()) - int(b.get())
       m = int(a.get()) * int(b.get())
       d = int(a.get()) / int(b.get())
       p = int(a.get()) ** int(b.get())
       c = int(a.get()) // int(b.get())
       mod = int(a.get()) % int(b.get())
       t_resultados.insert(INSERT, f"{a.get()} + {b.get()} = {s} \n")
       t_resultados.insert(INSERT, f"{a.get()} - {b.get()} = {r} \n")
       t_resultados.insert(INSERT, f"{a.get()} * {b.get()} = {m} \n")
       t_resultados.insert(INSERT, f"{a.get()} / {b.get()} = {d} \n")
       t_resultados.insert(INSERT, f"{a.get()} ** {b.get()} = {p} \n")
       t_resultados.insert(INSERT, f"{a.get()} // {b.get()} = {c} \n")
       t_resultados.insert(INSERT, f"{a.get()} % {b.get()} = {mod} \n")


def borrar():
       messagebox.showinfo("Minicalculadora 1.0", "Los datos seran borrados...")
       a.set("")
       b.set("")
       t_resultados.delete("1.0", "end")
      

def salir():
    messagebox.showinfo("Minicalculadora 1.0", "La app se cerrará")
    ventana_principal.destroy()

# ---------------------
# Ventana principal
# ---------------------

# Se declara una variable llamada ventana principal, que adquiere las caracteristicas de un objeto TK
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Minicalculadora01")

# tamaño de la ventada
ventana_principal.geometry("500x500")

# deshabilitar botón de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana
ventana_principal.config(bg="gray")

# ---------------------
# Variables de control 
# ---------------------
a = StringVar()
b = StringVar()

# ---------------------
# Frame entrada datos
# ---------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white",width=480, height=180)
frame_entrada.place(x=10,y=10)

# Logo de la app
logo = PhotoImage(file="img/npaezsar_logo_uis.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=11, y=40)

# Etiqueta para el titulo
lb_titulo = Label(frame_entrada, text ="Minicalculadora 1.0")
lb_titulo.config(bg="white", fg="green", font=("helvetica", 20))
lb_titulo.place(x=240, y=10)

# Etiqueta para el primer número 
lb_a = Label(frame_entrada, text="a :")
lb_a.config(bg="white", fg="green", font=("helvetica", 20))
lb_a.place(x=250, y=60)

# Caja de texto (entry) para el primer número
entry_a = Entry(frame_entrada, textvariable=a)
entry_a.config(bg="white", fg="green", font=("courier", 20))
entry_a.focus_set()
entry_a.place(x=290, y=60, width=100, height=30)

# Etiqueta para el segundo número 
lb_b = Label(frame_entrada, text="b :")
lb_b.config(bg="white", fg="green", font=("helvetica", 20))
lb_b.place(x=250, y=100)

# Caja de texto (entry) para el segundo número
entry_b = Entry(frame_entrada, textvariable=b)
entry_b.config(bg="white", fg="green", font=("courier", 20))
entry_b.place(x=290, y=100, width=100, height=30)
# ---------------------
# Frame operaciones
# ---------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white",width=480, height=100)
frame_operaciones.place(x=10,y=200)

# Botón para calcular 
bt_calcular = Button(frame_operaciones, text="Calcular",command=calcular)
bt_calcular.place(x=45, y=35, width=100, height=30)

# Botón para Borrar 
bt_Borrar = Button(frame_operaciones, text="Borrar",command=borrar)
bt_Borrar.place(x=190, y=35, width=100, height=30)

# Botón para Salir 
bt_Salir = Button(frame_operaciones, text="Salir",command=salir)
bt_Salir.place(x=335, y=35, width=100, height=30)


# ---------------------
# Frame resultados
# ---------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white",width=480, height=180)
frame_resultados.place(x=10,y=310)

# Area de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="black", fg="green", font=("courier", 20))
t_resultados.place(x=10, y=10, width=460, height=160)


# Run
# Se ejecuta la función (metodo) mainloop de la clase Tk() a traves de la instancia ventana_principal. Este
# metodo despliega una ventana simple en la pantalla y queda a la espera de lo que el usuario haga. Esta
# acción del usuario se conoce como evento. El mainloop() es un bucle "infinito".
ventana_principal.mainloop()