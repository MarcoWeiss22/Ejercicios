
superheroes = [
    "Iron Man", "Thor", "Hulk", "Black Widow", "Hawkeye",
    "Doctor Strange", "Spider-Man", "Black Panther", "Ant-Man",
    "Wasp", "Vision", "Scarlet Witch", "Falcon",
    "Winter Soldier", "Capitan America"
]

# Función recursiva para buscar "Capitan America"
def buscar_capitan_america(lista, index=0):
    if index >= len(lista):
        return False
    if lista[index] == "Capitan America":
        return True
    return buscar_capitan_america(lista, index + 1)

# Función recursiva para listar todos los superhéroes
def listar_superheroes(lista, index=0):
    if index >= len(lista):
        return
    print(lista[index])
    listar_superheroes(lista, index + 1)

if __name__ == "__main__":
    print("Buscar Capitan America")
    if buscar_capitan_america(superheroes):
        print("Capitan America está en la lista.")
    else:
        print("Capitan America NO está en la lista.")

    print("\nListado de Superhéroes:")
    listar_superheroes(superheroes)
