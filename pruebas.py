import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("300x200")

def eliminar_label():
    global label
    if label:  # Verificar si el widget existe
        #Cambiamos el label
        label = tk.Label(ventana, text="¡Hola, soy un Label cambiado!")
        label.pack(pady=20)  # Eliminar el widget

def main():
    

    # Crear un Label (widget)
    global label
    label = tk.Label(ventana, text="¡Hola, soy un Label!")
    label.pack(pady=20)
    
    

    # Crear un botón para eliminar el Label
    boton = tk.Button(ventana, text="Eliminar Label", command=eliminar_label)
    boton.pack()

    ventana.mainloop()

main()