
from queue_ import Queue
from list_ import List
from super_heroes_data import superheroes

def order_by_name(hero):
    return hero["name"]

def order_by_real_name(hero):
    return hero["real_name"] or ""

def order_by_appearance(hero):
    return hero["first_appearance"]

lista_heroes = List()
lista_heroes.add_criterion("name", order_by_name)
lista_heroes.add_criterion("real_name", order_by_real_name)
lista_heroes.add_criterion("first_appearance", order_by_appearance)

for hero in superheroes:
    lista_heroes.append(hero)

# A. Listado ordenado ascendente por nombre
def listar_por_nombre():
    lista_heroes.sort_by_criterion("name")
    print("A. Personajes ordenados por nombre:")
    for s in lista_heroes:
        print(s["name"])

# B. Posición de The Thing y Rocket Raccoon
def buscar_posiciones():
    print("\nB. Posiciones:")
    for name in ["The Thing", "Rocket Raccoon"]:
        index = lista_heroes.search(name, "name")
        if index is not None:
            print(f"{name} está en la posición {index + 1}")

# C. Listar todos los villanos
def listar_villanos():
    print("\nC. Villanos:")
    for s in lista_heroes:
        if s["is_villain"]:
            print(s["name"])

# D. Villanos en cola y mostrar los anteriores a 1980
def villanos_pre_1980():
    print("\nD. Villanos antes de 1980:")
    cola_villanos = Queue()
    for s in lista_heroes:
        if s["is_villain"]:
            cola_villanos.arrive(s)
    while cola_villanos.size() > 0:
        v = cola_villanos.attention()
        if v["first_appearance"] < 1980:
            print(f'{v["name"]} - {v["first_appearance"]}')

# E. Superhéroes que comienzan con Bl, G, My, W
def listar_por_prefijos():
    print("\nE. Superhéroes con prefijos (Bl, G, My, W):")
    prefijos = ("Bl", "G", "My", "W")
    for s in lista_heroes:
        if s["name"].startswith(prefijos):
            print(s["name"])

# F. Ordenar por nombre real
def ordenar_por_nombre_real():
    print("\nF. Ordenado por nombre real:")
    lista_heroes.sort_by_criterion("real_name")
    for s in lista_heroes:
        print(f'{s["real_name"]} ({s["name"]})')

# G. Ordenar por año de aparición
def ordenar_por_aparicion():
    print("\nG. Ordenado por año de aparición:")
    lista_heroes.sort_by_criterion("first_appearance")
    for s in lista_heroes:
        print(f'{s["name"]} - {s["first_appearance"]}')

# H. Modificar nombre real de Ant Man
def modificar_antman():
    print("\nH. Modificando nombre real de Ant Man...")
    index = lista_heroes.search("Ant Man", "name")
    if index is not None:
        print(f'Antes: {lista_heroes[index]["real_name"]}')
        lista_heroes[index]["real_name"] = "Scott Lang"
        print(f'Después: {lista_heroes[index]["real_name"]}')

# I. Personajes con 'time-traveling' o 'suit' en bio
def listar_por_bio_keywords():
    print("\nI. Biografías con 'time-traveling' o 'suit':")
    for s in lista_heroes:
        bio = s["short_bio"].lower()
        if "time-traveling" in bio or "suit" in bio:
            print(s["name"])

# J. Eliminar Electro y Baron Zemo
def eliminar_personajes():
    print("\nJ. Eliminando Electro y Baron Zemo:")
    for name in ["Electro", "Baron Zemo"]:
        eliminado = lista_heroes.delete_value(name, "name")
        if eliminado:
            print(f'Eliminado: {eliminado["name"]} ({eliminado["real_name"]})')

if __name__ == "__main__":
    listar_por_nombre()
    buscar_posiciones()
    listar_villanos()
    villanos_pre_1980()
    listar_por_prefijos()
    ordenar_por_nombre_real()
    ordenar_por_aparicion()
    modificar_antman()
    listar_por_bio_keywords()
    eliminar_personajes()
