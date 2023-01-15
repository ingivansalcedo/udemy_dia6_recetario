from pathlib import Path

def saludo_bienvenida():
    return ('Bienvenid@ al administrador de Recetas')

def ruta_acceso():
    home = Path.home()
    carpeta = 'Recetas'
    ruta = Path(home,carpeta)
    return ruta

print (saludo_bienvenida())
print (f"Ruta de acceso: {ruta_acceso()}")
print ("Seleccione alguna de las siguientes opciones: ")

