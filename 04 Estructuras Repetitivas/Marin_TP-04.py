# Ejercicio 1

def numerosDel0Al100(): 
    for i in range(1,101):
        print(i)

# Ejercicio 2

def nroDigitosDelEntero():

    numero = int(input("Ingrese un numero Entero a saber su largo\n"))
    cantidadDeDigitos = 0

    while numero != 0:
        numero = numero // 10
        cantidadDeDigitos += 1

    print(f"El numero ingresado tiene {cantidadDeDigitos}")

# Ejercicio 3

def sumaDeIntermedios():

    acumulador = 0

    #El rango debe empezar en 31 ya que el 30 se excluira
    for i in range(31,50):
        acumulador += i

    print(acumulador)

# Ejercicio 4

def acumuladorDeEnteros():

    acumulador = 0
    numero = int(input("Ingrese un entero diferente de cero para acumular\n"))

    while numero != 0:
        acumulador += numero
        numero = int(input("Ingrese un entero diferente de cero para acumular\n"))

    print(f"total del valor acumulado {acumulador}")


# Ejercicio 5

import random

def adivinarNumero():

    #Intentos debe empezar en 1 ya que el usuario ingresa un numero para iniciar el programa, en caso de que sea el mismo al numero random retornara que tomo un intento.
    intentos = 1
    #Generamos un numero random
    numeroRandom = random.randint(0,9)
    numero = int(input("Ingrese un numero entre 0 y 9\n"))

    while numeroRandom != numero:
        intentos += 1
        print(f"No es el numero, intentalo otra vez! {numeroRandom}")
        numero = int(input("Ingrese un numero entre 0 y 9\n"))

    print(f"Tardaste {intentos} intentos en adivinar el numero {numeroRandom}")

# Ejercicio 6

def paresHastaEl0DesdeEl100():

    for i in range(100, 0, -2):
        print(i)

# Ejercicio 7

def sumaDel0HastaNroIndicado():

    nroIndicado = int(input("Ingrese un numero para hacer la suma desde los numeros del 0 hasta el numero indicado\n"))
    acumulador = 0

    for i in range(0, nroIndicado):
        acumulador += i

    print(acumulador)

# Ejercicio 8

def clasificarNumerosIngresados():

    nrosPositivos = 0
    nrosNegativos = 0
    nrosPares = 0
    nrosImpares = 0

    for i in range(0, 100):
        nroAClasificar = int(input("Ingrese el numero a clasificar\n"))

        if nroAClasificar > 0:
            nrosPositivos += 1
        else:
            nrosNegativos += 0

        if nroAClasificar % 2 == 0:
            nrosPares += 1
        else:
            nrosImpares += 1
    
    print(f"Positivos {nrosPositivos} Negativos {nrosNegativos} Pares {nrosPares} Impares {nrosImpares}")

# Ejercicio 9

def mediaDeCienValores():

    acumulador = 0

    for i in range(0, 100):
        acumulador += int(input("Ingrese un numero entero"))

    media = acumulador / 100

    print(f"la media de los numeros ingresados es {media}")

# Ejercicio 10

def nroDigitosDelEntero(num):

    numero = num
    cantidadDeDigitos = 0

    while numero != 0:
        numero = numero // 10
        cantidadDeDigitos += 1

    #devuelve la cantidad de digitos que tiene el numero que se pasa por parametros
    return cantidadDeDigitos


def invertirNumeros():

    nroAInvertir = int(input("Ingrese un numero a invertir"))
    nroInvertido = 0

    while nroAInvertir != 0:
        
        #obtenemos el ultimo digito de los numeros actuales y los multiplicamos por 10 eleavdo a la cantida de digitos menos 1
        nroInvertido += (nroAInvertir % 10) * 10 ** (nroDigitosDelEntero(nroAInvertir) - 1)
        nroDigitosDelEntero(nroAInvertir)
        #Eliminamos el ultimo digito del nroAInvertir
        nroAInvertir = nroAInvertir // 10

    print(nroInvertido)
