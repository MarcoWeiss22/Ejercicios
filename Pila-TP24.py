
from stack import Stack

class PersonajeMCU:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas

    def __str__(self):
        return f"{self.nombre} - {self.peliculas} películas"

# Datos de prueba
personajes = [
    PersonajeMCU('Iron Man', 10),
    PersonajeMCU('Capitan America', 9),
    PersonajeMCU('Black Widow', 8),
    PersonajeMCU('Hulk', 6),
    PersonajeMCU('Rocket Raccoon', 5),
    PersonajeMCU('Groot', 4),
    PersonajeMCU('Doctor Strange', 4),
    PersonajeMCU('Gamora', 5),
    PersonajeMCU('Drax', 5),
    PersonajeMCU('Carol Danvers', 3)
]

pila_personajes = Stack()
for personaje in personajes:
    pila_personajes.push(personaje)

# a. Posición de Rocket Raccoon y Groot
print("--- a. Posiciones ---")
aux = Stack()
posiciones = {}
pos = 1
while pila_personajes.size() > 0:
    personaje = pila_personajes.pop()
    if personaje.nombre in ['Rocket Raccoon', 'Groot']:
        posiciones[personaje.nombre] = pos
    aux.push(personaje)
    pos += 1
while aux.size() > 0:
    pila_personajes.push(aux.pop())
for nombre in ['Rocket Raccoon', 'Groot']:
    print(f"{nombre} está en la posición {posiciones.get(nombre, 'no encontrada')}")

# b. Más de 5 películas
print("\n--- b. Personajes con más de 5 películas ---")
aux = Stack()
while pila_personajes.size() > 0:
    personaje = pila_personajes.pop()
    if personaje.peliculas > 5:
        print(personaje)
    aux.push(personaje)
while aux.size() > 0:
    pila_personajes.push(aux.pop())

# c. Películas de Black Widow
print("\n--- c. Películas de Black Widow ---")
aux = Stack()
while pila_personajes.size() > 0:
    personaje = pila_personajes.pop()
    if personaje.nombre == 'Black Widow':
        print(f"Black Widow participó en {personaje.peliculas} películas")
    aux.push(personaje)
while aux.size() > 0:
    pila_personajes.push(aux.pop())

# d. Nombres que comienzan con C, D o G
print("\n--- d. Personajes que comienzan con C, D o G ---")
aux = Stack()
while pila_personajes.size() > 0:
    personaje = pila_personajes.pop()
    if personaje.nombre.startswith(('C', 'D', 'G')):
        print(personaje)
    aux.push(personaje)
while aux.size() > 0:
    pila_personajes.push(aux.pop())
