print('********** Programa que determina si un número es positivo, negativo o cero **********')

num = int(input('Ingresa un número: '))

if num > 0:
    print (f'El número {num} es positivo')
elif num == 0:
    print(f'El número es {num} ') 
else: 
    print(f'El número {num} es negativo') 