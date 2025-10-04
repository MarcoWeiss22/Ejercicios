from tree import BinaryTree
from creatures_data import creatures

# --- Helpers ---
def safe_list(x):
    """Devuelve lista vacía si x es None o [] ya que tree data usa listas."""
    return x if x else []

# --- 1) Cargar árbol AVL con cada criatura ---
# En cada nodo: value = name, other_values = {
#    "defeated_by": [...],
#    "description": str,
#    "captured": None o nombre del héroe/dios
# }
tree = BinaryTree()

for c in creatures:
    info = {
        "defeated_by": safe_list(c.get("defeated_by")),
        "description": "",   # inicialmente vacío; inciso (b) permite cargarlo
        "captured": None
    }
    tree.insert(c["name"], info)

print("Árbol cargado con criaturas.\n")

# ----- a) listado inorden de las criaturas y quienes la derrotaron -----
print("a) Inorden: criatura - derrotado por")
tree.in_order()
print()

# ----- b) permitir cargar una breve descripción sobre cada criatura -----
# Implemento una función para asignar descripción a una criatura por su nombre
def add_description(tree, name, description):
    node = tree.search(name)
    if node:
        node.other_values["description"] = description
        return True
    return False

# Ejemplos: añadir descripciones cortas
add_description(tree, "Medusa", "Mujer con serpientes en la cabeza; su mirada petrifica.")
add_description(tree, "Hidra de Lerna", "Monstruo con múltiples cabezas que regeneran; corta una y crecen dos.")
add_description(tree, "Talos", "Autómata de bronce que custodiaba Creta.")
print("b) Descripciones añadidas a Medusa, Hidra de Lerna y Talos.\n")

# ----- c) mostrar toda la información de la criatura Talos -----
print("c) Información completa de Talos:")
pos = tree.search("Talos")
if pos:
    print(f"{pos.value} -> {pos.other_values}")
else:
    print("Talos no encontrado.")
print()

# ----- d) determinar los 3 héroes/dioses que derrotaron mayor cantidad de criaturas -----
from collections import Counter

def top_defeaters(tree, top_n=3):
    counts = Counter()
    def __rec(root):
        if root is not None:
            for d in root.other_values["defeated_by"]:
                counts[d] += 1
            __rec(root.left)
            __rec(root.right)
    __rec(tree.root)
    return counts.most_common(top_n)

print("d) Top 3 héroes/dioses que derrotaron más criaturas:")
for name, cnt in top_defeaters(tree, 3):
    print(f"{name}: {cnt}")
print()

# ----- e) listar las criaturas derrotadas por Heracles -----
print("e) Criaturas derrotadas por Heracles:")
defeated_by_heracles = []
def __collect_heracles(root):
    if root is not None:
        __collect_heracles(root.left)
        if "Heracles" in root.other_values["defeated_by"]:
            defeated_by_heracles.append(root.value)
        __collect_heracles(root.right)
__collect_heracles(tree.root)
print("\n".join(defeated_by_heracles) if defeated_by_heracles else "Ninguna")
print()

# ----- f) listar criaturas que no han sido derrotadas -----
print("f) Criaturas no derrotadas (ningún derrotador registrado):")
not_defeated = []
def __collect_not_defeated(root):
    if root is not None:
        __collect_not_defeated(root.left)
        if not root.other_values["defeated_by"]:
            not_defeated.append(root.value)
        __collect_not_defeated(root.right)
__collect_not_defeated(tree.root)
print("\n".join(not_defeated))
print()

# ----- g) cada nodo debe tener campo 'capturada' (ya existe en other_values) -----
# Ya creado en la carga inicial: other_values["captured"] = None

# ----- h) modificar nodos (Cerbero, Toro de Creta, Cierva Cerinea, Jabalí de Erimanto)
# indicando que Heracles las atrapó (asigno captured = "Heracles") -----
for name in ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]:
    node = tree.search(name)
    if node:
        node.other_values["captured"] = "Heracles"

print("h) Nodos modificados: Cerbero, Toro de Creta, Cierva de Cerinea, Jabalí de Erimanto -> captured = 'Heracles'\n")

# ----- i) búsqueda por coincidencia (proximity) -----
# Uso proximity_search que imprime coincidencias por startswith
print("i) Búsqueda por coincidencia (startswith). Ejemplos:")
print("Buscando 'Ta' -> debería listar Talos si existe:")
tree.proximity_search("Ta")
print("Buscando 'Ja' -> debería listar Jabalí de Calidón y Jabalí de Erimanto si existen:")
tree.proximity_search("Ja")
print()

# ----- j) eliminar Basilisco y Sirenas -----
print("j) Eliminando Basilisco y Sirenas...")
val1, _ = tree.delete("Basilisco")
val2, _ = tree.delete("Sirenas")
print("Eliminado Basilisco?" , "Sí" if val1 else "No")
print("Eliminado Sirenas?" , "Sí" if val2 else "No")
print()

# ----- k) modificar nodo Aves del Estínfalo para agregar que Heracles derrotó a varias -----
pos = tree.search("Aves del Estínfalo")
if pos:
    # agregar nota en defeated_by y en description
    if "Heracles" not in pos.other_values["defeated_by"]:
        pos.other_values["defeated_by"].append("Heracles")
    pos.other_values["description"] = pos.other_values.get("description", "") + " Derrotadas por Heracles (varias)."
    print("k) Aves del Estínfalo actualizadas.")
else:
    print("k) Aves del Estínfalo no encontrada.")
print()

# ----- l) modificar el nombre Ladón por Dragón Ladón -----
# implemento renombrado: extraer datos, eliminar y reinsertar con nuevo nombre
pos = tree.search("Ladón")
if pos:
    vals = pos.other_values
    tree.delete("Ladón")
    tree.insert("Dragón Ladón", vals)
    print("l) Ladón renombrado a 'Dragón Ladón'.")
else:
    print("l) Ladón no encontrado.")
print()

# ----- m) listado por nivel (barrido por niveles) -----
print("m) Listado por nivel (BFS):")
tree.by_level()
print()

# ----- n) mostrar criaturas capturadas por Heracles -----
print("n) Criaturas con captured == 'Heracles':")
captured_by_heracles = []
def __collect_captured(root):
    if root is not None:
        __collect_captured(root.left)
        if root.other_values.get("captured") == "Heracles":
            captured_by_heracles.append(root.value)
        __collect_captured(root.right)
__collect_captured(tree.root)
print("\n".join(captured_by_heracles) if captured_by_heracles else "Ninguna")
print()

# --- Extra: Mostrar inorden final (para comprobar cambios) ---
print("Inorden final (criatura -> other_values):")
tree.in_order()
