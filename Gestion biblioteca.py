#============================== IMPORTS ==============================
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#============================== CLASES ==============================
class dato:    #Datos STOCK
    def __init__(self, nombre = None, clave = None, state = None):
        self.nombre = nombre
        self.clave = clave
        self.state = state

    def valores_no_none(self):
        lista = []
        if self.nombre != None: lista.append(self.nombre)
        if self.clave != None: lista.append(self.clave)
        if self.state != None: lista.append(self.state)
        return lista

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

#============================== BASES DE DATOS ==============================
#Funciones
def leer_arch(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as base_datos:
            lista_instancias = []
            for linea in base_datos:
                linea = linea.strip().split("    ", maxsplit=3)
                lista_instancias.append(dato(linea[0], linea[1], linea[2]))
        return lista_instancias
        

    except(FileExistsError,FileNotFoundError):
        messagebox.showerror("Error archivo", f"Hay un error con el archivo de datos {nombre_archivo}")

def leer_arch_prestamos(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as base_datos:
            lista_instancias = []   #Lista de instancias de tipo dato que recoje tantos datos como lineas tenga el archivo
            for linea in base_datos:
                linea = linea.strip().split("    ", maxsplit=7)
                libros_prestados = []
                for i, elemento in enumerate(linea):
                    if i != 0:
                        libros_prestados.append(elemento)
                lista_instancias.append(dato(linea[0], libros_prestados))
        
        return lista_instancias
        

    except(FileExistsError,FileNotFoundError):
        messagebox.showerror("Error archivo", f"Hay un error con el archivo de datos {nombre_archivo}")

def add_arch(nombre_archivo):
    try:
        with open(nombre_archivo, "a", encoding="utf-8") as base_datos:
            base_datos.write(f"\n{usuario.nombre}    {usuario.password}    {usuario.premium}")

    except(FileExistsError,FileNotFoundError):
        messagebox.showerror("Error archivo", f"Hay un error con el archivo de datos {nombre_archivo}")

def leer_stock_y_prestamos():
    global stock_list
    stock_list = leer_arch("Datos/stock_libros.txt")
    global prestamos_list
    prestamos_list = leer_arch_prestamos("Datos/prestamos.txt")
    pass

def escribir_arch(nombre_archivo, lista):
    try:
        cadena = ""
        for i, dato in enumerate(lista):
            lista_aux = dato.valores_no_none()    #Almacena en lista_aux todos los valores validos de dato
            for indx, lista_aux2 in enumerate(lista_aux):
                if type(lista_aux2) == list:
                    for elemento in lista_aux2:
                        if indx != 0: cadena += "    "+str(elemento)
                        else: cadena += str(elemento)
                else:
                    if indx != 0: cadena += "    "+str(lista_aux2)
                    else: cadena += str(lista_aux2)
            if i != len(lista)-1:
                cadena += "\n"
        with open(nombre_archivo, "w", encoding="utf-8") as base_datos:
            base_datos.write(cadena)
    
    except(FileExistsError,FileNotFoundError):
        messagebox.showerror("Error archivo", f"Hay un error con el archivo de datos {nombre_archivo}")

#============================== INTERFAZ ==============================
# Confiugración inicial de la ventana
ventana = tk.Tk()
ventana.geometry("600x400")
ventana.resizable(False, False)  # No permite cambiar tamaño de la ventana

# Funcion principal
def change_screen(id = 0):  #Funcion que se encarga de eliminar el contenido que hay en la pantalla actual y luego llama a la funcion correspondiente al id dado
    #Eliminamos el contenido de la pantalla anterior
    for widget in ventana.winfo_children():
        widget.destroy()
    if   id == 0: screen0()   #SING IN 
    elif id == 1: screen1()   #SING UP
    elif id == 2: screen2()   #MAIN
    elif id == 3: screen3()   #SOLICITAR LIBRO
    elif id == 4: screen4()   #DEVOLICIONES

# Funciones extra
def titulo(name="tittle sin modificar"):
    #Tittle
    ventana.title(name)
    # Título de la ventana
    titulo = tk.Label(ventana, text="Gestión de biblioteca", font=("", 24, "underline"))
    titulo.place(relx=0.02, rely=0.05, relwidth=0.9, relheight=0.1)

def label_inicio():
    # Usuario
    usuario_label = tk.Label(ventana, text=usuario.nombre, bg="red")
    usuario_label.place(relx=0.25, rely=0.23)
    # Premium
    if usuario.premium == True:
        premium_label = tk.Label(ventana, text="*Premium*", bg="red")
        premium_label.place(relx=0.55, rely=0.23)

def devoluciones_disponibles():
    # Variable IntVar para controlar los Checkbuttons (solo uno seleccionado)
    variable_checkbutton = tk.IntVar()
    variable_checkbutton.set(-1)    #Ningún Checkbutton seleccionado inicialmente
    for indice, titulo in enumerate(usuario.prestamos_activos):
        #Label con el titulo del libro
        tk.Label(ventana, text=titulo).place(relx=0.325, rely=0.37+(0.07*indice))
        #Creamos los checkbuttons de manera dinámica
        checkbutton_dinamico = tk.Checkbutton(
            ventana,
            variable= variable_checkbutton,
            onvalue= indice,  # Este Checkbutton se selecciona cuando seleccion == indice
            offvalue= -1     # Cuando se deselecciona, seleccion vuelve a -1
        )
        checkbutton_dinamico.place(relx=0.275, rely=0.37+(0.07*indice))
    # Boton para aceptar
    aceptar_button = tk.Button(ventana, text="Aceptar", command=lambda: pulsado_aceptar_devolucion(variable_checkbutton))
    aceptar_button.place(relx=0.275, rely=0.37+(0.07*(indice+1)))

def actualizar_scroll(event):   # Ajustar el tamaño del canvas automáticamente al contenido del frame
    canvas.configure(scrollregion=canvas.bbox("all"))

# Screens
def screen0():  #Sing in
    # Título de la ventana
    titulo("Sing in")

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
    boton_aceptar = tk.Button(ventana, text="Aceptar", command=lambda: comprobar_contra(comprobar_user(consolidar_credenciales_usuario())))
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
    # Título de la ventana
    titulo("Sing up")
    
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
    boton_aceptar = tk.Button(ventana, text="Aceptar", command= lambda: comprobar_registro(consolidar_credenciales_usuario()))
    boton_aceptar.place(relx=0.45, rely=0.60, relwidth=0.25, relheight=0.05)
    
    #Mandamos los valores a class: user
    usuario.nombre = user_entry
    usuario.password = password_entry

def screen2():  #Main
    # Leemos los archivos de stock y prestamos
    leer_stock_y_prestamos()
    comprobar_prestamos()
    # Título de la ventana
    titulo("Main")
    #Usuario y premium
    label_inicio()
    # Libros en posesion
    libros_label = tk.Label(ventana, text=f"Libros en posesión: {len(usuario.prestamos_activos)}", bg="red")
    libros_label.place(relx=0.25, rely=0.30)
    #Prestamos restantes
    prestamos_label = tk.Label(ventana, text=f"Prestamos restantes: {usuario.prestamos_restantes}", bg="red")
    prestamos_label.place(relx=0.25, rely=0.37)
    # Boton VER
    ver_button = tk.Button(ventana, text="Ver", command=pulsado_ver_button)
    ver_button.place(relx=0.55, rely=0.30)
    # Boton DEVOLVER LIBRO
    devolver_libro_button = tk.Button(ventana, text="Devolver libro", command=pulsado_devolver_button)
    devolver_libro_button.place(relx=0.62, rely=0.30)
    # Boton PEDIR PRESTADO
    pedir_prestado_button = tk.Button(ventana, text="Pedir prestado", command=pulsado_pedir_button)
    pedir_prestado_button.place(relx=0.55, rely=0.37, relwidth=0.21)

def screen3():  #Solicitar libro
    # Título de la ventana
    titulo("Solicitar libro")
    #Usuario y premium
    label_inicio()
    #Label informacion extra
    info_label = tk.Label(ventana, text="Seleccione el libro que desea pedir prestado", font=("", 12, "bold"), bg="gray")
    info_label.place(relx=0.25, rely=0.30)
    #Buscador
    buscador_label = tk.Label(ventana, text="-- Futuro Buscador --", bg="green")
    buscador_label.place(relx=0.25, rely=0.37)
    
    # --- RECUADRO ---
    #Canvas y scrollbar
    global canvas
    canvas = tk.Canvas(ventana, background="lightgrey")
    scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    #Colocamos el canvas y el scrollbar en la ventana
    canvas.place(relx=0.25, rely=0.44, relwidth=0.56, relheight=0.4)
    scrollbar.place(relx=0.8, rely=0.44, relwidth=0.02, relheight=0.4)
    #Creamos el frame de dentro del canvas
    frame_contenido = tk.Frame(canvas, bg="lightgrey")
    canvas.create_window((0, 0), window=frame_contenido, anchor="nw")
    #Bindeamos el scroll con el frame
    frame_contenido.bind("<Configure>", actualizar_scroll)
    #Lista para almacenar el estado de los checkbuttons
    lista_estado_checks = []
    #Agregamos todos los titulos en forma de label
    for elemento in stock_list:
        #Variable para el checkbutton
        var = tk.BooleanVar()
        lista_estado_checks.append(var)
        
        # Creamos un contenedor para el Checkbutton y el Label
        item_frame = tk.Frame(frame_contenido, bg="lightgrey")
        item_frame.pack(fill="x", pady=2)  # Separación vertical entre elementos

        # Creamos el Checkbutton
        check = tk.Checkbutton(item_frame, variable=var, bg="lightgrey")
        check.pack(side="left", padx=5)  # Alineado a la izquierda con margen

        # Creamos el Label
        label = tk.Label(item_frame, text=(elemento.nombre) + ", de " + (elemento.clave), bg="lightgrey")
        label.pack(side="left")  # Alineado a la derecha del Checkbutton
    #Guardamos la lista con los checks en una clase para poder tener acceso a ella
    check_lista.estado = lista_estado_checks
    
    #Boton aceptar pedir
    aceptar_button = tk.Button(ventana, text="Aceptar", command=pulsado_aceptar_pedir)
    aceptar_button.place(relx=0.25, rely=0.86)

def screen4():  #Devoluciones
    # Título de la ventana
    titulo("Devoluciones")
    #Usuario y premium
    label_inicio()
    #Label informacion extra
    info_label = tk.Label(ventana, text="Seleccione el libro que desea devolver", font=("", 12, "bold"), bg="gray")
    info_label.place(relx=0.25, rely=0.30)
    # Muestra los libros disponibles para devolucion con checkbuttons
    devoluciones_disponibles()

#============================== CODIGO ==============================
#Login y registro
def checkbutton_no_iguales(ultimo): #Funcionalidad para que no se puedan pulsar los dos checks a la vez
    c1 = check1.estado.get()
    c2 = check2.estado.get()
    if c1 == c2:
        if ultimo == 1: #El ultimo check en activarse fue el 1
            check2.estado.set(0)
        elif ultimo == 2: #El ultimo check en activarse fue el 2
            check1.estado.set(0)

def comprobar_user(lista_para_comprobarobar):    #comprobarueba si el usuario existe en la base de datos
    #comprobarobamos si el usuario existe
    name = usuario.nombre
    for i, elemento in enumerate(lista_para_comprobarobar):
        if elemento.nombre.lower() == name.lower():
            encontrado = True   #El nombre está en la lista
            break
        encontrado = False
    return [encontrado,i]

def comprobar_prestamos():  # Rellena la informacion usuario.prestamos_activos y usuario.prestamos_restantes
    #comprobarobamos si el usuario se encuentra en la lista de prestamos activos
    lista = comprobar_user(prestamos_list)
    encontrado, i = lista[0], lista[1]
    # Prestamos activos predeterminados
    usuario.prestamos_activos = []
    if encontrado == True:  # Si el usuario se encuentra en la lista con prestamos
        usuario.prestamos_activos = prestamos_list[i].clave # Almacenamos en usuario.prestamos_activos el array con todos los titulos
    # La cantidad de prestamos disponibles para los usuarios premium son 6 y para los no premium son 3
    cantidad_predeterminada = 3
    if usuario.premium == True:
        cantidad_predeterminada += 3
    usuario.prestamos_restantes = cantidad_predeterminada-len(usuario.prestamos_activos)

def comprobar_contra(lista):    #Muestra por pantalla si el usuario existe y COMPLETA EL LOGIN si la contraseña coincide.   lista -> [encontrado, i] de la funcion comprobar_user
    encontrado = lista[0]
    i = lista[1]
    if encontrado == False: 
        messagebox.showerror("Error usuario", f"No se ha encontrado el nombre de usuario")
        change_screen(0)
    elif encontrado == True:    #Buscamos si la contraseña coincide
        contra = usuario.password
        if contra == users_list[i].clave:
            messagebox.showinfo("Login", "Login efectuado correctamente")
            #Completamos los datos antes de cambiar de pantalla para que tengan un formato correcto y no perderlos
            usuario.premium = int(users_list[i].state)
            leer_stock_y_prestamos()
            comprobar_prestamos()
            change_screen(2)
        else: 
            messagebox.showerror("Password error", "Contraseña incorrecta")
            change_screen(0)

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

def seguridad_pssw(*args):   #Introduce True/False en usuario.seguridad_contra segun la contraseña es apta o no para el registro
    #Creamos la cadena con el nivel de seguridad de la contraseña
    cadena = "Contraseña"
    cadena += puntuacion(usuario.password.get())
    #Eliminamos la información vieja de la pantalla y recargamos la nueva información
    global seguridad_label
    if seguridad_label: #comprobarobamos si existe 'seguridad_label'
        seguridad_label.destroy()
    #Mostramos la nueva informacion de seguridad de contraseña
    seguridad_label = tk.Label(ventana, text=cadena, fg="red")
    seguridad_label.place(relx=0.72, rely=0.3, relwidth=0.22, relheight=0.05)
    #Almacenamos si la contraseña es apta o no True/False en la instancia usuario
    if cadena == "Contraseña segura" or cadena == "Contraseña muy segura":
        usuario.seguridad_contra = True
    else: usuario.seguridad_contra = False

def consolidar_credenciales_usuario():
    usuario.nombre = usuario.nombre.get()
    usuario.password = usuario.password.get()
    return users_list

def comprobar_registro(*args):  #comprobarueba si el registro se puede efectuar correctamente
    c1 = check1.estado.get()
    c2 = check2.estado.get()
    #comprobarobamos si al menos un check fue puslado..
    if c1 == 1 or c2 == 1:
        #comprobarobamos si los campos están completos
        if not (usuario.nombre == "" or usuario.password == ""):
            #comprobarobamos que el nombre de usuario no exista
            encontrado = comprobar_user(users_list)   #comprobar_user devuelve un array [True/False(si lo encuentra o no), indice de donde está en el arreglo de usuarios de datos]
            if encontrado[0] == False:
                #comprobarobamos si la contraseña es segura
                if usuario.seguridad_contra == True:
                    #Almacenamos el valor del checkbox marcado
                    if c1 == 1: usuario.premium = 1
                    else: usuario.premium = 0
                    #Completamos el registro
                    completar_registro()
                else:
                    messagebox.showerror("Security error", "La contraseña es demasiado débil, el registro no se puede completar.")
                    change_screen(1)
            else:
                messagebox.showerror("User already exists error", "El nombre de usuario ya existe, prueba con otro.")
                change_screen(1)
        else:
            messagebox.showerror("User/password empty error", "Falta algún campo por rellenar, el registro no se puede completar.")
            change_screen(1)
    else:
        messagebox.showerror("Checkbox error", "Falta algún campo por rellenar, el registro no se puede completar.")
        change_screen(1)

def completar_registro():   #Añade los nuevos datos a la base de datos y vuelve a la pantalla de login
    #Enviamos los nuevos datos al archivo de datos
    add_arch("Datos/base_datos.txt")
    #Releemos los datos para que consten los nuevos datos en el login
    global users_list
    users_list = leer_arch("Datos/base_datos.txt")
    #Cambiamos a la pantalla de login
    messagebox.showinfo(message="Registro completado correctamente")
    change_screen(0)

#Pagina principal
def pulsado_ver_button():
    if len(usuario.prestamos_activos) > 0:
        lista = comprobar_user(prestamos_list)
        indice = lista[1]
        lista = prestamos_list[indice].clave
        texto = ""
        for titulo in lista:
            texto += titulo + "\n"
    else:
        texto = "No tienes prestamos activos"
    messagebox.showinfo("Libros prestados", texto)

def pulsado_pedir_button():
    if usuario.prestamos_restantes == 0:
        messagebox.showinfo("Pedir prestado", "No puedes pedir mas libros, devuelve alguno para poder continuar")
    else:
        change_screen(3)

def pulsado_devolver_button():
    if len(usuario.prestamos_activos) == 0:
        messagebox.showinfo("Devolver libro", "No tienes prestamos activos")
    else:
        change_screen(4)

#Devolver
def pulsado_aceptar_devolucion(indice):
    if indice.get() == -1:
        messagebox.showerror("Seleccion error", "Selecciona un libro para devolver")
    else:
        #Eliminamos el libro prestado
        for indice_prestamos_list ,usuario_prestamos in enumerate(prestamos_list):
            if usuario_prestamos.nombre == usuario.nombre:   #Buscamos en la lista de prestamos el usuario
                titulo_devuelto = prestamos_list[indice_prestamos_list].clave.pop(indice.get())   # Se elimina el valor en memoria que corresponde tanto a usuario.prestamos_activos como a este
                break
        #Renovamos los datos de las listas
        refresh_prestamos_list(indice_prestamos_list)
        refresh_stock_list(titulo_devuelto, 1)  #Sumamos 1 al stock
        #Cargamos los datos de las listas en los archivos
        escribir_arch("Datos/prestamos.txt", prestamos_list)
        escribir_arch("Datos/stock_libros.txt", stock_list)
        #Volvemos a la pagina principal
        change_screen(2)

def refresh_prestamos_list(indice_usuario):   # Verifica si el usuario de prestamos_list[indice] ya no tiene ningún libro asociado, si es asi se eliminará de la lista
    if len(prestamos_list[indice_usuario].clave) == 0:
        prestamos_list.pop(indice_usuario)#Eliminamos por completo al usuario de prestamos_list

def refresh_stock_list(titulo, num = 1):   #Suma 'num' a la cantidad de stock del 'titulo' correspondiente a la lista de stock
    for libro in stock_list:
        if libro.nombre == titulo:
            libro.state = int(libro.state)
            libro.state += num

#Pedir
def pulsado_aceptar_pedir():
    seleccionados_indices = [i for i, var in enumerate(check_lista.estado) if var.get()]
    if len(seleccionados_indices) > 1:
        messagebox.showerror("Prestamos sobrepasados", "Selecciona solo un prestamo por vez")
        change_screen(2)
    elif len(seleccionados_indices) == 0:
        messagebox.showerror("", "Selecciona algún libro para pedir prestado")
        change_screen(2)
    else:   #No hay ningun error
        indice = seleccionados_indices[0]
        #Comprobamos que haya stock del libro pedido
        if int(stock_list[indice].state) == 0:
            messagebox.showinfo("Out of stock", "Lo sentimos, actualmente no hay stock de este libro,\ntendrás que esperar a que alguien lo devuelva para poder alquilarlo")
            change_screen(2)
        else:
            # Restar 1 al stock del libro
            refresh_stock_list(stock_list[indice].nombre, -1)
            # Añadir el libro a la lista de prestamos
                #Comprobamos si el usuario ya está en la lista para añadirlo en su "apartado" o crear uno nuevo
            if len(usuario.prestamos_activos) > 0:
                for elemento in prestamos_list:
                    if elemento.nombre == usuario.nombre:
                        elemento.clave.append(stock_list[indice].nombre)
                        break
            else:   #Si el usuario no tiene prestamos activos..
                prestamos_list.append(dato(usuario.nombre, stock_list[indice].nombre))
            #Cargamos los datos de las listas en los archivos
            escribir_arch("Datos/prestamos.txt", prestamos_list)
            escribir_arch("Datos/stock_libros.txt", stock_list)
            change_screen(2)

#MAIN CODE
#Leemos los arcihvos y almacenamos los datos
users_list = leer_arch("Datos/base_datos.txt")

#Creamos el perfil del usuario vacio, los checkbuttons vacios
usuario = user()
check1 = checkbutton()
check2 = checkbutton()
check_lista = checkbutton()
seguridad_pssw_texto = ""

#Lanzamos la interfaz
change_screen(0)
ventana.mainloop()