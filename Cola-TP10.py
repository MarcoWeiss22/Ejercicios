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

    def tamanio(self):
        return len(self.items)

#TDA PILA
class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop() if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.items) == 0

#FUNCIONES

def eliminar_facebook(cola):
    aux = Cola()
    while not cola.esta_vacia():
        notif = cola.desencolar()
        if notif["app"] != "Facebook":
            aux.encolar(notif)
    while not aux.esta_vacia():
        cola.encolar(aux.desencolar())

def mostrar_twitter_python(cola):
    aux = Cola()
    print("\nNotificaciones de Twitter con 'Python':")
    while not cola.esta_vacia():
        notif = cola.desencolar()
        if notif["app"] == "Twitter" and "python" in notif["mensaje"].lower():
            print(f"{notif['hora']} - {notif['mensaje']}")
        aux.encolar(notif)
    while not aux.esta_vacia():
        cola.encolar(aux.desencolar())

def filtrar_por_hora(cola, desde, hasta):
    pila = Pila()
    aux = Cola()
    count = 0
    while not cola.esta_vacia():
        notif = cola.desencolar()
        if desde <= notif["hora"] <= hasta:
            pila.apilar(notif)
            count += 1
        aux.encolar(notif)
    while not aux.esta_vacia():
        cola.encolar(aux.desencolar())
    print(f"\nNotificaciones entre {desde} y {hasta}: {count}")

#CARGA Y EJECUCIÓN

cola_notif = Cola()
cola_notif.encolar({"hora": "10:30", "app": "Twitter", "mensaje": "Buenos días"})
cola_notif.encolar({"hora": "11:45", "app": "Facebook", "mensaje": "Recordá actualizar tu perfil"})
cola_notif.encolar({"hora": "12:10", "app": "Twitter", "mensaje": "Novedades de Python 3.12"})
cola_notif.encolar({"hora": "14:30", "app": "Instagram", "mensaje": "Nuevo mensaje"})
cola_notif.encolar({"hora": "16:00", "app": "Facebook", "mensaje": "Nuevo evento"})
cola_notif.encolar({"hora": "15:45", "app": "Twitter", "mensaje": "Python es tendencia"})

eliminar_facebook(cola_notif)
mostrar_twitter_python(cola_notif)
filtrar_por_hora(cola_notif, "11:43", "15:57")
