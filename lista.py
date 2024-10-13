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








