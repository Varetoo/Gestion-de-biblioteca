import tkinter as tk

class GestionBiblioteca:
    def __init__(self):
        self.ejemplo = [
            "Libro 1",
            "Libro 2",
            "Libro 3",
            "Libro 4",
            "Libro 5"
        ]

def on_accept(seleccion, clase):
    if seleccion.get() == -1:
        print("No se ha seleccionado ningún libro.")
    else:
        libro_seleccionado = clase.ejemplo[seleccion.get()]
        print(f"Has seleccionado: {libro_seleccionado}")

def generar_interfaz(ventana, clase):
    # Título de la ventana
    ventana.title("Gestión de Biblioteca")
    ventana.geometry("400x400")
    
    # Label principal
    titulo_label = tk.Label(ventana, text="Gestión de Biblioteca", font=("Arial", 16, "bold"))
    titulo_label.pack(pady=10)

    # Variable IntVar para controlar los Checkbuttons (solo uno seleccionado)
    seleccion = tk.IntVar()
    seleccion.set(-1)  # Ningún Checkbutton seleccionado inicialmente

    # Crear los Checkbuttons dinámicamente
    for index, item in enumerate(clase.ejemplo):
        # Crear el Checkbutton con un valor único para cada elemento
        checkbutton = tk.Checkbutton(
            ventana, 
            text=item,
            variable=seleccion,
            onvalue=index,  # Este Checkbutton se selecciona cuando seleccion == index
            offvalue=-1     # Cuando se deselecciona, seleccion vuelve a -1
        )
        checkbutton.pack(anchor="w", padx=20, pady=5)

    # Botón Aceptar
    boton_aceptar = tk.Button(
        ventana,
        text="Aceptar",
        command=lambda: on_accept(seleccion, clase)  # Pasamos la variable y la clase a la función
    )
    boton_aceptar.pack(pady=20)

# Crear la ventana y la clase
def main():
    ventana = tk.Tk()
    biblioteca = GestionBiblioteca()
    generar_interfaz(ventana, biblioteca)
    ventana.mainloop()

if __name__ == "__main__":
    main()