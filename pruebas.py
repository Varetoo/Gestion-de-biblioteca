class user:
    def __init__(self, nombre, contra, edad = None):
        self.__nombre = nombre
        self.contra = contra
        self.edad = edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, cadena):
        self.__nombre = cadena


print("HOLA")
usuario = user("Paco", "adowiha")


print(f"nombre: {usuario.nombre}, contraseña: {usuario.contra}, edad:{usuario.edad}")


usuario.nombre = "hola"



print(f"nombre: {usuario.nombre}, contraseña: {usuario.contra}, edad:{usuario.edad}")