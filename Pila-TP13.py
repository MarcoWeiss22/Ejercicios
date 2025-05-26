
from stack import Stack

class IronManSuit:
    def __init__(self, modelo, pelicula, estado):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado

    def __str__(self):
        return f"{self.modelo} - {self.pelicula} - {self.estado}"

# Datos de prueba
trajes = [
    IronManSuit('Mark III', 'Iron Man', 'Dañado'),
    IronManSuit('Mark V', 'Iron Man 2', 'Impecable'),
    IronManSuit('Mark XLIV', 'Avengers: Age of Ultron', 'Dañado'),
    IronManSuit('Mark XLIV', 'Avengers: Infinity War', 'Destruido'),
    IronManSuit('Mark L', 'Avengers: Infinity War', 'Impecable'),
    IronManSuit('Mark LXXXV', 'Avengers: Endgame', 'Destruido'),
    IronManSuit('Mark XLVII', 'Spider-Man: Homecoming', 'Impecable'),
    IronManSuit('Mark XLVI', 'Capitan America: Civil War', 'Dañado'),
]

pila_trajes = Stack()
for traje in trajes:
    pila_trajes.push(traje)

# a. ¿Fue usado Mark XLIV?
print("--- a. Hulkbuster (Mark XLIV) ---")
aux = Stack()
usado_en = []
while pila_trajes.size() > 0:
    traje = pila_trajes.pop()
    if traje.modelo == 'Mark XLIV':
        usado_en.append(traje.pelicula)
    aux.push(traje)
while aux.size() > 0:
    pila_trajes.push(aux.pop())

if usado_en:
    print("Hulkbuster fue usado en:", usado_en)
else:
    print("Hulkbuster no fue usado.")

# b. Mostrar dañados sin perder pila
print("\n--- b. Modelos dañados ---")
aux = Stack()
while pila_trajes.size() > 0:
    traje = pila_trajes.pop()
    if traje.estado == 'Dañado':
        print(traje)
    aux.push(traje)
while aux.size() > 0:
    pila_trajes.push(aux.pop())

# c. Eliminar destruidos
print("\n--- c. Eliminando trajes destruidos ---")
aux = Stack()
while pila_trajes.size() > 0:
    traje = pila_trajes.pop()
    if traje.estado == 'Destruido':
        print("Eliminado:", traje)
    else:
        aux.push(traje)
while aux.size() > 0:
    pila_trajes.push(aux.pop())

# e. Agregar Mark LXXXV si no está en Endgame
print("\n--- e. Agregar Mark LXXXV en Endgame si no existe ---")
existe = False
aux = Stack()
while pila_trajes.size() > 0:
    traje = pila_trajes.pop()
    if traje.modelo == 'Mark LXXXV' and traje.pelicula == 'Avengers: Endgame':
        existe = True
    aux.push(traje)
if not existe:
    nuevo = IronManSuit('Mark LXXXV', 'Avengers: Endgame', 'Impecable')
    aux.push(nuevo)
    print("Agregado:", nuevo)
else:
    print("Ya existe Mark LXXXV en Endgame")
while aux.size() > 0:
    pila_trajes.push(aux.pop())

# f. Mostrar trajes usados en dos películas específicas
print("\n--- f. Trajes usados en películas específicas ---")
peliculas_objetivo = ['Spider-Man: Homecoming', 'Capitan America: Civil War']
aux = Stack()
while pila_trajes.size() > 0:
    traje = pila_trajes.pop()
    if traje.pelicula in peliculas_objetivo:
        print(traje.modelo)
    aux.push(traje)
while aux.size() > 0:
    pila_trajes.push(aux.pop())
