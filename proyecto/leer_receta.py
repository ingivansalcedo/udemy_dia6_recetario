from pathlib import Path
from os import system
from funciones_locales.funciones import *

def LeerRecetas():
    LimpiarPantalla()
    opcion = None
    ruta = ruta_acceso()
    categorias = ListarCategorias(ruta)
    numero_opciones_categoria = len(categorias)

    # Loop while para listar las subcarpetas y recetas de la categoría seleccionada
      
    # print (numero_opciones_categoria)
    # print(len(opcionesCorrectas(numero_opciones_categoria,0)))

    while opcion != str(len(opcionesCorrectas(numero_opciones_categoria,0))):
        print ("\n CATEGORIA DE RECETAS \n")
        imprimir_menu_opciones(categorias)
        opcion = input("\nSeleccione una opción: ")
        #Funcion para imprimir lista de recetas de la carpeta seleccionada y 
        
        if opcion == str(len(opcionesCorrectas(numero_opciones_categoria,0))):
            LimpiarPantalla()
        elif opcion in opcionesCorrectas(numero_opciones_categoria,1):
            ruta_categoria_seleccionada = Path(ruta, categorias[opcion])
            recetas = ListarRecetas(ruta_categoria_seleccionada)
            if recetas == {} or len(recetas)==1:
                print ("Carpeta vacía")
                input("")
            else:
                LimpiarPantalla()
                print (f"Estas son las recetas que tiene la categoría {ruta_categoria_seleccionada.name.upper()}\n")
                imprimir_menu_opciones(recetas)
                opcion = input("\nSeleccione una opción: ")
                numero_opciones_recetas = len(recetas)
                if opcion in opcionesCorrectas(numero_opciones_recetas,0):
                    imprimirReceta(ruta_categoria_seleccionada,recetas[opcion])
                    input("")
                else:
                    print ("Opción incorrecta")
                    input("")
                    LimpiarPantalla()
        else:
            print ("Opcion Incorrecta")
            input("")
            LimpiarPantalla()
        
        LimpiarPantalla()