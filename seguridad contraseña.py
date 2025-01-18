'''
Modificar con variables nuevas, La funcion buscar_en_diccionario() se ejecuta cada vez que hay un cambio en el Entry
'''
import tkinter as tk

#Ventana
ventana = tk.Tk()
ventana.geometry("900x500")

#===============================================
def buscar_en_diccionario(*args):
    texto = variable_buscador.get()


#Variable para el input
variable_buscador = tk.StringVar()
variable_buscador.trace_add("write", buscar_en_diccionario)


#Boton de input
tk.Entry(ventana, textvariable=variable_buscador).grid(row=0, column=0, padx=10, pady=10)




ventana.mainloop()