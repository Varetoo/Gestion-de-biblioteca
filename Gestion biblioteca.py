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
        print(cadena)
        self.__nombre = cadena
        
    @password.setter
    def password(self, cadena):
        self.__password = cadena
        
    @prestamos_activos.setter
    def prestamos_activos(self, cadena):
        self.__prestamos_activos = cadena

class checkbutton:
    def __init__(self, estado = None):
        self.__estado = estado
    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, cadena):
        self.__estado = cadena


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

def change_screen(id = 0):  #Funcion que se encarga de eliminar el contenido que hay en la pantalla actual y luego llama a la funcion correspondiente al id dado
    #Eliminamos el contenido de la pantalla anterior
    for widget in ventana.winfo_children():
        widget.destroy()
    
    if   id == 0: screen0()   #SING IN 
    elif id == 1: screen1()   #SING UP
    elif id == 2: screen2()   #MAIN
    elif id == 3: screen3()   #SOLICITAR LIBRO
    elif id == 4: screen4()   #DEVOLICIONES

def screen0():  #Sing in
    #Title
    ventana.title("Sing in")
    # Título de la ventana
    titulo = tk.Label(ventana, text="Gestión de biblioteca", font=("", 24, "underline"))
    titulo.place(relx=0.02, rely=0.05, relwidth=0.9, relheight=0.1)

    # Usuario
    label_user = tk.Label(ventana, text="Usuario:")
    user_entry = tk.Entry(ventana)
    label_user.place(relx=0.25, rely=0.23, relwidth=0.2, relheight=0.03)
    user_entry.place(relx=0.45, rely=0.23, relwidth=0.25, relheight=0.05)

    # Contraseña
    label_password = tk.Label(ventana, text="Contraseña:")
    password_entry = tk.Entry(ventana, show="*")
    label_password.place(relx=0.25, rely=0.3, relwidth=0.2, relheight=0.05)
    password_entry.place(relx=0.45, rely=0.3, relwidth=0.25, relheight=0.05)

    # Botón ACEPTAR
    boton_aceptar = tk.Button(ventana, text="Aceptar", command=lambda: compr_contra(compr_user()))
    boton_aceptar.place(relx=0.45, rely=0.38, relwidth=0.25, relheight=0.05)

    # Mensaje y botón de REGÍSTRATE
    mensaje_registro = tk.Label(ventana, text="¿No tienes cuenta?")
    boton_registro = tk.Button(ventana, text="Regístrate", command=lambda: change_screen(1))
    mensaje_registro.place(relx=0.25, rely=0.6, relwidth=0.2, relheight=0.05)
    boton_registro.place(relx=0.45, rely=0.6, relwidth=0.25, relheight=0.05)

    #Mandamos los valores a class: user
    usuario.nombre = user_entry
    usuario.password = password_entry

def screen1():  #Sing up
    #Title
    ventana.title("Sing up")
    # Título de la ventana
    titulo = tk.Label(ventana, text="Gestión de biblioteca", font=("", 24, "underline"))
    titulo.place(relx=0.02, rely=0.05, relwidth=0.9, relheight=0.1)
    
    # Usuario
    label_user = tk.Label(ventana, text="Usuario:")
    user_entry = tk.Entry(ventana)
    label_user.place(relx=0.25, rely=0.23, relwidth=0.2, relheight=0.03)
    user_entry.place(relx=0.45, rely=0.23, relwidth=0.25, relheight=0.05)
    
    # Contraseña
    label_password = tk.Label(ventana, text="Contraseña:")
    password_entry = tk.Entry(ventana, show="*")
    label_password.place(relx=0.25, rely=0.3, relwidth=0.2, relheight=0.05)
    password_entry.place(relx=0.45, rely=0.3, relwidth=0.25, relheight=0.05)
    
    #Premium ¿?
    label_premium = tk.Label(ventana, text="Premium por 4,99€/mes?")
    var_ch1 = tk.IntVar()
    var_ch2 = tk.IntVar()
    check1_premium = tk.Checkbutton(ventana, text="Si", variable=var_ch1, command=lambda: checkbutton_no_iguales(1))
    check2_premium = tk.Checkbutton(ventana, text="No", variable=var_ch2, command=lambda: checkbutton_no_iguales(2))
    check1.estado = var_ch1
    check2.estado = var_ch2
    label_ventajas = tk.Label(ventana, text="Disfrutarás de los beneficios premium como tener más cantidad de libros prestados al\nmismo tiempo y poder pedir prestados todos los libros que tengas disponibles a la vez")
    
    label_premium.place( relx=0.20, rely=0.37, relwidth=0.25, relheight=0.03)
    check1_premium.place(relx=0.50, rely=0.37, relwidth=0.06, relheight=0.03)
    check2_premium.place(relx=0.60, rely=0.37, relwidth=0.06, relheight=0.03)
    label_ventajas.place(relx=0.18, rely=0.44, relwidth=0.76, relheight=0.08)
    
    # Botón ACEPTAR
    boton_aceptar = tk.Button(ventana, text="Aceptar", command=compr_checks)
    boton_aceptar.place(relx=0.45, rely=0.60, relwidth=0.25, relheight=0.05)
    
    #Mandamos los valores a class: user
    usuario.nombre = user_entry
    usuario.password = password_entry

def screen2():  #Main
    #Title
    ventana.title("Main")
    # Título de la ventana
    titulo = tk.Label(ventana, text="Gestión de biblioteca", font=("", 24))
    titulo.place(relx=0.02, rely=0.05, relwidth=0.9, relheight=0.1)

def screen3():  #Solicitar libro
    #Title
    ventana.title("Main")
    # Título de la ventana
    titulo = tk.Label(ventana, text="Gestión de biblioteca", font=("", 24))
    titulo.place(relx=0.02, rely=0.05, relwidth=0.9, relheight=0.1)

def screen4():  #Devoluciones
    #Title
    ventana.title("Main")
    # Título de la ventana
    titulo = tk.Label(ventana, text="Gestión de biblioteca", font=("", 24))
    titulo.place(relx=0.02, rely=0.05, relwidth=0.9, relheight=0.1)


#==================== CODIGO ====================
#Leemos los arcihvos y almacenamos los datos
users_list = leer_arch("Datos/base_datos.txt")
stock_list = leer_arch("Datos/stock_libros.txt")

#Funciones
def checkbutton_no_iguales(ultimo): #Funcionalidad para que no se puedan pulsar los dos checks a la vez
    c1 = check1.estado.get()
    c2 = check2.estado.get()
    if c1 == c2:
        if ultimo == 1: #El ultimo check en activarse fue el 1
            check2.estado.set(0)
        elif ultimo == 2: #El ultimo check en activarse fue el 2
            check1.estado.set(0)

def compr_user():    #Comprueba si los datos introducidos concuerdan con la base de datos
    #Comprobamos si el usuario existe
    name = usuario.nombre.get()
    for i, elemento in enumerate(users_list):
        if elemento.nombre == name:
            encontrado = True   #El nombre está en la lista
            break
        encontrado = False
    return [encontrado,i]
        
def compr_contra(lista):
    if lista[0] == False: messagebox.showerror("Error usuario", f"No se ha encontrado el nombre de usuario")    #lista[0] == encontrado
    elif lista[0] == True:    #Buscamos si la contraseña coincide
        contra = usuario.password.get()
        if contra == users_list[lista[1]].clave:    #lista[1] == i
            messagebox.showinfo("Login", "Login efectuado correctamente")
            change_screen(2)
        else: messagebox.showerror("Password error", "Contraseña incorrecta")

def compr_checks():
    c1 = check1.estado.get()
    c2 = check2.estado.get()
    #Si al menos uno está activo..
    if c1 == 1 or c2:
        return True
    else: return False


#Creamos el perfil del usuario vacio y los checkbuttons vacios
usuario = user()
check1 = checkbutton()
check2 = checkbutton()

#Lanzamos la interfaz
change_screen(0)
ventana.mainloop()