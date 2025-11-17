from graph import Graph

# (a) Cada vértice representa un ambiente de la casa
ambientes = [
    "Cocina",
    "Comedor",
    "Cochera",
    "Quincho",
    "Baño 1",
    "Baño 2",
    "Habitación 1",
    "Habitación 2",
    "Sala de estar",
    "Terraza",
    "Patio"
]

# Grafo NO dirigido (según tu implementación → usar is_directed=True)
g = Graph(is_directed=True)

for a in ambientes:
    g.insert_vertex(a)

# (b) Cargar al menos 3 aristas por ambiente, y 2 ambientes
#     deben tener 5 conexiones
#     Peso = distancia en metros

# Distancias de ejemplo (coherentes para una casa)
aristas = [
    ("Cocina", "Comedor", 4),
    ("Cocina", "Baño 1", 6),
    ("Cocina", "Sala de estar", 5),

    ("Comedor", "Sala de estar", 3),
    ("Comedor", "Patio", 7),
    ("Comedor", "Terraza", 10),

    ("Cochera", "Patio", 8),
    ("Cochera", "Habitación 2", 12),
    ("Cochera", "Quincho", 6),

    ("Quincho", "Patio", 5),
    ("Quincho", "Terraza", 11),
    ("Quincho", "Comedor", 9),

    ("Baño 1", "Habitación 1", 4),
    ("Baño 1", "Sala de estar", 3),

    ("Baño 2", "Habitación 2", 4),
    ("Baño 2", "Sala de estar", 6),
    ("Baño 2", "Patio", 9),

    ("Habitación 1", "Habitación 2", 6),
    ("Habitación 1", "Sala de estar", 4),
    ("Habitación 1", "Terraza", 12),   # 5 conexiones

    ("Habitación 2", "Sala de estar", 5),
    ("Habitación 2", "Patio", 10),     # 5 conexiones

    ("Sala de estar", "Terraza", 8),
    ("Sala de estar", "Patio", 7),

    ("Terraza", "Patio", 9),
]

# cargar aristas
for a, b, w in aristas:
    g.insert_edge(a, b, w)

# (c) Obtener árbol de expansión mínima (Kruskal)
#     y sumar total de metros de cable necesarios
print("(c) Árbol de expansión mínima y total de metros necesarios:\n")

mst = g.kruskal("Cocina")
print("Árbol de expansión mínima (formato string):")
print(mst)

# sumar metros del MST
total_metros = 0
for e in mst.split(";"):
    origen, destino, metros = e.split("-")
    total_metros += int(metros)

print(f"\nTotal de metros de cable necesarios: {total_metros} m\n")


# (d) Camino más corto desde Habitación 1 → Sala de estar
print("(d) Camino más corto de Habitación 1 a Sala de estar:\n")

def reconstruir_camino(pila, destino):
    camino = []
    costo = None
    actual = destino
    while pila.size() > 0:
        nodo = pila.pop()
        nombre, dist, padre = nodo
        if nombre == actual:
            if costo is None:
                costo = dist
            camino.append(nombre)
            actual = padre
    camino.reverse()
    return camino, costo

pila = g.dijkstra("Habitación 1")
camino, metros = reconstruir_camino(pila, "Sala de estar")

print(f"Camino: {camino}")
print(f"Metros necesarios: {metros} m")
