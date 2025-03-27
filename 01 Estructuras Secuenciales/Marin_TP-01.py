# Ejercicio 1
def saludarAlMundo():

    print(f"Hola Mundo!")

# Ejercicio 2
def saludarA():

    nombre = str(input("Ingrese su nombre!\n"))
    print(f"Hola {nombre}!")

# Ejercicio 3
def datosPersonales():

    nombre = str(input("Ingrese su nombre\n"))
    apellido = str(input("Ingrese su apellido\n"))
    edad = int(input("Ingrese su edad\n"))
    residencia = str(input("Ingrese su lugar de residencia\n"))

    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}!")


# Ejercicio 4
def areaYPerimetroDeCirculo():

    pi = 3.1416
    radioDelCirculo = float(input("Ingrese el radio del circulo\n"))
    #area
    areaDelCirculo = pi * (radioDelCirculo ** 2)
    print(f"El area de un Circulo de radio {radioDelCirculo} es {areaDelCirculo}")
    #perimetro
    perimetroDelCirculo = 2 * pi * radioDelCirculo
    print(f"El perimetro de un Circulo de radio {radioDelCirculo} es {perimetroDelCirculo} ")

# Ejercico 5
def segundosAHoras():

    segundos = int(input("Ingrese los Segundos a convertir a horas\n"))

    #conversiones previas    
    minutos =  segundos / 60
    horas = minutos / 60

    print(f"{segundos} Segundos convertidos a Horas son {horas}")

# Ejercicio 6
def tablasDeUnNumero():

    numeroABuscarTabla = int(input("Ingrese el Numero a saber la tabla de multiplicar\n"))

    for i in range(1, 11):
        print(f"{numeroABuscarTabla} x {i}: {numeroABuscarTabla * i}")

# Ejercicio 7 
def operacionesConDosNumeros():



    primerNumero = int(input("Ingrese el primer numero entero y distinto de 0\n"))
    segundoNumero = int(input("Ingrese el segundo Numero entero y distinto de 0\n"))

    #Operaciones
    print(f"{primerNumero} + {segundoNumero}: {primerNumero + segundoNumero}\n")
    print(f"{primerNumero} - {segundoNumero}: {primerNumero - segundoNumero}\n")
    print(f"{primerNumero} * {segundoNumero}: {primerNumero * segundoNumero}\n")
    print(f"{primerNumero} / {segundoNumero}: {primerNumero / segundoNumero}\n")


# Ejercicio 8
def indiceMasaCorporal():

    altura = float(input("Ingresa tu altura en metros\n"))
    peso = float(input("Ingrese tu peso actual en kg\n"))

    indiceMasaCorporal = peso / (altura ** 2)

    #conversion a 2 decimales
    indiceMasaCorporal = indiceMasaCorporal * 10000

    print(f"Tu indice de Masa Corporal es {indiceMasaCorporal}")

# Ejercicio 9
def celsiusAFahrenheit():

    celsius = float(input("Ingresa la temperatura en grados Celsius\n"))
    fahrenheit = 9 / 5 * celsius + 32

    print(f"{celsius} convertido a Fahrenheit es {fahrenheit}")

# Ejercicio 10
def promedioDe3Numeros():

    primerNumero = int(input("Ingrese el primer numero\n"))
    segundoNumero = int(input("Ingrese el segundo numero\n"))
    terceroNumero = int(input("Ingrese el tercero numero\n"))

    promedio = (primerNumero + segundoNumero + terceroNumero) / 3

    print(f"El promedio de los 3 numeros es {promedio}")

