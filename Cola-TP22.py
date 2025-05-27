
from queue_ import Queue

class PersonajeMCU:
    def __init__(self, nombre_real, nombre_superheroe, genero):
        self.nombre_real = nombre_real
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero  # 'M' o 'F'

    def __str__(self):
        return f"{self.nombre_real} / {self.nombre_superheroe} - {self.genero}"

# Datos de prueba
personajes = [
    PersonajeMCU("Tony Stark", "Iron Man", "M"),
    PersonajeMCU("Steve Rogers", "Capitán América", "M"),
    PersonajeMCU("Natasha Romanoff", "Black Widow", "F"),
    PersonajeMCU("Carol Danvers", "Capitana Marvel", "F"),
    PersonajeMCU("Scott Lang", "Ant-Man", "M"),
    PersonajeMCU("Stephen Strange", "Doctor Strange", "M"),
]

cola_personajes = Queue()
for p in personajes:
    cola_personajes.arrive(p)

# a. Personaje de Capitana Marvel
print("--- a. Capitana Marvel ---")
aux = Queue()
while cola_personajes.size() > 0:
    p = cola_personajes.attention()
    if p.nombre_superheroe == "Capitana Marvel":
        print("Personaje:", p.nombre_real)
    aux.arrive(p)
while aux.size() > 0:
    cola_personajes.arrive(aux.attention())

# b. Superhéroes femeninos
print("\n--- b. Superhéroes Femeninos ---")
aux = Queue()
while cola_personajes.size() > 0:
    p = cola_personajes.attention()
    if p.genero == "F":
        print(p.nombre_superheroe)
    aux.arrive(p)
while aux.size() > 0:
    cola_personajes.arrive(aux.attention())

# c. Personajes masculinos
print("\n--- c. Personajes Masculinos ---")
aux = Queue()
while cola_personajes.size() > 0:
    p = cola_personajes.attention()
    if p.genero == "M":
        print(p.nombre_real)
    aux.arrive(p)
while aux.size() > 0:
    cola_personajes.arrive(aux.attention())

# d. Superhéroe de Scott Lang
print("\n--- d. Superhéroe de Scott Lang ---")
aux = Queue()
while cola_personajes.size() > 0:
    p = cola_personajes.attention()
    if p.nombre_real == "Scott Lang":
        print("Superhéroe:", p.nombre_superheroe)
    aux.arrive(p)
while aux.size() > 0:
    cola_personajes.arrive(aux.attention())

# e. Mostrar todos cuyos nombres comienzan con S
print("\n--- e. Nombres que comienzan con S ---")
aux = Queue()
while cola_personajes.size() > 0:
    p = cola_personajes.attention()
    if p.nombre_real.startswith("S") or p.nombre_superheroe.startswith("S"):
        print(p)
    aux.arrive(p)
while aux.size() > 0:
    cola_personajes.arrive(aux.attention())

# f. Verificar si está Carol Danvers
print("\n--- f. ¿Carol Danvers está? ---")
encontrado = False
aux = Queue()
while cola_personajes.size() > 0:
    p = cola_personajes.attention()
    if p.nombre_real == "Carol Danvers":
        encontrado = True
        print(f"Está en la cola como {p.nombre_superheroe}")
    aux.arrive(p)
while aux.size() > 0:
    cola_personajes.arrive(aux.attention())
if not encontrado:
    print("Carol Danvers no está en la cola.")
