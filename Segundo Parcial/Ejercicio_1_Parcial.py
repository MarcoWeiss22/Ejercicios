from pokemones_data import pokemons
from tree import BinaryTree
from queue_ import Queue

#(a) CREACIÓN DE LOS 3 ÁRBOLES: POR NOMBRE, NÚMERO Y TIPO:
arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

def insertar_en_arbol_tipo(arbol, tipo, pokemon):
    nodo = arbol.search(tipo)
    if nodo is not None:
        nodo.other_values.append(pokemon)
    else:
        arbol.insert(tipo, [pokemon])

for p in pokemons:
    arbol_nombre.insert(p["name"], p.copy())
    arbol_numero.insert(p["number"], p.copy())
    for t in p["types"]:
        insertar_en_arbol_tipo(arbol_tipo, t, p.copy())


# (b) MOSTRAR TODOS LOS DATOS DE UN POKÉMON:
#     - por número
#     - por nombre (búsqueda por proximidad)
def buscar_por_numero(n):
    nodo = arbol_numero.search(n)
    return nodo.other_values if nodo else None

def buscar_por_nombre_proximidad(sub):
    resultados = []
    sub = sub.lower()
    def _rec(root):
        if root:
            _rec(root.left)
            if sub in root.value.lower():
                resultados.append(root.other_values)
            _rec(root.right)
    _rec(arbol_nombre.root)
    return resultados

# (c) MOSTRAR TODOS LOS NOMBRES DE POKÉMON POR TIPO:
#     (fantasma, fuego, acero y eléctrico)
def pokemons_por_tipo(tipo):
    nodo = arbol_tipo.search(tipo)
    return nodo.other_values if nodo else []

# (d) LISTADO ASCENDENTE POR NÚMERO, POR NOMBRE
#     Y LISTADO POR NIVEL (BFS)
def listado_asc_numero():
    result = []
    def _in(root):
        if root:
            _in(root.left)
            result.append((root.value, root.other_values))
            _in(root.right)
    _in(arbol_numero.root)
    return result

def listado_asc_nombre():
    result = []
    def _in(root):
        if root:
            _in(root.left)
            result.append((root.value, root.other_values))
            _in(root.right)
    _in(arbol_nombre.root)
    return result

def listado_por_nivel_nombre():
    res = []
    cola = Queue()
    if arbol_nombre.root:
        cola.arrive(arbol_nombre.root)
        while cola.size() > 0:
            nodo = cola.attention()
            res.append(nodo.value)
            if nodo.left: cola.arrive(nodo.left)
            if nodo.right: cola.arrive(nodo.right)
    return res

# (e) POKÉMONS DÉBILES FRENTE A:
#     - Jolteon
#     - Lycanroc
#     - Tyrantrum
def debiles_contra(nombre_pkm):
    nodo = arbol_nombre.search(nombre_pkm)
    if nodo is None:
        return []
    tipos_atacante = nodo.other_values["types"]
    res = []
    for p in pokemons:
        if any(t in p["weaknesses"] for t in tipos_atacante):
            res.append(p["name"])
    return res

# (f) MOSTRAR TODOS LOS TIPOS Y CUÁNTOS HAY DE CADA UNO:
def contar_por_tipo():
    conteo = {}
    def _in(root):
        if root:
            _in(root.left)
            conteo[root.value] = len(root.other_values)
            _in(root.right)
    _in(arbol_tipo.root)
    return conteo

# (g) CUÁNTOS POKÉMON TIENEN MEGAEVOLUCIÓN
# (h) CUÁNTOS TIENEN FORMA GIGAMAX
def contar_mega_gigamax():
    mega = sum(1 for p in pokemons if p["mega"])
    giga = sum(1 for p in pokemons if p["gigamax"])
    return mega, giga

# RESULTADOS DEL EJERCICIO:
print("RESULTADOS DEL EJERCICIO\\n")

# (b) búsqueda por número
print("1) (b) Buscar Pokemon por numero (6):")
print(buscar_por_numero(6), "\\n")

# (b) búsqueda por proximidad en nombre
print("2) Busqueda por proximidad 'bul':")
print([p['name'] for p in buscar_por_nombre_proximidad("bul")], "\\n")

# (c) Pokémons por tipo
print("3) (c) Mostrar Pokemons por tipo (Ghost, Fire, Steel, Electric):")
for t in ["Ghost", "Fire", "Steel", "Electric"]:
    print(f"{t}: {[p['name'] for p in pokemons_por_tipo(t)]}")
print()

# (d) Listado ascendente por número
print("4) (d) Listado ascendente por numero:")
for n, p in listado_asc_numero():
    print(n, p["name"])
print()

# (d) Listado ascendente por nombre
print("Listado ascendente por nombre:")
for n, p in listado_asc_nombre():
    print(n)
print()

# (d) BFS por nombre
print("Listado por nivel por nombre (BFS):")
print(listado_por_nivel_nombre(), "\\n")

# (e) Débiles a...
print("5) (e) Pokemons debiles frente a Jolteon:")
print(debiles_contra("Jolteon"), "\\n")

print("Pokemons debiles frente a Lycanroc:")
print(debiles_contra("Lycanroc"), "\\n")

print("Pokemons debiles frente a Tyrantrum:")
print(debiles_contra("Tyrantrum"), "\\n")

# (f) Conteo de pokémon por tipo
print("6) (f) Conteo por tipo:")
print(contar_por_tipo(), "\\n")

# (g) y (h)
mega, giga = contar_mega_gigamax()
print("7) (g) Cantidad con megaevolucion:", mega)
print("8) (h) Cantidad con forma gigamax:", giga)
