from pathlib import Path
from os import system
from funciones_locales.funciones import *
from leer_receta import LeerRecetas


def saludo_bienvenida():
    print ('Bienvenid@ al administrador de Recetas')
    print (f"Ruta de acceso a sus recetas: {ruta_acceso()}")
    print (f"Cantidad de recetas: {numero_recetas(ruta_acceso())}")
    print ("Seleccione alguna de las siguientes opciones:\n")

def menu(opcion):
    match opcion:
        case '1':
            LeerRecetas()
        case '2':
            print("Opcion 2")
        case '3':
            print("Opcion 3")
        case '4':
            print("Opcion 4")
        case '5':
            print("Opcion 5")
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
        system('cls')

if __name__ == '__main__':
    generar_menu_principal()