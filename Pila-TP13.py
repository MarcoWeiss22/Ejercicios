traje = {
    "modelo": "Mark XLIV",
    "pelicula": "Avengers: Age of Ultron",
    "estado": "Dañado"
}

def modelo_hulkbuster(pila):
    aux = Pila()
    encontrado = False
    print("Películas con el modelo Mark XLIV (Hulkbuster):")
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
    print("Modelos que quedaron dañados:")
    while not pila.esta_vacia():
        traje = pila.desapilar()
        if traje["estado"] == "Dañado":
            print(f"- {traje['modelo']} ({traje['pelicula']})")
        aux.apilar(traje)
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())

def eliminar_destruidos(pila):
    aux = Pila()
    print("Modelos destruidos eliminados:")
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
        print(f"Ya existe el modelo {modelo} en la película {pelicula}")
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())

def mostrar_trajes_peliculas(pila, peliculas):
    aux = Pila()
    print("Trajes usados en películas seleccionadas:")
    while not pila.esta_vacia():
        traje = pila.desapilar()
        if traje["pelicula"] in peliculas:
            print(f"- {traje['modelo']} ({traje['pelicula']})")
        aux.apilar(traje)
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())
