print('*** Listas en Python ***')

nombres = ['Karla', 'Laura', 'Juan']

print(f'Listas de nombres: {nombres}')

#Listas heterogénea o multiples tipos de datos

lista_heterogenea = [100, True, 'Ivonne']
print(f'Listas de nombres: {lista_heterogenea}')

#Iterar o recorrer los elementos de las listas 

for nombre in nombres:
    print(nombre, end=' ')


#Lista de números 
numeros =[100,200,300,400,500]

#Recuperando los elementos de la lista a través de su índice
print(numeros[0]) #Se recupera el valor 100

#Modificar los elemntos de una lista

numeros[0] = 1000 #Ahora en la lista en el índice 0 el valor será de 1000

print(numeros)

numero_a_buscar = 3000

if numero_a_buscar in numeros:
    print('El número se encuentra en la lista')
else: 
    print('El número no se encuentra en la lista')

#Recuperar el índice de cierto elemento de la lista 
indice = numeros.index(300)
print(indice)

#Redefinir la lista para tener en cuenta los valores originales 
numeros =[100,200,300,400,500]

#Recuperar una sublista = lista[índice_inicio, índice_final -1]

valores_recuperados = numeros[0:3]
print(valores_recuperados)

#Recuperar una sublista solo indicando el indice final
print(numeros[:2]) #Por default si no se espcidica inicio será el índice 0 

#Realizar una copia completa 
lista_copiada = numeros[:]
print(lista_copiada)

#Métodos de las listas
#length
largo_lista = len(numeros)
#agregar un nuevo elemento al final de la lista
numeros.append(600)
#insertar nuevo elementos en el indice deseado
numeros.insert(2,50)#los valores a partir de ese indice se moveran hacia la derecha y no habra perdida de datos 

##Eliminar un valor de la lista 
numeros.remove(600) #Solo indicamos en valor del elemento que queremos eliminar y no el indice 

#En caso de que hubiera elementos repetido se eliminará el primero que encuentre

#Concatenar listas 

nueva_lista = lista_copiada + numeros
print(f'Lista concatenada: {nueva_lista}')

#Eliminar un elemento por su indice 
del numeros[3] #removemos el valor en el indice 3
print(numeros)

#Eliminar lista completa 
numeros[:] = []
print(numeros) #no contiene elementos en esta linea

#Eliminar variables 
del numeros 











