# Definición del TDA Pila
class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop() if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.items) == 0

    def en_cima(self):
        return self.items[-1] if not self.esta_vacia() else None

    def tamanio(self):
        return len(self.items)

# Funciones para trabajar con los trajes de Iron Man
def modelo_hulkbuster(pila):
    aux = Pila()
    encontrado = False
    print("\nPelículas con el modelo Mark XLIV (Hulkbuster):")
    while not pila.esta_vacia():
        traje = pila.desapilar()
        if traje["modelo"] == "Mark XLIV":
            print(f"- {traje['pelicula']}")
            encontrado = True
        aux.apilar(traje)
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())
    if not encontrado:
        print("No se encontró el modelo Hulkbuster.")

def mostrar_danados(pila):
    aux = Pila()
    print("\nModelos que quedaron dañados:")
    while not pila.esta_vacia():
        traje = pila.desapilar()
        if traje["estado"] == "Dañado":
            print(f"- {traje['modelo']} ({traje['pelicula']})")
        aux.apilar(traje)
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())

def eliminar_destruidos(pila):
    aux = Pila()
    print("\nModelos destruidos eliminados:")
    while not pila.esta_vacia():
        traje = pila.desapilar()
        if traje["estado"] == "Destruido":
            print(f"- {traje['modelo']} ({traje['pelicula']})")
        else:
            aux.apilar(traje)
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())

def agregar_modelo(pila, modelo, pelicula, estado):
    aux = Pila()
    repetido = False
    while not pila.esta_vacia():
        traje = pila.desapilar()
        if traje["modelo"] == modelo and traje["pelicula"] == pelicula:
            repetido = True
        aux.apilar(traje)
    if not repetido:
        aux.apilar({"modelo": modelo, "pelicula": pelicula, "estado": estado})
    else:
        print(f"\nYa existe el modelo {modelo} en la película {pelicula}")
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())

def mostrar_trajes_peliculas(pila, peliculas):
    aux = Pila()
    print("\nTrajes usados en películas seleccionadas:")
    while not pila.esta_vacia():
        traje = pila.desapilar()
        if traje["pelicula"] in peliculas:
            print(f"- {traje['modelo']} ({traje['pelicula']})")
        aux.apilar(traje)
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())
