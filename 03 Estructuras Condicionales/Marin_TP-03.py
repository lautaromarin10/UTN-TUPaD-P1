# Ejercicio 1

def esMayor():
    edad = int(input("Ingrese su edad\n"))

    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")

# Ejercicio 2
def comprobarNota():
    nota = int(input("Ingresa la nota a comprobar\n"))

    print("Aprobado" if nota >= 6 else "Desaprobado" )

# Ejercicio 3

def esPar(numero):
    return numero % 2 == 0

def numerosPares():
    numero = int(input("Ingresa un número par\n"))
    print("Ha ingresado un número par" if esPar(numero) else "Por favor, ingrese un número par")

# Ejercicio 4

def evaluarCategoriaPorEdad():

     edad = int(input("Ingrese su edad para conocer su categoría\n"))

     if edad < 12:
         print("Es niño")
     elif edad > 12 and edad < 18:
         print("Adolescente")
     elif edad >= 18 and edad < 30:
         print("Adulto/a joven")
     else:
         print("Adulto/a") 

# Ejercicio 5

def esPasswordValida(password):
    longitud = len(password)
    return longitud >= 8 and longitud <= 14

def revisarPassword():
    password = input("Ingrese una contraseña que contenga entre 8 a 14 caracteres")
    #Mensajes
    msjSuccess = "Ha ingresado una contraseña correcta"
    msjFail = "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"

    print( msjSuccess if esPasswordValida(password) else msjFail  )


# Ejercicio 6
import random
from statistics import mode, median, mean

def haySesgoPositivo(media, mediana, moda):
    return media > mediana > moda

def haySesgoNegativo(media, mediana, moda):
    return media < mediana < moda

def noHaySesgo(media, mediana, moda):
    return media == mediana == moda

def comprobarSesgo():

    numerosAleatorios = [random.randint(1,100) for i in range(50)]

    moda = mode(numerosAleatorios)
    mediana = median(numerosAleatorios)
    media = mean(numerosAleatorios)

    print(f"Media: {media}, Mediana: {mediana}, moda: {moda}")

    if haySesgoPositivo(media, mediana, moda):
            print("Hay sesgo positivo")
    elif haySesgoNegativo(media, mediana, moda):
            print("Hay sesgo negativo")
    elif noHaySesgo(media, mediana, moda):
        print("No hay sesgo")

# Ejercicio 7

def terminaEnVocal(palabra):
    #calcula el largo de la palabra
    largo = len(palabra)
    #deja solo el ultimo caracter de la palabra
    ultimaLetra = palabra[largo-1]
    #retorna verdadero si ultimaLetra es una vocal, caso contrario retorna falso
    return ultimaLetra.lower() in ["a", "e", "i", "o", "u"]


def analizarFraseOPalabra():

    fraseOPalabra = input("Ingrese una frase o una palabra\n")
    print(f"{fraseOPalabra}!" if terminaEnVocal(fraseOPalabra) else fraseOPalabra)
    
# Ejercicio 8

def nombreAMinuscula(nombre):
    return nombre.lower()

def nombreAMayuscula(nombre):
    return nombre.upper()

def nombreCapitalizado(nombre):
    return nombre.capitalize()

def transformarNombre():
    nombre = input("Ingresa tu nombre\n")
    opcionSeleccionada = int(input("Selecciona una de las opciones para transformar \n 1)Nombre a mayusculas\n 2)Nombre a minusculas\n 3)Nombre con primera letra mayuscula\n"))

    if opcionSeleccionada == 1:
        print(nombreAMinuscula(nombre))
    elif opcionSeleccionada == 2:
        print(nombreAMayuscula(nombre))
    elif opcionSeleccionada == 3:
        print(nombreCapitalizado(nombre))
    else:
        print("No has ingresado una opcion valida")

# Ejercicio 9

def evaluarTerremoto():

    magnitud = float(input("Ingrese la magnitud de un terremoto\n"))

    if 3 <= magnitud < 4:
        print("Leve")
    elif 4 <= magnitud < 5:
        print("Moderado")
    elif 5 <= magnitud < 6:
        print("Fuerte")
    elif 6 <= magnitud < 7:
        print("Muy fuerte")
    elif magnitud >= 7:
        print("Extremo")
    else:
        print("Muy Leve")

# Ejercicio 10

def esPrimerPeriodo(mes, dia):
    #el primer periodo va desde el 12 de Diciembre hasta el 20 de Marzo
    return (mes == 12 and dia >= 21) or (mes in [1,2] and (dia >= 1 and dia <= 31)) or (mes == 3 and dia <= 20)

def esSegundoPeriodo(mes, dia):
    #el segundo periodo va desde el 21 de Marzo hasta el 20 de Junio
    return (mes == 3 and dia >= 21) or (mes in [4,5] and (dia >= 1 and dia <= 31)) or (mes == 6 and dia <= 20)

def esTercerPeriodo(mes, dia):
    #el tercer periodo va desde el 21 de Junio hasta el 20 de Septiembre
    return (mes == 6 and dia >= 21) or (mes in [7,8] and (dia >= 1 and dia <= 31)) or (mes == 9 and dia <= 20)



def definirEstacion():
    
    hemisferio = input("En que Hemisferio te encuentras? \n N) Norte\n S) Sur\n").upper()
    mes = int(input("Que mes del año es? ingrese el numero correspondiente\n"))
    dia = int(input("Ingrese el dia actual"))

    if esPrimerPeriodo(mes, dia):
        print("En el Hemisferio Norte es Invierno" if hemisferio == "N" else "En el Hemisferio Sur es Verano")
    elif esSegundoPeriodo(mes,dia):
        print("En el Hemisferio Norte es Primavera" if hemisferio == "N" else "En el Hemisferio Sur es Otoño")
    elif esTercerPeriodo(mes, dia):
        print("En el Hemisferio Norte es Verano" if hemisferio == "N" else "En el Hemisferio Sur es Invierno")
    else:
        print("En el Hemisferio Norte es Otoño" if hemisferio == "N" else "En el Hemisferio Sur es Primavea")

definirEstacion()