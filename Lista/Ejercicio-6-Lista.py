from list_ import List
from super_heroes_data import superheroes

class Superhero:
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain
    
    def __str__(self):
        return f"{self.name} ({self.first_appearance}) - {'Villano' if self.is_villain else 'Héroe'}"


def order_by_name(hero): return hero.name
def order_by_year(hero): return hero.first_appearance


# Crear lista de superhéroes
lista_superheroes = List()
lista_superheroes.add_criterion('name', order_by_name)
lista_superheroes.add_criterion('year', order_by_year)

# Cargar datos desde el archivo
for s in superheroes:
    lista_superheroes.append(
        Superhero(
            s["name"], s["alias"], s["real_name"],
            s["short_bio"], s["first_appearance"], s["is_villain"]
        )
    )

# a) Eliminar Linterna Verde
print("a) Eliminar Linterna Verde:")
eliminado = lista_superheroes.delete_value("Linterna Verde", "name")
print("Eliminado:", eliminado if eliminado else "No estaba en la lista")
print()

# b) Mostrar año de aparición de Wolverine
print("b) Año de aparición de Wolverine:")
pos = lista_superheroes.search("Wolverine", "name")
if pos is not None:
    print("Wolverine apareció en:", lista_superheroes[pos].first_appearance)
else:
    print("No se encontró Wolverine.")
print()

# c) Cambiar la casa de Dr. Strange a Marvel
print("c) Cambiar casa de Dr. Strange a Marvel:")
pos = lista_superheroes.search("Dr Strange", "name")
if pos is not None:
    lista_superheroes[pos].is_villain = False
    print("Casa modificada correctamente")
else:
    print("No se encontró Dr. Strange.")
print()

# d) Mostrar héroes con 'traje' o 'armadura'
print("d) Superhéroes con 'traje' o 'armadura':")
for hero in lista_superheroes:
    if "traje" in hero.short_bio.lower() or "armadura" in hero.short_bio.lower():
        print(hero.name)
print()

# e) Nombre y casa de los anteriores a 1963
print("e) Superhéroes anteriores a 1963:")
for hero in lista_superheroes:
    if hero.first_appearance < 1963:
        print(f"{hero.name} - {'Villano' if hero.is_villain else 'Héroe'}")
print()

# f) Casa de Capitana Marvel y Mujer Maravilla
print("f) Casa de Capitana Marvel y Mujer Maravilla:")
for nombre in ["Capitana Marvel", "Mujer Maravilla"]:
    pos = lista_superheroes.search(nombre, "name")
    if pos is not None:
        print(f"{nombre}: {'Villano' if lista_superheroes[pos].is_villain else 'Héroe'}")
    else:
        print(f"{nombre} no está en la lista.")
print()

# g) Mostrar toda la información de Flash y Star-Lord
print("g) Info de Flash y Star-Lord:")
for nombre in ["Flash", "Star-Lord"]:
    pos = lista_superheroes.search(nombre, "name")
    if pos is not None:
        print(lista_superheroes[pos])
    else:
        print(f"{nombre} no está en la lista.")
print()

# h) Listar superhéroes que empiezan con B, M o S
print("h) Superhéroes que comienzan con B, M o S:")
for hero in lista_superheroes:
    if hero.name.startswith(("B", "M", "S")):
        print(hero.name)
