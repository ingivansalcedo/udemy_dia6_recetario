from pathlib import Path
from os import system
from sysconfig import sys

def PlataformaSistemaOperativo():
    if sys.platform.startswith('win32'):
        return ('Windows')
    elif sys.platform.startswith('linux'):
        return ('Linux')

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

def imprimir_menu_opciones(opciones):
    for opcion, nombre_opcion in opciones.items():
        print (f"{opcion} -> {nombre_opcion}")

def ListarRecetas(ruta):
    contar = 0
    lista_recetas = {}
    for txt in Path(ruta).glob('**/*.txt'):
        contar += 1
        lista_recetas[str(contar)] = txt.name
    return lista_recetas

def ListarCategorias(ruta):
    lista_carpetas = {}
    contar = 0
    for carpeta in ruta.iterdir():
        if carpeta.is_dir():
            contar +=1
            lista_carpetas[str(contar)] = carpeta.name
    lista_carpetas[str(contar+1)] = 'Regresar al menú anterior'
    return lista_carpetas

def imprimirReceta(ruta, nombre_receta):
    ruta_completa = Path(ruta,nombre_receta)
    print(ruta_completa.read_text())

def LimpiarPantalla():
    if PlataformaSistemaOperativo() == 'Windows':
        return system('cls')
    else:
        return system('clear') 