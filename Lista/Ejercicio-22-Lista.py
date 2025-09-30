from list_ import List
from jedis_data import jedis

class Jedi:
    def __init__(self, name, masters, lightsaber_colors, species):
        self.name = name
        self.masters = masters
        self.lightsaber_colors = lightsaber_colors
        self.species = species

    def __str__(self):
        return (f"Nombre: {self.name}\n"
                f"Maestros: {', '.join(self.masters) if self.masters else 'Ninguno'}\n"
                f"Colores sable: {', '.join(self.lightsaber_colors)}\n"
                f"Especie: {self.species}\n")

# --- Criterios ---
def order_by_name(jedi): return jedi.name
def order_by_species(jedi): return jedi.species

# Crear lista de Jedi
lista_jedi = List()
lista_jedi.add_criterion('name', order_by_name)
lista_jedi.add_criterion('species', order_by_species)

for j in jedis:
    lista_jedi.append(Jedi(
        j["name"], j["masters"], j["lightsaber_colors"], j["species"]
    ))

# a) Listado ordenado por nombre y especie
print("a) Listado ordenado por nombre:")
lista_jedi.sort_by_criterion('name')
lista_jedi.show()

print("\nListado ordenado por especie:")
lista_jedi.sort_by_criterion('species')
lista_jedi.show()
print()

# b) Info de Ahsoka Tano y Kit Fisto
print("b) Información de Ahsoka Tano y Kit Fisto:\n")
for nombre in ["Ahsoka Tano", "Kit Fisto"]:
    pos = lista_jedi.search(nombre, 'name')
    print(lista_jedi[pos] if pos is not None else f"{nombre} no encontrado.\n")
print()

# c) Padawans de Yoda y Luke Skywalker
print("c) Padawans de Yoda y Luke Skywalker:\n")
for maestro in ["Yoda", "Luke Skywalker"]:
    print(f"Padawans de {maestro}:")
    for jedi in lista_jedi:
        if maestro in jedi.masters:
            print(" -", jedi.name)
    print()
print()

# d) Jedi humanos o twi'lek
print("d) Jedi humanos o twi'lek:\n")
for jedi in lista_jedi:
    if jedi.species.lower() in ["humano", "twi'lek"]:
        print(jedi.name, "-", jedi.species)
print()

# e) Jedi que comienzan con A
print("e) Jedi que comienzan con A:\n")
for jedi in lista_jedi:
    if jedi.name.startswith("A"):
        print(jedi.name)
print()

# f) Jedi que usaron más de un color
print("f) Jedi que usaron más de un color de sable:\n")
for jedi in lista_jedi:
    if len(jedi.lightsaber_colors) > 1:
        print(jedi.name, "-", jedi.lightsaber_colors)
print()

# g) Jedi con sable amarillo o violeta
print("g) Jedi con sable amarillo o violeta:\n")
for jedi in lista_jedi:
    if "amarillo" in jedi.lightsaber_colors or "violeta" in jedi.lightsaber_colors:
        print(jedi.name, "-", jedi.lightsaber_colors)
print()

# h) Padawans de Qui-Gon Jinn y Mace Windu
print("h) Padawans de Qui-Gon Jinn y Mace Windu:\n")
for maestro in ["Qui-Gon Jinn", "Mace Windu"]:
    print(f"Padawans de {maestro}:")
    found = False
    for jedi in lista_jedi:
        if maestro in jedi.masters:
            print(" -", jedi.name)
            found = True
    if not found:
        print("   Ninguno")
    print()
