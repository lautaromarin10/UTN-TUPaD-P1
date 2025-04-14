# Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

def saludar_al_mundo():
    imprimir_hola_mundo()

# Ejercicio 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

def saludar_usuario_ingresado():
    nombre = input("Ingrese su nombre\n")
    saludar_usuario(nombre)

# Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def presentar_usuario_con_informacion():
   nombre = input("Ingrese solo su nombre\n")
   apellido = input("Ingrese su apellido\n")
   edad = int(input("Ingrese su edad en numeros\n"))
   residencia = input("Ingrese la residencia en la cual vive.\n")

   informacion_personal(nombre, apellido, edad, residencia)

# Ejercicio 4

import math

def calcular_area_circulo(radio):
    #Dado el radio ingresado devuelve el area del circulo
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return (2 * math.pi) * radio

def imprimir_area_y_perimetro(radio):
    print(f"El circulo con radio {radio} tiene un area de {calcular_area_circulo(radio)} y un perimetro de {calcular_perimetro_circulo(radio)}")

def calcular_area_y_perimetro_segun_radio():
    #Pide el radio por consola y devuelve el area y el perimetro del circulo
    radio = float(input("Ingrese el radio del circulo a evaluar\n"))
    imprimir_area_y_perimetro(radio)

# Ejercicio 5

def segundos_a_horas(segundos):
    #Recibe una cantidad de segundos y devuelve las horas correspondiente.
    return segundos / 3600

def convertir_segundos_en_horas():
    segundos = float(input("Ingrese la cantidad de segundos a convertir en horas"))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} Segundos equivalen a {horas} horas.")

# Ejercicio 6

def numero_multiplicado_en(numero, multiplicador):
    return numero * multiplicador

def tabla_multiplicar():
    numero = int(input("Ingrese un numero para saber su tabla\n"))

    for i in range(1, 11):
        resultado = numero_multiplicado_en(numero, i)
        print(f"{numero} x {i} = {resultado}")

# Ejercicio 7

def operaciones_basicas(a, b):

    print(f"Operaciones basicas entre {a} y {b}:")
    print(f"Suma: {a + b}")
    print(f"Resta: {a - b}")
    print(f"Multiplicación: {a * b}")
    print(f"División: {a / b}")

# Ejercicio 8

def calcular_imc(peso, altura):
    return  peso / altura ** 2

def solicitar_peso_y_altura():
    peso = float(input("Ingrese su peso expresado en KG\n"))
    altura = float(input("Ingrese su altura separada en Metros (y utilizando . como separador)\n"))
    
    imc = calcular_imc(peso, altura)

    print(f"El IMC segun tu peso de {peso} kg y tu estatura de {altura}M es de {imc}")


# Ejercicio 9

def celsius_a_fahrenheit(celsius):
    return 9 / 5 * celsius + 32

def conversor_a_celsius():

    celsius = float(input("Ingrese la temperatura a convertir en Fahrenheit expresada en Celsius"))
    tempEnFahrenheit = celsius_a_fahrenheit(celsius)

    print(f"El equivalente en fahrenheit de la temperatura {celsius} Celsius es {tempEnFahrenheit}")

# Ejercicio 10

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

def promedio_entre_tres():

    primerNumero = float(input("Ingrese el primer numero"))
    segundoNumero = float(input("Ingrese el primer numero"))
    tercerNumero = float(input("Ingrese el primer numero"))

    promedio = calcular_promedio(primerNumero, segundoNumero, tercerNumero)

    print(f"El promedio entre {primerNumero}, {segundoNumero} y {tercerNumero} es {promedio}")

# Programa principal
def main():
    saludar_usuario_ingresado()
    presentar_usuario_con_informacion()