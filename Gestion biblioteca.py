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
    def __init__(self, nombre = None, password = None, premium = None, prestamos_activos = None, prestamos_restantes = None, seguridad_contra = None):
        self.__nombre = nombre
        self.__password = password
        self.premium = premium
        self.__prestamos_activos = prestamos_activos
        self.prestamos_restantes = prestamos_restantes
        self.seguridad_contra = seguridad_contra
    
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

def add_arch(nombre_archivo):
    try:
        with open(nombre_archivo, "a", encoding="utf-8") as base_datos:
            base_datos.write(f"\n{usuario.nombre}    {usuario.password}    {usuario.premium}")

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
    user_label = tk.Label(ventana, text="Usuario:")
    user_entry = tk.Entry(ventana)
    user_label.place(relx=0.25, rely=0.23, relwidth=0.2, relheight=0.03)
    user_entry.place(relx=0.45, rely=0.23, relwidth=0.25, relheight=0.05)
    
    # Contraseña
    password_label = tk.Label(ventana, text="Contraseña:")
    global password_status
    password_status = tk.StringVar()
    password_status.trace_add("write", seguridad_pssw)
    password_entry = tk.Entry(ventana, textvariable=password_status, show="*")
    
    global seguridad_label
    seguridad_label = tk.Label(ventana, text="", fg="red")
    seguridad_label.place(relx=0.75, rely=0.3, relwidth=0.20, relheight=0.05)
    
    password_label.place( relx=0.25, rely=0.3, relwidth=0.20, relheight=0.05)
    password_entry.place( relx=0.45, rely=0.3, relwidth=0.25, relheight=0.05)
    
    # Premium ¿?
    premium_label = tk.Label(ventana, text="Premium por 4,99€/mes?")
    ch1_var = tk.IntVar()
    ch2_var = tk.IntVar()
    check1_premium = tk.Checkbutton(ventana, text="Si", variable=ch1_var, command=lambda: checkbutton_no_iguales(1))
    check2_premium = tk.Checkbutton(ventana, text="No", variable=ch2_var, command=lambda: checkbutton_no_iguales(2))
    check1.estado = ch1_var
    check2.estado = ch2_var
    ventajas_label = tk.Label(ventana, text="Disfrutarás de los beneficios premium como tener más cantidad de libros prestados al\nmismo tiempo y poder pedir prestados todos los libros que tengas disponibles a la vez")
    premium_label.place( relx=0.20, rely=0.37, relwidth=0.25, relheight=0.03)
    check1_premium.place(relx=0.50, rely=0.37, relwidth=0.06, relheight=0.03)
    check2_premium.place(relx=0.60, rely=0.37, relwidth=0.06, relheight=0.03)
    ventajas_label.place(relx=0.18, rely=0.44, relwidth=0.76, relheight=0.08)
    
    # Botón ACEPTAR
    boton_aceptar = tk.Button(ventana, text="Aceptar", command=compr_registro)
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

#Funciones
def checkbutton_no_iguales(ultimo): #Funcionalidad para que no se puedan pulsar los dos checks a la vez
    c1 = check1.estado.get()
    c2 = check2.estado.get()
    if c1 == c2:
        if ultimo == 1: #El ultimo check en activarse fue el 1
            check2.estado.set(0)
        elif ultimo == 2: #El ultimo check en activarse fue el 2
            check1.estado.set(0)

def compr_user():    #Comprueba si el usuario exist en la base de datos
    #Comprobamos si el usuario existe
    name = usuario.nombre.get()
    for i, elemento in enumerate(users_list):
        if elemento.nombre.lower() == name.lower():
            encontrado = True   #El nombre está en la lista
            break
        encontrado = False
    return [encontrado,i]
        
def compr_contra(lista):    #Muestra por pantalla si el usuario existe y completa el login si la contraseña coincide.   lista -> [encontrado, i] de la funcion compr_user
    if lista[0] == False: messagebox.showerror("Error usuario", f"No se ha encontrado el nombre de usuario")    #lista[0] == encontrado
    elif lista[0] == True:    #Buscamos si la contraseña coincide
        contra = usuario.password.get()
        if contra == users_list[lista[1]].clave:    #lista[1] == i
            messagebox.showinfo("Login", "Login efectuado correctamente")
            change_screen(2)
        else: messagebox.showerror("Password error", "Contraseña incorrecta")

def puntuacion(contra):  #Función que verifica la seguridad del usuario según varios factores y devuelve una puntuación que va desde -6 hasta 6 según su seguridad
    punt = 0
    #Longitud
    if len(contra) < 8: punt -= 1   #Puntuamos segun los criterios
    elif len(contra) > 12: punt += 1
    
    #Mayusculas
    mayus = len([letra for letra in contra if letra.isupper()])
    if mayus == 0 or mayus == 1: punt -=1   #Puntuamos segun los criterios
    elif mayus >= 3: punt +=1
    
    #Numeros
    num = len([numero for numero in contra if numero.isdigit()])
    if num == 0 or num == 1: punt -=1   #Puntuamos segun los criterios
    elif num >= 3: punt +=1
    
    #Caracteres especiales
    simbolos = 0
    cadena_especiales = "!#$%&()-/:;<=>?@[]^_"
    for letra in contra:
        for caracter in cadena_especiales:
            if letra == caracter: simbolos += 1
    if simbolos == 0: punt -=1   #Puntuamos segun los criterios
    elif simbolos >= 2: punt +=1
    
    #Repeticion de caracteres
    conteo = {}
    
    for letra in contra:
        if letra not in conteo: conteo[letra] = 1
        else: conteo[letra] += 1

    car_rep = 0 #Contamos los caracteres que se repiten y lo sumamos
    lista_rep = list(conteo.values())
    for valor in lista_rep:
        if valor > 1:
            car_rep += valor    #'car_rep' contiene el valor total de caracteres repetidos en la contraseña
    if car_rep >= 3: punt -=1   #Puntuamos segun los criterios
    elif car_rep <= 1: punt +=1

    #Variedad de caracteres
    normales = len([letra for letra in contra if letra.islower()])
    if all(valor == 0 for valor in [num, simbolos]): punt -= 1  #Puntuamos segun los criterios
    elif all(valor >= 1 for valor in [num, simbolos]) and (normales >= 1 or mayus >= 1): punt += 1
    
    if punt <= -3: return " débil"
    elif -2 <= punt <= 2: return " segura"
    elif punt >= 3: return " muy segura"
    
    return punt #Valor final de seguridad de contraseña

def seguridad_pssw(*args):
    #Creamos la cadena con el nivel de seguridad de la contraseña
    cadena = "Contraseña"
    cadena += puntuacion(usuario.password.get())
    #Eliminamos la información vieja de la pantalla y recargamos la nueva información
    global seguridad_label
    if seguridad_label: #Comprobamos si existe 'seguridad_label'
        seguridad_label.destroy()
    #Mostramos la nueva informacion de seguridad de contraseña
    seguridad_label = tk.Label(ventana, text=cadena, fg="red")
    seguridad_label.place(relx=0.72, rely=0.3, relwidth=0.22, relheight=0.05)
    #Almacenamos si la contraseña es apta o no True/False en la instancia usuario
    if cadena == "Contraseña segura" or cadena == "Contraseña muy segura":
        usuario.seguridad_contra = True
    else: usuario.seguridad_contra = False

def completar_registro():
    #Completamos los datos antes de enviarlos para que tengan un formato correcto
    usuario.nombre = usuario.nombre.get()
    usuario.password = usuario.password.get()
    #Enviamos los nuevos datos al archivo de datos
    add_arch("Datos/base_datos.txt")
    #Releemos los datos para que consten los nuevos datos en el login
    global users_list
    users_list = leer_arch("Datos/base_datos.txt")
    #Cambiamos a la pantalla de login
    messagebox.showinfo(message="Registro completado correctamente")
    change_screen(0)

def compr_registro():  #Comprueba si el registro se puede efectuar correctamente
    #Comprobamos si al menos un check fue puslado..
    c1 = check1.estado.get()
    c2 = check2.estado.get()
    if c1 == 1 or c2 == 1:
        #Comprobamos si los campos están completos
        nombre = usuario.nombre.get()
        contraseña = usuario.password.get()
        if not (nombre == "" or contraseña == ""):
            #Comprobamos que el nombre de usuario no exista
            encontrado = compr_user()   #compr_user devuelve un array [True/False(si lo encuentra o no), indice de donde está en el arreglo de usuarios de datos]
            if encontrado[0] == False:
                #Comprobamos si la contraseña es segura
                if usuario.seguridad_contra == True:
                    #Almacenamos el valor del checkbox marcado
                    if c1 == 1: usuario.premium = 1
                    else: usuario.premium = 0
                    #Completamos el registro
                    completar_registro()
                
                
                else: messagebox.showerror("Security error", "La contraseña es demasiado débil, el registro no se puede completar.")
            else: messagebox.showerror("User already exists error", "El nombre de usuario ya existe, prueba con otro.")
        else: messagebox.showerror("User/password empty error", "Falta algún campo por rellenar, el registro no se puede completar.")
    else: messagebox.showerror("Checkbox error", "Falta algún campo por rellenar, el registro no se puede completar.")

#Leemos los arcihvos y almacenamos los datos
users_list = leer_arch("Datos/base_datos.txt")
stock_list = leer_arch("Datos/stock_libros.txt")

#Creamos el perfil del usuario vacio, los checkbuttons vacios
usuario = user()
check1 = checkbutton()
check2 = checkbutton()
seguridad_pssw_texto = ""

#Lanzamos la interfaz
change_screen(0)
ventana.mainloop()