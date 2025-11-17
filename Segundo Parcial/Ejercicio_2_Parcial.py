from graph import Graph

# (a) Crear un grafo NO DIRIGIDO donde:
#     - Cada vértice almacena el nombre de un personaje
#     - Cada arista representa cuántos episodios compartieron
g = Graph(is_directed=False)


# (d) Cargar al menos los personajes indicados:
personajes = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO",
    "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]

for p in personajes:
    g.insert_vertex(p)

# Relaciones (aristas) con cantidad de episodios compartidos
# Estos datos son de ejemplo; se pueden modificar.
relaciones = [
    ("Luke Skywalker", "Darth Vader", 4),
    ("Luke Skywalker", "Leia", 5),
    ("Luke Skywalker", "Han Solo", 5),
    ("Han Solo", "Leia", 6),
    ("Chewbacca", "Han Solo", 6),
    ("Chewbacca", "Leia", 3),
    ("C-3PO", "R2-D2", 9),
    ("C-3PO", "Luke Skywalker", 6),
    ("C-3PO", "Leia", 7),
    ("R2-D2", "Luke Skywalker", 6),
    ("R2-D2", "Leia", 6),
    ("Yoda", "Luke Skywalker", 3),
    ("Yoda", "Darth Vader", 1),
    ("Rey", "Kylo Ren", 3),
    ("Rey", "BB-8", 3),
    ("Leia", "Kylo Ren", 2),
]

for origen, destino, peso in relaciones:
    g.insert_edge(origen, destino, peso)

# (b) Hallar el árbol de expansión mínimo (Kruskal)
#     desde C-3PO, Yoda y Leia
print("\n(b) Arboles de expansion minimo:")

for personaje in ["C-3PO", "Yoda", "Leia"]:
    print(f"\nKruskal desde {personaje}:")
    mst = g.kruskal(personaje)
    print(mst)

# (c) Determinar el número máximo de episodios compartidos
#     e indicar todos los pares que coinciden con ese número
print("\n(c) Mayor cantidad de episodios compartidos:")

max_eps = 0
pares_maximos = []

for vertex in g:
    for edge in vertex.edges:
        if edge.weight > max_eps:
            max_eps = edge.weight
            pares_maximos = [(vertex.value, edge.value)]
        elif edge.weight == max_eps:
            pares_maximos.append((vertex.value, edge.value))

print("Maximo numero de episodios:", max_eps)
print("Pares que lo alcanzan:")
for p in pares_maximos:
    print(p)

# (e) Camino más corto usando Dijkstra
#     - desde C-3PO a R2-D2
#     - desde Yoda a Darth Vader
def reconstruir_camino(stack, destino):
    camino = []
    destino_actual = destino
    costo_total = None

    while stack.size() > 0:
        nodo = stack.pop()
        if nodo[0] == destino_actual:
            if costo_total is None:
                costo_total = nodo[1]
            camino.append(nodo[0])
            destino_actual = nodo[2]

    camino.reverse()
    return camino, costo_total

print("\n(e) Caminos mas cortos:")

# C-3PO → R2-D2
pila = g.dijkstra("C-3PO")
camino, costo = reconstruir_camino(pila, "R2-D2")
print("\nCamino mas corto de C-3PO a R2-D2:", camino, "Costo =", costo)

# Yoda → Darth Vader
pila = g.dijkstra("Yoda")
camino, costo = reconstruir_camino(pila, "Darth Vader")
print("\nCamino mas corto de Yoda a Darth Vader:", camino, "Costo =", costo)

# (f) Indicar qué personajes aparecieron en los 9 episodios
#     → interpretamos que peso = 9 indica aparición en todos
print("\n(f) Personajes que aparecieron en los 9 episodios:")

nueve_eps = set()
for vertex in g:
    for edge in vertex.edges:
        if edge.weight == 9:
            nueve_eps.add(vertex.value)
            nueve_eps.add(edge.value)

print(list(nueve_eps))
