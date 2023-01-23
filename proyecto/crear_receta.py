from pathlib import Path
from os import system
from funciones_locales.funciones import *

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
            contenido_receta = input ("Ingrese el contenido de su receta: ")
            print (ruta_categoria_seleccionada)


#CrearReceta()

datos = []
while True:
    entrada = input(">>> ")
    if entrada.strip(): #si contiene algo es True, de lo contrario False
        datos.append(entrada) #agregamos en caso contenga algo
    else:
        break #detenemos el ciclo for
#unimos todo mediante un salto de línea
print("\n".join(datos))