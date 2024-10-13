
print('***Sistema de Administración de Cuentas***')

salir = False 

while not salir:
    print(f'''Menu:
      1 Crear Cuenta
      2 Eliminar cuenta
      3 Salir''')
      
    option = int(input('Escoje una opción: '))

    if option == 1:
        print('Creando cuenta')
    elif option == 2:
        print('Eliminando cuenta')
    elif option == 3: 
        print('Saliendo')
        salir = True
    else:
        print('Por favor introduce un valor válido')