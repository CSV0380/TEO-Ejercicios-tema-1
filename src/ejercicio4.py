def lee_numeros(cantidad):
    lista = []
    for i in range(cantidad):
        numero = int(input(f"Ingrese el número {i+1}: "))  # El i+1 sirve para pedir el 1, luego el 2, luego el 3...
        lista.append(numero)
    return lista





#Subapartados

def mayor_numero(lista):  
    return max(lista)

def media_numeros(lista):
    return sum(lista) / len(lista)

def contar_pares(lista):
    return len([num for num in lista if num % 2 == 0])

def mayores_a_10(lista):
    return [num for num in lista if num > 10]




#Inputs

cantidad_numeros = int(input("Dime una cantidad de números: "))
numeros = lee_numeros(cantidad_numeros)
print("Lista de números introducidos:", numeros)




#Lo que quiere que calcule

mayor = mayor_numero(numeros)
print(f"El mayor número de la lista es: {mayor}")


media = media_numeros(numeros)
print(f"La media de los números es: {media:.2f}")


pares = contar_pares(numeros)
print(f"Hay {pares} números pares")


mayores = mayores_a_10(numeros)
print(f"Nueva lista con números mayores a 10: {mayores}")

