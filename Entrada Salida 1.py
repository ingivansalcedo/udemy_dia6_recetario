mi_archivo = open('prueba.txt')


################################################

# Metodo read() para leer todoo el archivo
# print(mi_archivo.read())


################################################
# Metodo para leer linea por linea del archivo
# El metodo rstrip sirve para quitar el salto de linea

#una_linea = mi_archivo.readline()
#print(una_linea)
#una_linea = mi_archivo.readline()
#print(una_linea.rstrip())
#una_linea = mi_archivo.readline()
#print(una_linea)
################################################

#for l in mi_archivo:
#    print("Aqui dice: " + l)

################################################

todas = mi_archivo.readlines()
todas = todas.pop()
print(todas)

mi_archivo.close()