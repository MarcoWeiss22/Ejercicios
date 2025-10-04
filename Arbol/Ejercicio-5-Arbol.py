from tree import BinaryTree
from super_heroes_data import superheroes

# Crear árbol principal con héroes y villanos
mcu_tree = BinaryTree()

# a) Cargar el árbol con nombre y booleano is_villain
for character in superheroes:
    mcu_tree.insert(character["name"], {"is_villain": character["is_villain"]})

print("Árbol MCU cargado con héroes y villanos\n")

# b) Listar villanos alfabéticamente
print("b) Villanos en orden alfabético:")
mcu_tree.villain_in_order()
print()

# c) Superhéroes que empiezan con C
print("c) Superhéroes que comienzan con 'C':")
def heroes_starting_with_C(root):
    if root is not None:
        heroes_starting_with_C(root.left)
        if root.value.startswith("C") and root.other_values["is_villain"] == False:
            print(root.value)
        heroes_starting_with_C(root.right)

heroes_starting_with_C(mcu_tree.root)
print()

# d) Contar superhéroes
print("d) Total de superhéroes:")
total_heroes = mcu_tree.count_heroes()
print("Total de superhéroes:", total_heroes)
print()

# e) Búsqueda por proximidad para Doctor Strange
print("e) Buscar Doctor Strange por proximidad (mal cargado):")
mcu_tree.proximity_search("Dr")
print("\nModificando nombre...")

# Intentamos eliminar el nombre incorrecto y agregar el correcto
value, other_values = mcu_tree.delete("Dr Strannnnnge")
if value is not None:
    other_values["is_villain"] = False
    mcu_tree.insert("Doctor Strange", other_values)
    print("Doctor Strange corregido.")
else:
    print("No se encontró el nombre mal cargado.")
print()

# f) Listar superhéroes en orden descendente
print("f) Superhéroes en orden descendente:")
def heroes_descendente(root):
    if root is not None:
        heroes_descendente(root.right)
        if root.other_values["is_villain"] == False:
            print(root.value)
        heroes_descendente(root.left)

heroes_descendente(mcu_tree.root)
print()

# g) Generar bosque (un árbol de héroes y otro de villanos)
heroes_tree = BinaryTree()
villains_tree = BinaryTree()

mcu_tree.divide_tree(heroes_tree, villains_tree)

# I. Determinar cuántos nodos tiene cada árbol
def contar_nodos(tree):
    def __contar(root):
        if root is None:
            return 0
        return 1 + __contar(root.left) + __contar(root.right)
    return __contar(tree.root)

print("g-I) Cantidad de nodos:")
print("Héroes:", contar_nodos(heroes_tree))
print("Villanos:", contar_nodos(villains_tree))
print()

# II. Barrido alfabético de cada árbol
print("g-II) Barrido ordenado de héroes:")
heroes_tree.in_order()
print("\nBarrido ordenado de villanos:")
villains_tree.in_order()
print()
