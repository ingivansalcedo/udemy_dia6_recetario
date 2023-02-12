from pathlib import Path
from os import system
from funciones_locales.funciones import *

def CrearCategoria():
    LimpiarPantalla()
    ruta = ruta_acceso()
    nombre_categoria = input("Ingrese el nombre de la categoria: ")
    ruta_completa = Path(ruta, nombre_categoria)
    ruta_completa.mkdir()
