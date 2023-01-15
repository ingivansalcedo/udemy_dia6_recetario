from pathlib import Path


# base = Path.home()
# guia = Path(base, 'Documents','udemy','udemy_dia6_recetario','prueba.txt')
# guia2 = guia.with_name('prueba2.txt')
# print(guia)

''' Imprime el antecesor de la ruta, en este caso /home/sistemas/Documents/udemy/udemy_dia6_recetario '''
# print(guia.parent)

''' Enumerar los archivos '''
base = Path.home()
carpeta = Path('Documents','udemy','udemy_dia6_recetario')
ruta_completa = Path(base,carpeta)

print(ruta_completa)
# for txt in Path(ruta_completa).glob('*.txt'):
#     print (txt)

''' Ruta relativa'''
home = ruta_completa.relative_to(Path('/','home','sistemas'))
#documentos = ruta_completa.relative_to(Path('home','sistemas','Documents'))

print(home)
#print(documentos)
