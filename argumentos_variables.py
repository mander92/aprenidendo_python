print('*** Argumentos Variables ***')

def super_heroe(nombre, *args):
    print(f'superheroe: {nombre}, {args}')
    for arg in args: 
        print(arg)

super_heroe('SpiderMan', 'Instinto Arancnido', 'tela de araña')

#Es opcional enviar argumentos a variables 
super_heroe('Mario')