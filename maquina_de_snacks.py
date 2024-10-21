
salir = False
pedido = []
total = 0 
items = [
{'id': 0,'nombre': 'Papas','precio': 30},
{'id': 1,'nombre': 'Refresco','precio': 50},
{'id': 0,'nombre': 'Sandwich','precio': 120}
]
print('Sancks Disponibles:')
print('  Id: 0 -> Papas - Precio: 300')
print('  Id: 1 -> Refresco - Precio: 50')
print('  Id: 2 -> Sadwich - Precio: 120')

while not salir:

    print('Menu:')
    print('   1. Comprar')
    print('   2. Mostrar ticket')
    print('   3. Salir')
    option = int(input('Escoge una opción:'))

    if(option == 1):
        number = int(input('¿Qué número quieres?: '))
        if number < 0 and number > 3:
            print('por favor intorduce un número válido')
        else:
            pedido.append(items[number])
            print(f'Has pedido el producto: {items[0]}')
    if(option == 2):
        for item in pedido:
            total += item['precio'] 
        print(f'Tu pedido es: {pedido}')  
        print(f'Con un total de: {total}') 
    elif(option == 3):
        salir = True
        print('Hasta pronto...')
    else:
        print('Introduce un número válido')