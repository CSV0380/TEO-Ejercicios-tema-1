
from ejercicio1 import * #para importar las funciones de otro fichero


#creamos una nueva funcion y metemos dentro la otra funcion del ejercicio 1


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



# Leer los valores de peso y altura desde el teclado una vez
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))



# Llamar a la función para calcular el estado nutricional y mostrarlo
estado_nutricional = calcula_estado_nutricional(peso, altura)
print(f"Tu estado nutricional es: {estado_nutricional}")
