# Ejercicio 1
def factorial_recursivo(num):
    return 1 if num == 0 else num * factorial_recursivo(num - 1)

def buscar_factorial():
    numero = int(input("Ingrese un numero a buscar el factorial\n"))
    print(factorial_recursivo(numero))

# Ejercicio 2
def calcular_valor_fibonacci(posicion):
    if posicion in [0, 1]:
        return posicion
    else:
        return calcular_valor_fibonacci(posicion-1)+calcular_valor_fibonacci(posicion-2)
    

def serie_fibonacci():
    posicion = int(input("Ingrese una posición a cortar en fibonacci\n"))

    for posicion_actual in range(posicion + 1):
        print(calcular_valor_fibonacci(posicion_actual))

# Ejercicio 3
def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

def prueba_algoritmo():
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    print(potencia_recursiva(base, exponente))

# Ejercicio 4
def cociente_y_resto(numero):
    return [numero // 2, numero % 2]


def conversion_decimal_a_binario(numero):
    if numero == 0:
        return [0]
    else:
        cociente = cociente_y_resto(numero)[0]
        resto = cociente_y_resto(numero)[1]
        return conversion_decimal_a_binario(cociente) + [resto]

def representacion_decimal_a_binario():
    numero_decimal = int(input("Ingrese el numero a buscar su representación en bianrio"))
    representacion_binaria = conversion_decimal_a_binario(numero_decimal)
    cadena_binaria = ''.join(map(str, representacion_binaria))
    return cadena_binaria

# Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

# Ejercicio 6
def suma_digitos(num):
    if num < 10:
        return num # Base
    else:
        return num % 10 + suma_digitos(num // 10)

# Ejercicio 7
def contar_bloques(n):
    if n in [0, 1]:
        return n #base
    else: 
        return n + contar_bloques(n - 1)

# Ejercicio 8
def contar_digito(numero, digito):
    if numero <= 0:
        return 0 #retorno 0 en caso de que el numero sea negativo o 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito) # sumo uno si es igual
    else:
        return contar_digito(numero // 10, digito) #sigo recorriendo si no es igual