from tkinter import messagebox

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

usuario = user("warrel", "aoih123@#21", 1)

def add_arch(nombre_archivo):
    try:
        with open(nombre_archivo, "a", encoding="utf-8") as base_datos:
            base_datos.write(f"\n{usuario.nombre}    {usuario.password}    {usuario.premium}")
        
        
    except(FileExistsError,FileNotFoundError):
        messagebox.showerror("Error archivo", f"Hay un error con el archivo de datos {nombre_archivo}")

add_arch("Datos/base_datos.txt")