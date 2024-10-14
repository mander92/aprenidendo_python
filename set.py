print('*** Manejo de set en python ***')
#Un set es un conjunto de datos NO ordenados y no se pueden repetir sus elementos

conjunto = {'Karla', 100, 'Laura', True, 'karla'}
print(conjunto)

#conjunto[0] = 'karla' arroja error, no se pueden modificar los elementos

for item in conjunto:
    pass
    #print(item, end=' ')

numero_a_buscar = 1000
if numero_a_buscar in conjunto:
    print('Existe')
else:
    print('vete a la playa')

#Eliminar un elemento 
conjunto.remove(100)

#Añadir un elemento
conjunto.add(600)