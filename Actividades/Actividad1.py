# AUTOR: Bryan David Ortiz Arteaga

# Ejercicio no.31

# Desarrolle una clase en Python que realice la abstracción de un sistema planetario,
# debiendo tener en cuenta para cada cuerpo del sistema aspectos como: masa,
# densidad, diámetro, distancia al sol (suponga órbitas circulares), un número de
# identificador único y un nombre textual. Incluya método que calcule la atracción
# gravitatoria entre dos cuerpos cualesquiera del sistema.


class Sistema_Planetario: # Creamos la clase sistema planetario

    def __init__(planeta, masa, densidad, diámetro, distancia_sol, identificador, nombre): # Definimos el constructor de la clase con sus atributos

        # Definimos los atributos que son las características de los planetas

        planeta.ms = masa
        planeta.dns = densidad
        planeta.dmt = diámetro
        planeta.dis = distancia_sol
        planeta.id = identificador
        planeta.n = nombre

    
    # Definimos los métodos (Atracción Gravitatoria)

    def Atracción_Gravitatoria(planeta, otro_planeta): # Método que calcula la atracción gravitatoria entre dos planetas

        Constante_de_Gravitación_Universal = 6.674e-11 # Constante necesaria para  el cálculo de la función

        masa1 = planeta.ms # Sacamos la masa del primer planeta
        masa2 = otro_planeta.ms # Sacamos la masa del segundo planeta

        distancia_centros = abs((planeta.dis - otro_planeta.dis) * 1e9 * 1000) # Sacamos la distancia del centro de los planetas y lo convertimos a metros

        AG = Constante_de_Gravitación_Universal * (masa1 * masa2) / (distancia_centros**2) # Fórmula de la atracción gravitatoria

        return AG # Retornamos el valor de la atracción gravitatoria

# Definimos los Objetos (Planetas)

Mercurio = Sistema_Planetario(3.302e23, 5427, 4879, 57.9, 1, "Mercurio")
Venus = Sistema_Planetario(4.867e24, 5243, 12104, 108.2, 2, "Venus")
Tierra = Sistema_Planetario(5.972e24, 5514, 12742, 149.6, 3, "Tierra")
Marte = Sistema_Planetario(6.417e23, 3933, 6779, 227.9, 4, "Marte")
Júpiter = Sistema_Planetario(1.898e27, 1326, 142984, 778.6, 5, "Júpiter")
Saturno = Sistema_Planetario(5.683e26, 687, 120536, 1433.5, 6, "Saturno")
Urano = Sistema_Planetario(8.681e25, 1270, 51118, 2872.5, 7, "Urano")
Neptuno = Sistema_Planetario(1.024e26, 1638, 49528, 4495.1, 8, "Neptuno")

AG = Tierra.Atracción_Gravitatoria(Venus)
print(f"La atracción gravitatoria entre {Tierra.n} y {Venus.n} es {AG:.2e} N")

AG = Marte.Atracción_Gravitatoria(Mercurio)
print(f"La atracción gravitatoria entre {Marte.n} y {Mercurio.n} es {AG:.2e} N")

AG = Júpiter.Atracción_Gravitatoria(Saturno)
print(f"La atracción gravitatoria entre {Júpiter.n} y {Saturno.n} es {AG:.2e} N")



# Ejercicio no.34

# Se quiere implementar el control de un Ferry. Para ello cree una clase Vehículo.
# Incluya aspectos comunes a todos los vehículos como número de pasajeros,
# presencia o ausencia de tripulación, número de ruedas, fecha de matriculación,
# medio por el que se desplaza, etc. Incluya los métodos que considere oportunos.
# Realice un programa capaz de leer por teclado los datos de 10 vehículos y los liste a
# continuación por pantalla.

class Vehículo: # Creamos la clase vehículo

    def __init__(vehículo, num_pasajeros, tripulación, num_ruedas, fecha_matriculación, medio_desplazamiento): # Definimos el constructor de la clase con sus atributos

    # Definimos los atributos que son las características de los vehículos

        vehículo.np = num_pasajeros
        vehículo.tr = tripulación
        vehículo.nr = num_ruedas
        vehículo.fm = fecha_matriculación
        vehículo.md = medio_desplazamiento

    # Definimos los métodos (Mostrar Información)

    def Mostrar_Información(vehículo): # Método que muestra la información del vehículo

        info = f"Número de pasajeros: {vehículo.np}\n"
        info += f"Presencia de tripulación: {vehículo.tr}\n"
        info += f"Número de ruedas: {vehículo.nr}\n"   
        info += f"Fecha de matriculación: {vehículo.fm}\n"
        info += f"Medio de desplazamiento: {vehículo.md}\n"
        return info
    
# Definimos una lista para almacenar los vehículos

vehículos = []

# Leemos los datos de 10 vehículos por teclado

for i in range(1):
    print(f"Ingrese los datos del vehículo {i+1}:")
    np = int(input("Número de pasajeros: "))
    tr = input("¿Tiene tripulación? (sí o no): ")
    nr = int(input("Número de ruedas: "))
    fm = input("Fecha de matriculación (DD/MM/AAAA): ")
    md = input("Medio de desplazamiento: ")
    
    # Creamos un objeto Vehículo y lo añadimos a la lista

    vehículo = Vehículo(np, tr, nr, fm, md)
    vehículos.append(vehículo)

# Listamos los vehículos por pantalla

print("Información de los vehículos ingresados:")
for i, vehículo in enumerate(vehículos, start=1):
    print(f"\nVehículo {i}:\n{vehículo.Mostrar_Información()}")



# Ejercicio no.1

# Crear una clase con atributos: nombre, edad, genero, peso, altura.
# Incluir métodos para calcular IMC, y verificar la mayoría de edad.

class Persona: # Creamos la clase persona

    def __init__(persona, nombre, edad, genero, peso, altura): # Definimos el constructor de la clase con sus atributos

        # Definimos los atributos que son las características de las personas

        persona.n = nombre
        persona.e = edad
        persona.g = genero
        persona.p = peso
        persona.a = altura

    def calcular_IMC(persona): # Método que calcula el IMC

        IMC = persona.p / (persona.a ** 2) # Fórmula del IMC
        return IMC
    
    def verificar_edad(persona): # Método que verifica si la persona es mayor de edad
        return persona.e >= 18
    
# Definimos un objeto Persona

persona1 = Persona("Juan", 25, "Masculino", 70, 1.75)

IMC = persona1.calcular_IMC()
print(f"El IMC de {persona1.n} es {IMC}")

if persona1.verificar_edad():
    print(f"{persona1.n} es mayor de edad.")
else:
    print(f"{persona1.n} no es mayor de edad.")
