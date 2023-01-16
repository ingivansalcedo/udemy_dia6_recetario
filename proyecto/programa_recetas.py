from pathlib import Path
from os import system

def saludo_bienvenida():
    print ('Bienvenid@ al administrador de Recetas')
    print (f"Ruta de acceso a sus recetas: {ruta_acceso()}")
    print (f"Cantidad de recetas: {numero_recetas(ruta_acceso())}")
    print ("Seleccione alguna de las siguientes opciones:\n")


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


def menu(opcion):
    match opcion:
        case '1':
            print("Opcion 1")
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

    imprimir_lista_menu_principal(opciones)

def imprimir_lista_menu_principal(opciones):
    for opcion, nombre_opcion in opciones.items():
        print (f"{opcion} -> {nombre_opcion}")

def generar_menu():
    opcion = None
    while opcion != '6':
        saludo_bienvenida()
        lista_menu_principal()
        opcion = input("\nSeleccione una opción: ")
        menu(opcion)
        input("")
        system('cls')

if __name__ == '__main__':
    generar_menu()