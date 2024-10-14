print('*** Dictionary in python ***')
#Un diccionario (objeto) almacena suss elementos en forma de llave-valor (key/value)
diccionario = {
    'nombre': 'Mario',
    'apellido': 'Cervantes',
    'edad': 27, #No se permites duplicar elementos si esto es asi se guardara el ultimo elemento siempre 
    'edad': 28
}

print(diccionario)


#Acceder al elementos. Los elementos se acceden con corchetes []
print(f'Nombre: {diccionario["nombre"]}')#dentro de un string con commillas simples o doble se debe utilizar la contaria
print(f' Edad: {diccionario.get("edad")}')

print(f'El largo del diccionariuo es: {len(diccionario)}')

#Agregar un nuevo elemento 
diccionario['telefono'] = 644418548
print(f'Diccionario modificado: {diccionario}')

# Obtener una lista de las llaves del diccionario
print(f'Lista de las llaves del diccionario: {diccionario.keys()}')

#Obtner una lista de los valores del diccionario
print(f'Lista de valores del diccionario: {diccionario.values()}')

#Obtener los elemntos del diccionario
print(f'Lista como elementos en forma de tupla: {diccionario.items()}')

#Revisar si existe llave dentro del diccionario 
llave_a_buscar = 'nombre'
if llave_a_buscar in diccionario:
    print(f'La llave {llave_a_buscar} Sí existe ene diccionario')
else: 
    print(f'La llave {llave_a_buscar} No existe ene el diccionario')

#Si queremos modificar el valor de una llave 
diccionario['nombre'] = 'Eduardo'

print(diccionario)#El nuevo diccionario incluye este valor modificado 

#Eliminar un valor del diccionario 
diccionario.pop('edad')

print(diccionario) #En esta linea ya no se incluye el valor eliminado 

#Recorrero las llavers de un dic
for llave in diccionario.key():
    print(llave, end=' - ')

print('**********************')
#Recorrer los valores de un diccionario
for llave in diccionario.values():
    print(llave, end=' - ')

#Recorrer los elementos de un dic pero como una tupla 
for llave, valor in diccionario.items():
    print(f'Llave: {llave}, Valor: {valor}')

#Limpiar el diccionario 
diccionario.clear() #todos sus valores se han eliminado en esta linea 


