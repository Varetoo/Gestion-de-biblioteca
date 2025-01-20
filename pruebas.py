cadena = []
try:
    with open("Datos/stock_libros.txt", "r", encoding="utf-8") as archivo:
        for i, linea in enumerate(archivo):
            linea = linea.strip("\n")
            linea += f"{i+1}\n"
            cadena.append(linea)
        
except(FileNotFoundError):
    print("error")
try:
    with open("Datos/stock_libros.txt", "w", encoding="utf-8") as archivo:
        for elemento in cadena:
            archivo.write(elemento)
        
except(FileNotFoundError):
    print("error")


print(cadena)