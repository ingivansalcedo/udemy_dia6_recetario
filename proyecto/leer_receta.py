from pathlib import Path
from os import system
from funciones_locales.funciones import *

#Devuelve una lista con las opciones que el usuario tiene disponible a seleccionar.
def opcionesCorrectas(lista,n):
    opcioncorrecta = []
    for op in range(lista-n):
        opcioncorrecta.append(str(op+1))
    return opcioncorrecta

def generar_menu_recetas():
    opcion = None
    ruta = ruta_acceso()
    categorias = ListarCategorias(ruta)
    numero_opciones_categoria = len(categorias)

    # Loop while para listar las subcarpetas y recetas de la categoría seleccionada
      
    # print (numero_opciones_categoria)
    # print(len(opcionesCorrectas(numero_opciones_categoria,0)))

    while opcion != str(len(opcionesCorrectas(numero_opciones_categoria,0))):
        imprimir_menu_opciones(categorias)
        opcion = input("\nSeleccione una opción: ")
        #Funcion para imprimir lista de recetas de la carpeta seleccionada y 
        
        if opcion == str(len(opcionesCorrectas(numero_opciones_categoria,1))):
            print("Regresar al menu principal")
            input("")
            system('cls')
        elif opcion == str(len(opcionesCorrectas(numero_opciones_categoria,0))):
            print ("Hasta luego...")
        elif opcion in opcionesCorrectas(numero_opciones_categoria,2):
            ruta_categoria_seleccionada = Path(ruta, categorias[opcion])
            recetas = ListarRecetas(ruta_categoria_seleccionada)
            print (f"Estas son las recetas que tiene la categoría {ruta_categoria_seleccionada.name.upper()}")
            imprimir_menu_opciones(recetas)
            opcion = input("\nSeleccione una opción: ")
            numero_opciones_recetas = len(recetas)
            if opcion in opcionesCorrectas(numero_opciones_recetas,0):
                leerReceta(ruta_categoria_seleccionada,recetas[opcion])
            else:
                print ("Opción incorrecta")
                
            input("")
            system('cls')
        else:
            print ("Opcion Incorrecta")
            input("")
            system('cls')