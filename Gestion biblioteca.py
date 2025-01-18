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
#Global
nombre_arch_usuarios = "Datos/base_datos.txt"
nombre_arch_stock = "Datos/stock_libros.txt"

#Funciones
def leer_arch(nombre_archivo):
    try:
        with open(nombre_archivo, "r+", encoding="utf-8") as base_datos:
            lista = []
            for linea in base_datos:
                linea = linea.strip().split("    ", maxsplit=3)
                lista.append(dato(linea[0], linea[1], linea[2]))
        return lista
        

    except(FileExistsError,FileNotFoundError):
        messagebox.showerror("Error archivo", f"Hay un error con el archivo de datos {nombre_archivo}")


#Main
users_datos = leer_arch(nombre_arch_usuarios)
stock_datos = leer_arch(nombre_arch_stock)


#==================== CODIGO ====================
pass


#==================== INTERFAZ ====================

