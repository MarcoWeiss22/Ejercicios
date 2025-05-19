def usar_la_fuerza(mochila, objetos_retirados=0):
    # Caso base: mochila vacía
    if len(mochila) == 0:
        return False, objetos_retirados

    # Sacamos el primer objeto
    objeto = mochila.pop(0)
    objetos_retirados += 1

    # ¿Encontramos el sable de luz?
    if objeto == "sable de luz":
        return True, objetos_retirados
    else:
        # Llamada recursiva con el resto de la mochila
        return usar_la_fuerza(mochila, objetos_retirados)

# Ejemplo de uso:
mochila = ["comida", "botiquín", "comunicador", "sable de luz", "manta"]

encontrado, cantidad = usar_la_fuerza(mochila.copy())

if encontrado:
    print(f"¡Sable de luz encontrado después de sacar {cantidad} objetos!")
else:
    print("No había sable de luz en la mochila.")
