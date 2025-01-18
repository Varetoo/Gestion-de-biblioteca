import tkinter as tk

libros_dicc = {}
try:
    with open("stock_libros.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            titulo, autor = linea.strip().split("    ", maxsplit=1)
            libros_dicc[titulo] = autor



except (FileExistsError, FileNotFoundError):
    input(f"El archivo {archivo}, no se encuentra o no existe")


    

#Ventana
ventana = tk.Tk()
ventana.geometry("900x500")

#===============================================
def buscar_en_diccionario(*args):
    resultado_busqueda = {} #titulo: autor
    texto = variable_buscador.get()
    for titulo in libros_dicc:
        if texto in titulo: 
            resultado_busqueda[titulo] = libros_dicc[titulo]
    print(f"Buscando: {texto}\nResultado:{resultado_busqueda}")



#Variable para el input
variable_buscador = tk.Entry(ventana)
variable_buscador.grid(row=0, column=0, padx=10, pady=10)

#Boton de input
tk.Button(ventana, text="Buscar", command=buscar_en_diccionario).grid(row=1,column=0, padx=10, pady=10)




ventana.mainloop()