from pathlib import Path

def saludo_bienvenida():
    return ('Bienvenid@ al administrador de Recetas')

def ruta_acceso():
    home = Path.home()
    carpeta = 'Recetas'
    ruta = Path(home,carpeta)
    return ruta

def numero_recetas(ruta):
    recetas = 0
    for txt in Path(ruta).glob('**/*.txt'):
        recetas += 1
    return recetas

ruta = ruta_acceso()
opcion = 1

print (saludo_bienvenida())
print (f"Ruta de acceso a sus recetas: {ruta}")
print (f"Cantidad de recetas: {numero_recetas(ruta)}")
print ("Seleccione alguna de las siguientes opciones: ")