
from queue_ import Queue
from stack import Stack

class Notificacion:
    def __init__(self, hora, app, mensaje):
        self.hora = hora  # formato "HH:MM"
        self.app = app
        self.mensaje = mensaje

    def __str__(self):
        return f"[{self.hora}] {self.app}: {self.mensaje}"

def hora_en_rango(hora, inicio, fin):
    return inicio <= hora <= fin

# Datos de prueba
notificaciones = [
    Notificacion("10:00", "Facebook", "Nueva solicitud de amistad"),
    Notificacion("11:45", "Twitter", "Aprende Python con ejemplos"),
    Notificacion("12:30", "Instagram", "Nueva historia"),
    Notificacion("14:20", "Twitter", "Python es genial"),
    Notificacion("16:00", "Facebook", "Sugerencia de página"),
    Notificacion("15:30", "WhatsApp", "Mensaje de grupo"),
]

cola_notificaciones = Queue()
for n in notificaciones:
    cola_notificaciones.arrive(n)

# a. Eliminar notificaciones de Facebook
print("--- a. Eliminar Facebook ---")
aux = Queue()
while cola_notificaciones.size() > 0:
    n = cola_notificaciones.attention()
    if n.app != "Facebook":
        aux.arrive(n)
while aux.size() > 0:
    cola_notificaciones.arrive(aux.attention())
cola_notificaciones.show()

# b. Mostrar notificaciones de Twitter con 'Python'
print("\n--- b. Twitter y Python ---")
aux = Queue()
while cola_notificaciones.size() > 0:
    n = cola_notificaciones.attention()
    if n.app == "Twitter" and "Python" in n.mensaje:
        print(n)
    aux.arrive(n)
while aux.size() > 0:
    cola_notificaciones.arrive(aux.attention())

# c. Almacenar en pila notificaciones entre 11:43 y 15:57
print("\n--- c. Notificaciones entre 11:43 y 15:57 ---")
stack = Stack()
inicio = "11:43"
fin = "15:57"
aux = Queue()
contador = 0
while cola_notificaciones.size() > 0:
    n = cola_notificaciones.attention()
    if hora_en_rango(n.hora, inicio, fin):
        stack.push(n)
        contador += 1
    aux.arrive(n)
while aux.size() > 0:
    cola_notificaciones.arrive(aux.attention())

print(f"Cantidad de notificaciones en ese rango: {contador}")
