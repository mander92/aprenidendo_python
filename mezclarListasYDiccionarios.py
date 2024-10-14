print('*** Mezclar listas y diccionario o objetos ***')

personas = [
    {
        'nombre': 'Mario',
        'apellido': 'Martin',
        'edad': 32
    },
    {
        'nombre': 'Juan',
        'apellido': 'Lopez',
        'edad': 23
    }
]

print(personas[0].get('nombre'))

print(personas[1].get('edad'))

#Recorreo los elementos de la lista
for contador, persona in enumerate(personas):
    print(f'Persona: {contador}: {persona.get('nombre')}')

