# Bryan Ortiz

# Encuesta para 6 usuarios

# Nombre - Carrera - Idea de proyecto - Programas a usar - Sabe trabajar en equipo

class Encuesta:

    def __init__(self, nombre, carrera, proyecto, equipo):

        self.nombre = nombre
        self.carrera = carrera
        self.proyecto = proyecto
        self.equipo = equipo

    def mostrar_respuestas(self):

        respuesta = f"Nombre: {self.nombre}\n"
        respuesta += f"Carrera: {self.carrera}\n"
        respuesta += f"Proyecto: {self.proyecto}\n"
        respuesta += f"¿Sabe trabajar en equipo?: {self.equipo}"
        return respuesta

def agregar_respuestas():

    usuarios = [] 

    for i in range(10):
        
        print(f"\nEncuesta #{i+1}:")
        nombre = input("¿Cuál es su nombre? ")
        carrera = input("¿Cuál es su carrera? ")
        proyecto = input("¿Cuál es su idea de proyecto? ")
        equipo = input("¿Sabe trabajar en equipo? (Sí/No): ")
        print("GRACIAS\n")

        usuario = Encuesta(nombre, carrera, proyecto, equipo)
        usuarios.append(usuario)

    return usuarios

usuarios = agregar_respuestas()

print("\nInformación de los usuarios:")
for i, usuario in enumerate(usuarios, start=1):
    print(f"\nRespuestas usuario #{i}:\n{usuario.mostrar_respuestas()}")
