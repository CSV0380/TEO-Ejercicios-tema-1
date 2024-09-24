
from ejercicio1 import *


def calcula_estado_nutricional(peso, altura):
    # Llamar a la función calcula_imc para obtener el IMC
    imc = calcula_imc(peso, altura)

    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"


# Leer los valores de peso y altura desde el teclado una vez
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))


# Llamar a la función para calcular el estado nutricional y mostrarlo
estado_nutricional = calcula_estado_nutricional(peso, altura)
print(f"Tu estado nutricional es: {estado_nutricional}")
