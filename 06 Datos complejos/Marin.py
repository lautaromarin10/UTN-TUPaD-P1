# Ejercicio 1, añadir frutas al diccionario
def diccionario_frutas():
    precios_frutas = {"Banana": 1200, "Anana": 2500, "Melon": 3000, "Uva": 1450}
    #Nuevas frutas
    precios_frutas["Naranja"] = 1200
    precios_frutas["Manzana"] = 1500
    precios_frutas["Pera"] = 2300
    #Retorno para continuar ejercicio 2
    return precios_frutas

# Ejercicio 2, modificar los precios de las frutas
def modificar_precio_frutas():
    # Lista anterior
    lista_frutas = diccionario_frutas()
    # Precios anterior
    print(lista_frutas)

    #Modifico los precios
    lista_frutas["Banana"] = 1330
    lista_frutas["Manzana"] = 1700
    lista_frutas["Melon"] = 2800

    #Retorno para continuar ejercicio 3
    return lista_frutas

# Ejercicio 3 lisata nueva solamente con nombres, sin precios
def solo_nombres_frutas():
    #Lista obtenida en el ejercicio 2
    lista_frutas = modificar_precio_frutas()
    #Obtengo las keys de las frutas, es decir, solo el nombre de las frutas sin su valor.
    solo_frutas = lista_frutas.keys()

    return solo_frutas

#Clase persona con metodo init
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

def creacion_con_saludo():
    lautaro = Persona("Lautaro", "Argentina", 23)
    lautaro.saludar()

#Ejercio 5, clase circulo
from math import pi

class Circulo:
    
    #Constructor
    def __init__(self, radio):
        self.radio = radio

    #Metodos
    def calcular_area(self):
        return pi * (self.radio ** 2)
    
    def calcular_perimetro(self):
        return 2 * pi * self.radio
    

nuevoCirculo = Circulo(10)

#Ejercicio 6, verificar si algo esta balanceado
class Pila:
    
    def __init__(self):
        self.elementos = ""

    def apilar(self, elemento):
        self.elementos = self.elementos + elemento

    def esta_vacia(self):
        return self.elementos == ""

    def desapilar(self):
        if not self.esta_vacia():
            nuevo_elemento = self.elementos[:-1]
        self.elementos = nuevo_elemento

    def tiene_longitud_par(self):
        return len(self.elementos) % 2 == 0 if not self.esta_vacia() else False

    def esta_balanceada(self):
        pila_aux = Pila()
        parentesis_apertura = "({["
        parentesis_cierre = ")}]"
        
        for caracter in self.elementos:
            if caracter in parentesis_apertura:
                pila_aux.apilar(caracter)
            elif caracter in parentesis_cierre:
                if pila_aux.esta_vacia():
                    return False
                
                # Verificar si el último paréntesis de apertura corresponde con el de cierre
                ultimo_caracter = pila_aux.elementos[-1]
                if parentesis_apertura.index(ultimo_caracter) == parentesis_cierre.index(caracter):
                    pila_aux.desapilar()
                else:
                    return False
        
        return pila_aux.esta_vacia()

def comprobar_balanceo():
    comprobar = Pila()
    comprobar.apilar("{")
    print(comprobar.esta_balanceada())
    comprobar.apilar("}")
    print(comprobar.esta_balanceada())

#Ejercicio 7 simular turno de bancos

from collections import deque

class Cola_Banco:

    def __init__(self):
        self.personas = deque()

    def encolar(self, persona):
        self.personas.append(persona)

    def cola_vacia(self):
        return len(self.personas) == 0

    def desencolar(self):
        if not self.cola_vacia():
            return self.personas.popleft()
        
    def siguiente_cliente(self):
        if self.cola_vacia():
            print("La fila esta vacia")
        else:
            return self.personas[0]
        
#Ejercicio 8, lista enlazada

#Definimos la clase nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

#Creo la clase lista enlazada
class lista_enlazada:
    def __init__(self):
        self.cabecera = None #Inicialización de cabecera vacia

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabecera
        self.cabecera = nuevo_nodo

    

    def mostrar_nodos(self):
        actual_cabecera = self.cabecera
        while actual_cabecera:
            print(actual_cabecera.dato, end="=>")
            actual_cabecera = actual_cabecera.siguiente
        print("Ninguno")

    #Ejercicio 9, invertir lista
    def largo_de_lista(self):
        contador = 0
        actual = self.cabecera
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def retornar_nodos(self):
        lista_nodos = []
        actual_cabecera = self.cabecera
        while actual_cabecera:
            lista_nodos.append(actual_cabecera.dato)
            actual_cabecera = actual_cabecera.siguiente
        return lista_nodos

    def invertir_lista(self):
        lista_actual = self.retornar_nodos()
        lista_invertida = []

        for i in range(self.largo_de_lista() -1, -1, -1):
            lista_invertida.append(lista_actual[i])

        return lista_invertida


#Prueba de ejercicios 8 y 9
lista_prueba = lista_enlazada()
lista_prueba.insertar("1")
lista_prueba.insertar("2")
lista_prueba.insertar("3")
print(lista_prueba.invertir_lista())