# Ejercicio 1
lista_al_100 = list(range(4,101,4))

# Ejercicio 2
lista_cinco_elementos = ["Piña", "Banana", "Melon", "Sandia", "Manzana"]
print(lista_cinco_elementos[-2])

# Ejercicio 3
lista_vacia = []
lista_vacia.append("Me")
lista_vacia.append("Fui")
lista_vacia.append("Llenando")
print(lista_vacia)

# Ejercicio 4
animales = ["Perro", "Gato", "Conejo", "Pez"]
animales[1] = "Loro"
animales[-1] = "Oso"
print(animales)

# Ejercicio 5
# Lo que hace el programa es remover de la lista de nuemros el numero mas grande, siendo el mas grande el 22

# Ejercicio 6
numeros_diez_al_treinta = list(range(10, 31, 5))
print(numeros_diez_al_treinta[:2])

# Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "Subaru"
autos[2] = "Vento"

# Ejercicio 8

lista_con_dobles = []

for numero in [5, 10, 15]:
    lista_con_dobles.append(numero * 2)

print(lista_con_dobles)

# Ejercicio 9

compras = [["pan" , "leche"], ["arroz","fideos","salsa"],["agua"]]
#Agregamos Jugo a la tercer lista
compras[2].append("Jugo")
#Reemplazo fideos por tallarines
compras[1][1] = "Tallarines"
#Elimino pan de la primer lista
compras[0].remove("pan")
#Imprimo la lista resultante
print(compras)

# Ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)