from graph import Graph

# (a) Crear grafo no dirigido y cargar cada nodo con "tipo"
g = Graph(is_directed=True)  # ver nota arriba

nodos = {
    "Router 1": "router",
    "Router 2": "router",
    "Router 3": "router",
    "Switch 1": "switch",
    "Switch 2": "switch",
    "Red Hat": "notebook",
    "Debian": "notebook",
    "Arch": "notebook",
    "Manjaro": "pc",
    "Parrot": "pc",
    "Fedora": "pc",
    "Ubuntu": "pc",
    "Mint": "pc",
    "Guaraní": "servidor",
    "MongoDB": "servidor",
    "Impresora": "impresora",
}

for nombre, tipo in nodos.items():
    g.insert_vertex(nombre)
    pos = g.search(nombre, 'value')
    if pos is not None:
        g[pos].other_values = {"tipo": tipo}

# Conexiones (pesos tomados desde la figura)
relaciones = [
    ("Router 1", "Router 2", 37),
    ("Router 1", "Router 3", 43),
    ("Router 2", "Router 3", 50),
    ("Router 2", "Guaraní", 9),
    ("Router 2", "Red Hat", 25),

    ("Router 3", "Switch 2", 61),
    ("Switch 2", "Manjaro", 40),
    ("Switch 2", "Parrot", 12),
    ("Switch 2", "MongoDB", 5),
    ("Switch 2", "Arch", 56),
    ("Switch 2", "Fedora", 3),

    ("Switch 1", "Debian", 17),
    ("Switch 1", "Ubuntu", 18),
    ("Switch 1", "Mint", 80),
    ("Switch 1", "Impresora", 22),
    ("Switch 1", "Router 1", 29),
]

for a, b, w in relaciones:
    g.insert_edge(a, b, w)

# Helpers
def reconstruir_camino(pila, destino):
    camino = []
    costo = None
    actual = destino
    while pila.size() > 0:
        nodo = pila.pop()
        if nodo[0] == actual:
            if costo is None:
                costo = nodo[1]
            camino.append(nodo[0])
            actual = nodo[2]
    camino.reverse()
    return camino, costo

def camino_mas_corto(origen, destino):
    pila = g.dijkstra(origen)
    return reconstruir_camino(pila, destino)

# (b) Barrido profundidad y amplitud desde las 3 notebooks
print("(b) Barrido desde notebooks (Red Hat, Debian, Arch)\n")

for inicio in ["Red Hat", "Debian", "Arch"]:
    print(f"Barrido en profundidad desde {inicio}:")
    g.deep_sweep(inicio)
    print(f"\nBarrido en amplitud desde {inicio}:")
    g.amplitude_sweep(inicio)
    print()

# (c) Camino más corto para imprimir desde:
#     Manjaro, Red Hat, Fedora -> Impresora
print("(c) Caminos más cortos hacia la Impresora:\n")

for pc in ["Manjaro", "Red Hat", "Fedora"]:
    camino, costo = camino_mas_corto(pc, "Impresora")
    print(f"{pc} -> Impresora: Camino = {camino}, Costo = {costo}")

print()

# (d) Árbol de expansión mínima (Kruskal)
print("(d) Árbol de expansión mínima (Kruskal):\n")
mst = g.kruskal("Router 1")
print(mst)
print()

# (e) Desde qué PC (no notebook) es más corto llegar a Guaraní
print("(e) Mejor PC para llegar a Guaraní:\n")

pcs = [v.value for v in g if v.other_values and v.other_values["tipo"] == "pc"]

mejor = None
mejor_costo = None
mejor_camino = None

for pc in pcs:
    camino, costo = camino_mas_corto(pc, "Guaraní")
    if costo is not None:
        if mejor_costo is None or costo < mejor_costo:
            mejor = pc
            mejor_costo = costo
            mejor_camino = camino

print(f"Mejor PC: {mejor}  -> Camino = {mejor_camino},  Costo = {mejor_costo}")
print()

# (f) Desde qué computadora del Switch 1
#     es más corto llegar a MongoDB
print("(f) Mejor computadora del Switch 1 hacia MongoDB:\n")

pos_sw1 = g.search("Switch 1", "value")
compus = []

if pos_sw1 is not None:
    for edge in g[pos_sw1].edges:
        nombre = edge.value
        pos = g.search(nombre, "value")
        if pos is not None and g[pos].other_values:
            tipo = g[pos].other_values["tipo"]
            if tipo in ("pc", "notebook"):
                compus.append(nombre)

mejor = None
mejor_costo = None
mejor_camino = None

for c in compus:
    camino, costo = camino_mas_corto(c, "MongoDB")
    if costo is not None:
        if mejor_costo is None or costo < mejor_costo:
            mejor = c
            mejor_costo = costo
            mejor_camino = camino

print(f"Mejor computadora del Switch 1: {mejor}  -> Camino = {mejor_camino}, Costo = {mejor_costo}")
print()

# (g) Cambiar conexión impresora → Router 2
#     y repetir barrido del punto (b)
print("(g) Barrido después de mover impresora a Router 2:\n")

g.delete_edge("Switch 1", "Impresora", "value")
g.insert_edge("Router 2", "Impresora", 22)

for inicio in ["Red Hat", "Debian", "Arch"]:
    print(f"Barrido en profundidad desde {inicio}:")
    g.deep_sweep(inicio)
    print(f"\nBarrido en amplitud desde {inicio}:")
    g.amplitude_sweep(inicio)
    print()