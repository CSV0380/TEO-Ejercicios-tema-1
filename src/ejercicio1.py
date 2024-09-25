def calcula_imc(peso,estatura):
    imc = peso / (estatura**2)
    return imc

#los valores que obtenga la funcion siempre deben estar fuera de la misma, por ejemplo: peso y estatura 

peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

#para llamar a una funcion podemos hacerlo igualanado una variable para guardarlo dentro el valor

imc = calcula_imc(peso, altura)

#ponemos la salida de los valores introducidos

print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}") # .2f para dos decimales, la f depsues del print sirve para poder añadir dentro variables enrtre corchetes
