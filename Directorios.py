# import os

''' Mostrar la ruta'''
# ruta = os.getcwd()

''' Cambiar de directorio'''
# ruta = os.chdir('/home/sistemas/Alternativo')
# archivo = open('Otro_Archivo.txt')
# print(archivo.read())
# archivo.close()

''' Crear directorios'''
# ruta = os.makedirs('/home/sistemas/Alternativo/otra')

''' Obtener ruta (dirname) y nombre del archivo(s) (basename)'''
# ruta = '/home/sistemas/Documents/cursos/udemy/dia6_programaunrecetario/prueba.txt'
# elemento = os.path.basename(ruta)
# print(elemento) # prueba.txt

# elemento = os.path.dirname(ruta)
# print(elemento) # /home/sistemas/Documents/cursos/udemy/dia6_programaunrecetario 

# elemento = os.path.split(ruta)
# print(elemento) # ('/home/sistemas/Documents/cursos/udemy/dia6_programaunrecetario', 'prueba.txt')


''' Eliminar directorio '''
# ruta = os.rmdir('/home/sistemas/Alternativo/otra')
# print(ruta)

from pathlib import Path

carpeta = Path('/home/sistemas/Alternativo')
archivo = carpeta / 'Otro_Archivo.txt'

mi_archivo = open(archivo)
print (mi_archivo.read())