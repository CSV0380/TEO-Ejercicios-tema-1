def calcula_imc(peso,estatura):
    imc = peso / (estatura**2)
    return imc


peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

imc = calcula_imc(peso, altura)


print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}") # .2f para dos decimales, la f depsues del print sirve para poder añadir dentro variables enrtre corchetes
