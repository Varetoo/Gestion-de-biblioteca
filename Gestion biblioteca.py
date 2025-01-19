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
    def __init__(self, nombre = None, password = None, premium = None, prestamos_activos = None, prestamos_restantes = None):
        self.__nombre = nombre
        self.__password = password
        self.premium = premium
        self.__prestamos_activos = prestamos_activos
        self.prestamos_restantes = prestamos_restantes
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def password(self):
        return self.__password
    
    @property
    def prestamos_activos(self):
        return self.__prestamos_activos
    
    @nombre.setter
    def nombre(self, cadena):
        self.__nombre = cadena
        
    @password.setter
    def password(self, cadena):
        self.__password = cadena
        
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
ventana.geometry("600x400")

def change_screen(id = 0):  #Funcion que se encarga de cambiar de pantalla la interfaz
    #Eliminamos el contenido de la pantalla anterior
    for widget in ventana.winfo_children():
        widget.destroy()
    
    #Compone la pantalla actual. Lista de ids: "sing in: 0, sing up: -1, main: 1, solicitar libro: 2, devoluciones: 3"
    if id == 0: #SING IN
        #Title
        ventana.title("Sing in")
        # Título de la ventana
        titulo = tk.Label(ventana, text="Gestión de biblioteca", font=("", 24, "underline"))
        titulo.place(relx=0.02, rely=0.05, relwidth=0.9, relheight=0.1)

        # Usuario
        label_usuario = tk.Label(ventana, text="Usuario:")
        user_entry = tk.Entry(ventana)
        label_usuario.place(relx=0.25, rely=0.23, relwidth=0.2, relheight=0.03)
        user_entry.place(relx=0.45, rely=0.23, relwidth=0.25, relheight=0.05)

        # Contraseña
        label_password = tk.Label(ventana, text="Contraseña:")
        password_entry = tk.Entry(ventana, show="*")
        label_password.place(relx=0.25, rely=0.3, relwidth=0.2, relheight=0.05)
        password_entry.place(relx=0.45, rely=0.3, relwidth=0.25, relheight=0.05)

        # Botón ACEPTAR
        boton_aceptar = tk.Button(ventana, text="Aceptar", command=lambda: change_screen(1))
        boton_aceptar.place(relx=0.45, rely=0.38, relwidth=0.25, relheight=0.05)

        # Mensaje y botón de REGÍSTRATE
        mensaje_registro = tk.Label(ventana, text="¿No tienes cuenta?")
        boton_registro = tk.Button(ventana, text="Regístrate", command=lambda: change_screen(-1))
        mensaje_registro.place(relx=0.25, rely=0.6, relwidth=0.2, relheight=0.05)
        boton_registro.place(relx=0.45, rely=0.6, relwidth=0.25, relheight=0.05)

        usuario = user(user_entry, password_entry, None, None, )
    
    elif id == -1:    #SING UP
        #Title
        ventana.title("Sing up")
        # Título de la ventana
        titulo = tk.Label(ventana, text="Gestión de biblioteca", font=("", 24, "underline"))
        titulo.place(relx=0.02, rely=0.05, relwidth=0.9, relheight=0.1)
        
        # Usuario
        label_usuario = tk.Label(ventana, text="Usuario:")
        user_entry = tk.Entry(ventana)
        label_usuario.place(relx=0.25, rely=0.23, relwidth=0.2, relheight=0.03)
        user_entry.place(relx=0.45, rely=0.23, relwidth=0.25, relheight=0.05)
        
        # Contraseña
        label_password = tk.Label(ventana, text="Contraseña:")
        password_entry = tk.Entry(ventana, show="*")
        label_password.place(relx=0.25, rely=0.3, relwidth=0.2, relheight=0.05)
        password_entry.place(relx=0.45, rely=0.3, relwidth=0.25, relheight=0.05)
        
        #Premium ¿?
        label_premium = tk.Label(ventana, text="Premium por 4,99€/mes?")
        check1_premium = tk.Checkbutton(ventana, text="Si")
        check2_premium = tk.Checkbutton(ventana, text="No")
        label_ventajas = tk.Label(ventana, text="Disfrutarás de los beneficios premium como tener más cantidad de libros prestados al\nmismo tiempo y poder pedir prestados todos los libros que tengas disponibles a la vez")
        
        label_premium.place( relx=0.20, rely=0.37, relwidth=0.25, relheight=0.03)
        check1_premium.place(relx=0.50, rely=0.37, relwidth=0.06, relheight=0.03)
        check2_premium.place(relx=0.60, rely=0.37, relwidth=0.06, relheight=0.03)
        label_ventajas.place(relx=0.18, rely=0.44, relwidth=0.76, relheight=0.08)
        
        # Botón ACEPTAR
        boton_aceptar = tk.Button(ventana, text="Aceptar", command=lambda: change_screen(1))
        boton_aceptar.place(relx=0.45, rely=0.60, relwidth=0.25, relheight=0.05)
    
    
    elif id == 1:     #MAIN
        #Title
        ventana.title("Main")
        # Título de la ventana
        titulo = tk.Label(ventana, text="Gestión de biblioteca", font=("", 24))
        titulo.place(relx=0.02, rely=0.05, relwidth=0.9, relheight=0.1)
    
    
    # elif id == 2:     #SOLICITAR LIBRO
        
    
    # elif id == 3:     #DEVOLICIONES



#==================== CODIGO ====================
#Funciones
def compr_user():    #Comprueba si los datos introducidos concuerdan con la base de datos
    user = password_entry.get()
    pssw = 

        
    
    


#Leemos los arcihvos y almacenamos los datos
users_datos = leer_arch("Datos/base_datos.txt")
stock_datos = leer_arch("Datos/stock_libros.txt")


#Iniciamos la primera pantalla
change_screen(0)

#Lanzamos la interfaz
ventana.mainloop()