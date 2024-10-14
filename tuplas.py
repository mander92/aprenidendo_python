print('*** Manejo de tuplas ***')
nombres = ('Karla', 'Juan', 'Laura')

print(nombres)

#Creamos una tuple heterogénea
tupla_heterogenea = 100, True, 'Ivonne',

print(tupla_heterogenea)

#Recorrer los elementos de una tupla

for nombre in nombres:
    pass
 #   print(nombre)

numeros = (100,200,300,400,500)
print(numeros[0]) #Para acceder al elemento en una tupla usamos [indice]

print(numeros[-1]) #Se recupera el ultimo elemento de la tupla. Se puede recorrer de esta manera el indice de dercha a izquierda.
numeros_a_buscar = 200
if numeros_a_buscar in numeros:
    print(f'El número a buscar existe en la tupla: {numeros_a_buscar}')
else:
    print(f'El número a buscar no se encuentra en la tupla: {numeros_a_buscar}')

