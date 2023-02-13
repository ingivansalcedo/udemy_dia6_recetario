from pathlib import Path
from os import system
import os
from funciones_locales.funciones import *

#Funcion para crear archivo (receta) en la categoría seleccionada
def CrearRecetaCategoria(ruta, nombre_receta, contenido_receta):
    os.chdir(ruta)
    nombre_receta = nombre_receta + '.txt'
    archivo = open(nombre_receta,'w') 
    for l in contenido_receta:
        archivo.writelines(l + '\n')
    archivo.close

def CrearReceta():
    LimpiarPantalla()
    print ("\n CATEGORIAS \n")
    opcion = None
    ruta = ruta_acceso()
    categorias = ListarCategorias(ruta)
    numero_opciones_categoria = len(categorias)

    while opcion != str(len(opcionesCorrectas(numero_opciones_categoria,0))):

        imprimir_menu_opciones(categorias)
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == str(len(opcionesCorrectas(numero_opciones_categoria,0))):
            LimpiarPantalla()
        elif opcion in opcionesCorrectas(numero_opciones_categoria,1):
            ruta_categoria_seleccionada = Path(ruta, categorias[opcion])
            nombre_receta = input ("Ingrese el nombre de su receta: ")
            contenido_receta = []
            print ("Escriba el contenido de su receta. (Dos enter seguidos para guardar el contenido)")
            while True:
                entrada = input(">>> ")
                if entrada.strip(): #si contiene algo es True, de lo contrario False
                    contenido_receta.append(entrada) #agregamos en caso contenga algo
                else:
                    break #detenemos el ciclo for
            CrearRecetaCategoria(ruta_categoria_seleccionada, nombre_receta, contenido_receta)
            print ("Receta creada correctamente.")
            input("")
            break

#CrearReceta()