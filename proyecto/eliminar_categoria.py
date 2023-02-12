from pathlib import Path
from os import system
import shutil
from funciones_locales.funciones import *

def EliminarCategoria():
    LimpiarPantalla()
    ruta = ruta_acceso()
    opcion = None
    categorias = ListarCategorias(ruta)
    numero_opciones_categoria = len(categorias)

    while opcion != str(len(opcionesCorrectas(numero_opciones_categoria,0))):
        categorias = ListarCategorias(ruta)
        numero_opciones_categoria = len(categorias)
        LimpiarPantalla()
        print ("\n CATEGORIA DE RECETAS \n")
        imprimir_menu_opciones(categorias)
        opcion = input("\nSeleccione una opción: ")

        if opcion == str(len(opcionesCorrectas(numero_opciones_categoria,0))):
            LimpiarPantalla()
        elif opcion in opcionesCorrectas(numero_opciones_categoria,1):
            ruta_completa = Path(ruta,categorias[opcion])
            shutil.rmtree(ruta_completa)
        else:
            print("Opción incorrecta")
            input("") 