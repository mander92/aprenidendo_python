print('*** Función con argumentos ***')
#Una función que recibe argumentos como parámetro
def crear_persona(nombre, apellido, edad):
    print(f'Persona: nombre = {nombre}, apellido: {apellido}, edad: {edad}')


#Lamamos a la función.Debemos respetar en este caso el mismo orden o sino habrá que espcificar el nombre de la variables, en ese caso, no será necesario guardarlo.
crear_persona('Ricardo', 'Cruz', 29)

