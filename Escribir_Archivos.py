''' Este modo de apertura ('a') solo permite leer el archivo. '''
# archivo = open('prueba.txt','r') 

''' 
 Este modo de apertura ('w') permite modificar el archivo:
 - Lo reescribe si el archivo exite y/o
 - Crea un archivo nuevo con el nombre indicado
'''
# archivo = open('prueba1.txt','w') 
# archivo.write('Soy el nuevo texto\n')
# archivo.write('Hola Mundo.\n')
# archivo.write('''Ahora con saltos
#         de linea
# de esta manera.\n''')
# archivo.writelines(['hola','mundo','aqui','estoy','\n'])

# lista = ['hola','mundo','aqui','estoy']
# for l in lista:
#     archivo.writelines(l + '\n')

# archivo.close()


''' 
Este modo de apertura 'a' permite 
 - Modificar y/o crear el archivo 
con la caracteristicas que se posiciona en la ultima línea sin reescribirlo'''

archivo = open('prueba2.txt','a') 
archivo.write('Bienvenido')
archivo.close()

archivo = open('prueba2.txt','r')
print (archivo.read())
archivo.close()