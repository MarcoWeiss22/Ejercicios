
from queue_ import Queue

def usar_la_fuerza_queue(queue, contador=0):
    if queue.size() == 0:
        return False, contador
    item = queue.attention()
    contador += 1
    if item == 'sable de luz':
        return True, contador
    return usar_la_fuerza_queue(queue, contador)

if __name__ == "__main__":
    mochila = Queue()
    for item in ['comunicador', 'comida', 'sable de luz', 'cuerda', 'manta']:
        mochila.arrive(item)

    encontrado, pasos = usar_la_fuerza_queue(mochila)
    if encontrado:
        print(f'Sable encontrado tras sacar {pasos} objetos.')
    else:
        print('No se encontró el sable.')
