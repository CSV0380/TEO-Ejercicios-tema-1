"""
from ejercicio1 import *


def calcula_estado_nutricional(peso, altura):
    # Llamar a la función calcula_imc para obtener el IMC
    imc = calcula_imc(peso, altura)
    #las condiciones segun el imc
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"



def imprime_estados_nutricionales(personas):
    for i, (peso,estatura) in enumerate(personas):
        imc = calcula_imc(peso,estatura)
        estado = calcula_estado_nutricional(peso, estatura)
        print(f"El IMC de la persona {i} es {imc}, y su estado nutricional es {estado}.")

   

personas = [
    (60.0, 1.6),
    (75.4, 1.75),
    (87.9, 1.69),
    (45.1, 1.65)
]

# Llamar a la función para mostrar los resultados
imprime_estados_nutricionales(personas)


"""





def calcula_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


def calcula_estado_nutricional(peso, altura):
    imc = calcula_imc(peso, altura)
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"



def imprime_estados_nutricionales(personas):
    for i, (peso, altura) in enumerate(personas): #enumerate sirve para enumerar cada elemento de la lista de tuplas comenzando por 0, se pone el peso y altura para saber que es cada cosa de la tupla
        # Calcular el IMC y el estado nutricional para cada persona
        imc = calcula_imc(peso, altura) #debo calcular el imc de cada persona de la lista
        estado = calcula_estado_nutricional(peso, altura) #debo calcular el estado de cada persona de la lista
        
        # Imprimir el resultado en el formato solicitado
        print(f"El IMC de la persona {i} es {imc: .2f}, y su estado nutricional es {estado}.") #.2f es para los mostrar 2 decimales


personas = [
    (60.0, 1.6),
    (75.4, 1.75),
    (87.9, 1.69),
    (45.1, 1.65)
]

# Llamar a la función para mostrar los resultados
imprime_estados_nutricionales(personas)
