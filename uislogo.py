# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox


#----------------------
# funciones de la app
#----------------------
def calcular():
        messagebox.showinfo("Minicalculadora 1.0", "Hizo click en el boton calcular")
        s = int(a.get())+int(b.get())
        r = int(a.get())+int(b.get())
        area_resultados.insert(INSERT, f"{a.get()}+{b.get()} = {s} \n ")
        area_resultados.insert(INSERT, f"{a.get()}-{b.get()} = {r} \n ")

def borrar():
    messagebox.showinfo("Minicalculadora 1.0", "Hizo click en el boton borrar")
    a.set("")
    b.set("")
    area_resultados.delete("1.0", "end")

def salir():
    messagebox.showinfo("Minicalculadora 1.0", "La app se cerrara")
    ventana_principal.destroy()
#----------------
# ventana principal
#------------------

# se declara una variable ventana_principal,
# que adquiere las caracteristicas de un objeto tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Mini calculadora 1.0")

# tamano de la ventana 
ventana_principal.geometry("500x500")

# deshabilitar boton maximizar
ventana_principal.resizable(0,0)

# variables de control
a = StringVar()
b = StringVar()
# color de fondo de la ventana

ventana_principal.config(bg="grey")

#----------------------
# frame entrada datos
#---------------------


frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x = 10, y = 10)

logo = PhotoImage(file="img/npaezsar_logo_uis.png")
lb_logo = Label(frame_entrada, image = logo, bg = "white")
lb_logo.place(x=11,y=40)

#etiqueta titulo
lb_titulo = Label(frame_entrada, text="Minicalculadora 1.0")
lb_titulo.config(bg="white", fg="green", font=("Helvetica",20))
lb_titulo.place(x=240,y=10)

# etiqueta para 
lb_a= Label(frame_entrada, text="a : ")
lb_a.config(bg="white", fg="black", font=("Fixedsys", 16) )
lb_a.place(x=250, y=60)

#------------caja 1 texto
entry_a= Entry(frame_entrada)
entry_a.config(bg="white", fg="green", font=("Courier", 20) )
entry_a.focus_set()
entry_a.place(x=290, y=60, width=150, height=30)

# etiqueta para 
lb_b= Label(frame_entrada, text="b : ")
lb_b.config(bg="white", fg="black", font=("Fixedsys", 16) )
lb_b.place(x=250, y=100)

#------------caja 1 texto
entry_b= Entry(frame_entrada)
entry_b.config(bg="white", fg="green", font=("Courier", 20) )
entry_b.place(x=290, y=100, width=150, height=30)



frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x = 10, y = 200)

#boton calcular
boton_calcular = Button(frame_operaciones, text= "Calcular",command=calcular)
boton_calcular.place(x=45, y=35, width=100, height=30)
#boton borrar
boton_borrar = Button(frame_operaciones, text= "Borrar", command= borrar)
boton_borrar.place(x=190, y=35, width=100, height=30)
#boton salir
boton_salir = Button(frame_operaciones, text= "Salir", command= salir)
boton_salir.place(x=335, y=35, width=100, height=30)

#frame resultados

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=180)
frame_resultados.place(x = 10, y = 310)

area_resultados = Text(frame_resultados)
area_resultados.config(bg="black", fg="green", font=("Courier,16"))
area_resultados.place(x=10, y=10, width=460, height=160)



ventana_principal.mainloop()