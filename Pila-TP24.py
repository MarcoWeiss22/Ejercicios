# Funciones para trabajar con la pila de personajes
def posicion_personaje(pila, nombres):
    aux = Pila()
    pos = 1
    encontrados = {nombre: None for nombre in nombres}
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje["nombre"] in nombres:
            encontrados[personaje["nombre"]] = pos
        aux.apilar(personaje)
        pos += 1
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())
    print("\nPosiciones de personajes:")
    for nombre in nombres:
        print(f"{nombre}: posición {encontrados[nombre] if encontrados[nombre] else 'no encontrada'}")

def personajes_mas_de_5(pila):
    aux = Pila()
    print("\nPersonajes con más de 5 películas:")
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje["peliculas"] > 5:
            print(f"- {personaje['nombre']} ({personaje['peliculas']} películas)")
        aux.apilar(personaje)
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())

def cantidad_viuda_negra(pila):
    aux = Pila()
    cantidad = 0
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje["nombre"] == "Black Widow":
            cantidad = personaje["peliculas"]
        aux.apilar(personaje)
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())
    print(f"\nBlack Widow participó en {cantidad} películas.")

def personajes_por_letras(pila, letras):
    aux = Pila()
    print(f"\nPersonajes cuyos nombres empiezan con {', '.join(letras)}:")
    while not pila.esta_vacia():
        personaje = pila.desapilar()
        if personaje["nombre"][0].upper() in letras:
            print(f"- {personaje['nombre']}")
        aux.apilar(personaje)
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())
