print('*** Funciones en Python ***')

#Definir una función 
def saludar():
    print('Hola mundo')

saludar() #Llamamos a la función 

#Definir uina función con parámetros o argumentos 
def saludarConNombre(nombre):
    print(f'Hola {nombre}')
    return 'terminado'

saludarConNombre('Mario')

valor_del_return = saludarConNombre('Luis')
print(valor_del_return)#El valor que retorna la función se guarda en esta variable