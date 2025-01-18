#IMPORTS
import tkinter as tk
from tkinter import messagebox


#CLASES
class datoS:    #Datos STOCK
    def __init__(self, nombre, clave):
        self.nombre = nombre
        self.clave = clave

class datoU(datoS): #Datos USUARIO
    def __init__(self, nombre, clave, premium):
        super().__init__(nombre, clave)
        self.premium = premium

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


#BASES DE DATOS
nombre_base_usuarios = "base_datos.txt"
nombre_base_stock = "stock_libros.txt"
def leer_arch():
    try:
        with open(nombre_base_usuarios, "r+", encoding="utf-8") as base_datos:
            users_datos = []
            for linea in base_datos:
                nombre, pssw, prem = linea.strip().split("    ", maxsplit=3)
                users_datos.append(datoU(nombre, pssw, prem))
        return users_datos
        

    except(FileExistsError,FileNotFoundError):
        messagebox.showerror("Error archivo", "Hay un error con los archivos de datos .txt")


#CODIGO
pass

#INTERFAZ

