class user:
    def __init__(self, nombre, contra, edad = None):
        self.nombre = nombre
        self.contra = contra
        self.edad = edad


print("HOLA")
usuario = user("Paco", "adowiha")


print(f"nombre: {usuario.nombre}, contraseña: {usuario.contra}, edad:{usuario.edad}")