print('**Cajero automatico***')

saldo_actual = 1000
salir = False

while not salir:
    print(f'''
    1.Consultar Saldo
    2.Retirar dinero
    3.Depositar
    4. Salir
          ''')

    option = int(input('Escoge una optción: '))

    if option == 1: 
        print(f'tu saldo actual es de: {saldo_actual:.2f}\n')
    elif option == 2:
        retirar = float(input('Cuanto quieres retirar?: '))
        if retirar <= saldo_actual:  
            saldo_actual -= retirar
            print(f'Retirada de saldo completado con éxito. Tu saldo es de: {saldo_actual}')
        else:
            print(f'No tienes suficiente saldo para esta operación, saldo actual: {saldo_actual:.2f}\n')
    elif option == 3:
        retirar = float(input('Cuanto quieres depositar?: '))
        saldo_actual += retirar
        print(f'Depósito de saldo completado con éxito. Tu nuevo saldo es de: {saldo_actual:.2f}\n')
    elif option == 4:
        print('Saliendo del cajero automático... Hasta pronto')
        salir = True
    else:
        print('P favor intoruzca una opción válida')


