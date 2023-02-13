from pathlib import Path
from os import system
import os
from funciones_locales.funciones import *

def EliminarReceta():
    LimpiarPantalla()
    opcion = None
    ruta = ruta_acceso()
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
            ruta_categoria_seleccionada = Path(ruta, categorias[opcion])
            os.chdir(ruta_categoria_seleccionada)
            recetas = ListarRecetas(ruta_categoria_seleccionada)
            #La siguiente condicional controla cuando en la carpeta no exitan recetas 
            if recetas == {} or len(recetas)==1:
                print ("Carpeta vacía")
                input("")
            else:
                LimpiarPantalla()
                print (f"ELIMINAR RECETAS")
                print (f"Estas son las recetas que tiene la categoría {ruta_categoria_seleccionada.name.upper()}\n")
                imprimir_menu_opciones(recetas)
                opcion = input("\nSeleccione una opción: ")
                numero_opciones_recetas = len(recetas)
                if opcion == str(len(opcionesCorrectas(numero_opciones_recetas,0))):
                    EliminarReceta()
                elif opcion in opcionesCorrectas(numero_opciones_recetas,1):
                    os.remove(recetas[opcion])
                    print ("Receta eliminada correctamente")
                    input("")
                else:
                    print ("Opción incorrecta")
                    input("")
                    LimpiarPantalla()
                

#EliminarReceta()