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







