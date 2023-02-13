from pathlib import Path
from os import system
from funciones_locales.funciones import *
from leer_receta import LeerRecetas
from crear_receta import CrearReceta
from crear_categoria import CrearCategoria
from eliminar_categoria import EliminarCategoria
from eliminar_receta import EliminarReceta


def saludo_bienvenida():
    print ('Bienvenid@ al administrador de Recetas')
    print (f"Ruta de acceso a sus recetas: {ruta_acceso()}")
    print (f"Esta actual: {Path.cwd()}")
    print (f"Cantidad de recetas: {numero_recetas(ruta_acceso())}")
    print ("Seleccione alguna de las siguientes opciones:\n")

def menu(opcion):
    match opcion:
        case '1':
            LeerRecetas()
        case '2':
            CrearReceta()
        case '3':
            CrearCategoria()
        case '4':
            EliminarReceta()
        case '5':
            EliminarCategoria()
        case '6':
            print("Opcion Salir")
        case _:
            print("Opcion Incorrecta")

def lista_menu_principal():
    opciones = {
        '1': 'Leer Receta',
        '2': 'Crear Receta',
        '3': 'Crear Categoría',
        '4': 'Eliminar Receta',
        '5': 'Eliminar Categoría',
        '6': 'Salir'
    }

    imprimir_menu_opciones(opciones)

def generar_menu_principal():
    opcion = None
    while opcion != '6':
        saludo_bienvenida()
        lista_menu_principal()
        opcion = input("\nSeleccione una opción: ")
        menu(opcion)
        LimpiarPantalla()

if __name__ == '__main__':
    generar_menu_principal()