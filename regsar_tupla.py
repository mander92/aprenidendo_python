print('*** Regresar una tupla de valores desde una función ***')

def persona_mayusculas(nombre, apellido, edad):
    print('Esta función regresa varios (tuplas)')
    return (nombre.upper(), apellido.upper(), edad)

nombre, apellido, edad = persona_mayusculas('sandra', 'maria', 27)
print(nombre)
print(apellido)
print(edad)