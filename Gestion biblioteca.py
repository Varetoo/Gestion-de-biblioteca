#==================== IMPORTS ====================
import tkinter as tk
from tkinter import messagebox


#==================== CLASES ====================
class dato:    #Datos STOCK
    def __init__(self, nombre, clave, state):
        self.nombre = nombre
        self.clave = clave
        self.state = state

class user:
    def __init__(self, nombre, premium, prestamos_activos, prestamos_restantes):
        self.__nombre = nombre
        self.premium = premium
        self.__prestamos_activos = prestamos_activos
        self.prestamos_restantes = prestamos_restantes
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def prestamos_activos(self):
        return self.__prestamos_activos
    
    @nombre.setter
    def nombre(self, cadena):
        self.__nombre = cadena
        
    @prestamos_activos.setter
    def prestamos_activos(self, cadena):
        self.__prestamos_activos = cadena


#==================== BASES DE DATOS ====================
#Funciones
def leer_arch(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as base_datos:
            lista = []
            for linea in base_datos:
                linea = linea.strip().split("    ", maxsplit=3)
                lista.append(dato(linea[0], linea[1], linea[2]))
        return lista
        

    except(FileExistsError,FileNotFoundError):
        messagebox.showerror("Error archivo", f"Hay un error con el archivo de datos {nombre_archivo}")


#==================== INTERFAZ ====================
#Confiugración inicial de la ventana
ventana = tk.Tk()
ventana.geometry("900x500")




#==================== CODIGO ====================
#Funciones
def funcion_prueba():
    pass

def change_screen(id):  #funcion que se encarga de cambiar de pantalla la interfaz
    #Eliminamos el contenido de la pantalla anterior
    for widget in ventana.winfo_children():
        widget.destroy()
    #Compone la pantalla actual. Lista de ids: "sing in: 0, sing up: -1, main: 1, solicitar libro: 2, devoluciones: 3"
    if id == 0: #SING IN
        #Titulo ventana
        ventana.title("Sing in")
        #Titulo label
        tk.Label(ventana, text="Gestion de biblioteca", font=("", 24, "underline")).place(relx=0.020,rely=0.05,relwidth=0.4,relheight=0.07)
        #Usuario: []
        tk.Label(ventana, text="Usuario:").place(relx=0.05,rely=0.15,relwidth=0.1,relheight=0.02)
        user = tk.Entry(ventana)
        user.place(relx=0.13,rely=0.145,relwidth=0.1,relheight=0.03)
        #Contraseña: []
        tk.Label(ventana, text="Contraseña:").place(relx=0.05,rely=0.25,relwidth=0.1,relheight=0.02)
        pssw = tk.Entry(ventana)
        pssw.place(relx=0.1,rely=0.3,relwidth=0.1,relheight=0.1)
        #Boton ACEPTAR
        tk.Button(ventana, text="Aceptar", command=funcion_prueba).place(relx=0.1,rely=0.4,relwidth=0.1,relheight=0.1)
        #Boton REGISTRATE
        tk.Label(ventana, text="No tienes cuenta?").place(relx=0.1,rely=0.5,relwidth=0.1,relheight=0.1)
        tk.Button(ventana, text="Registrate", command=lambda: change_screen(-1)).place(relx=0.1,rely=0.5,relwidth=0.1,relheight=0.1)
    
    
    elif id == -1:    #SING UP
        #Titulo ventana
        ventana.title("Sing up")
        #Titulo label
        tk.Label(ventana, text="Gestion de biblioteca", font=("", 24, "underline"), ).grid(row=0, column=0, padx=20, pady=20, columnspan=5)
        #Usuario: []
        tk.Label(ventana, text="Usuario:").grid(row=1, column=0, padx=0, pady=0)
        user = tk.Entry(ventana)
        user.grid(row=1, column=0, padx=30, pady=0, columnspan=100)
        #Contraseña: []
        tk.Label(ventana, text="Contraseña:").grid(row=2, column=0, padx=0, pady=10)
        pssw = tk.Entry(ventana)
        pssw.grid(row=2, column=0, padx=30, pady=10, columnspan=100)
        #Premium ¿?
        tk.Label(ventana, text="Premium por 4,99€/mes?").grid(row=3, column=0, padx=10, pady=10)
        texto = "Disfrutarás de los beneficios premium como tener más cantidad de libros prestados al mismo tiempo\n y poder pedir prestados todos los libros que tengas disponibles a la vez"
        tk.Label(ventana, text=texto).grid(row=4, column=0, padx=10, pady=10, columnspan=100)
        #Boton ACEPTAR
        tk.Button(ventana, text="Aceptar", command=funcion_prueba).grid(row=5, column=1, padx=0, pady=10, columnspan=1)
        
    
    # elif id == 1:     #MAIN
        
    
    # elif id == 2:     #SOLICITAR LIBRO
        
    
    # elif id == 3:     #DEVOLICIONES
        
    
    


#Leemos los arcihvos y almacenamos los datos
users_datos = leer_arch("Datos/base_datos.txt")
stock_datos = leer_arch("Datos/stock_libros.txt")


#Iniciamos la primera pantalla
change_screen(0)


#Lanzamos la interfaz
ventana.mainloop()