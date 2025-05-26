#TDA COLA
class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        self.items.insert(0, item)

    def desencolar(self):
        return self.items.pop() if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.items) == 0

#FUNCIONES

def buscar_personaje(cola, personaje):
    aux = Cola()
    encontrado = False
    while not cola.esta_vacia():
        dato = cola.desencolar()
        if dato["personaje"] == personaje:
            print(f"\nEl personaje {personaje} es el superhéroe {dato['superheroe']}")
            encontrado = True
        aux.encolar(dato)
    while not aux.esta_vacia():
        cola.encolar(aux.desencolar())
    if not encontrado:
        print(f"\n{personaje} no encontrado.")

def mostrar_superheroinas(cola):
    aux = Cola()
    print("\nSuperhéroes femeninos:")
    while not cola.esta_vacia():
        dato = cola.desencolar()
        if dato["genero"] == "F":
            print(f"- {dato['superheroe']}")
        aux.encolar(dato)
    while not aux.esta_vacia():
        cola.encolar(aux.desencolar())

def mostrar_personajes_masculinos(cola):
    aux = Cola()
    print("\nPersonajes masculinos:")
    while not cola.esta_vacia():
        dato = cola.desencolar()
        if dato["genero"] == "M":
            print(f"- {dato['personaje']}")
        aux.encolar(dato)
    while not aux.esta_vacia():
        cola.encolar(aux.desencolar())

def buscar_superheroe(cola, nombre_personaje):
    aux = Cola()
    while not cola.esta_vacia():
        dato = cola.desencolar()
        if dato["personaje"] == nombre_personaje:
            print(f"\n{nombre_personaje} es {dato['superheroe']}")
        aux.encolar(dato)
    while not aux.esta_vacia():
        cola.encolar(aux.desencolar())

def mostrar_nombres_S(cola):
    aux = Cola()
    print("\nDatos de personajes o superhéroes que comienzan con 'S':")
    while not cola.esta_vacia():
        dato = cola.desencolar()
        if dato["personaje"].startswith("S") or dato["superheroe"].startswith("S"):
            print(dato)
        aux.encolar(dato)
    while not aux.esta_vacia():
        cola.encolar(aux.desencolar())

def verificar_carol_danvers(cola):
    aux = Cola()
    encontrado = False
    while not cola.esta_vacia():
        dato = cola.desencolar()
        if dato["personaje"] == "Carol Danvers":
            print(f"\nCarol Danvers es {dato['superheroe']}")
            encontrado = True
        aux.encolar(dato)
    while not aux.esta_vacia():
        cola.encolar(aux.desencolar())
    if not encontrado:
        print("\nCarol Danvers no se encuentra en la cola.")

#CARGA Y EJECUCIÓN

cola_mcu = Cola()
cola_mcu.encolar({"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"})
cola_mcu.encolar({"personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"})
cola_mcu.encolar({"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"})
cola_mcu.encolar({"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"})
cola_mcu.encolar({"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"})
cola_mcu.encolar({"personaje": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"})

buscar_personaje(cola_mcu, "Carol Danvers")
mostrar_superheroinas(cola_mcu)
mostrar_personajes_masculinos(cola_mcu)
buscar_superheroe(cola_mcu, "Scott Lang")
mostrar_nombres_S(cola_mcu)
verificar_carol_danvers(cola_mcu)
