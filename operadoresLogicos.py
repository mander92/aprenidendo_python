print('Operadores Lóggicos')

llueve = False  
nublado = True
#Aplicamos el operador And

if not llueve and nublado:
    print('llevar paraguas') 
elif llueve: 
    print('llevar paraguas, va a llover')
elif nublado:
    print('no hace falta llevar paraguas, esta nublado pero no va a llover')
else: 
    print('hoy hacxe un buen día')
#Aplicamos el operador Or

if llueve or nublado:
    print('llevar paraguas') 
elif llueve: 
    print('llevar paraguas, va a llover')
elif nublado:
    print('no hace falta llevar paraguas, esta nublado pero no va a llover')
else: 
    print('hoy hacxe un buen día')


