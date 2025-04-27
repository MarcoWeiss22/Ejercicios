def romano_a_decimal(romano):
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    anterior = 0
    
    for letra in reversed(romano):
        valor = valores[letra]
        if valor < anterior:
            total -= valor
        else:
            total += valor
        anterior = valor
    
    return total

# Ejemplo para tener una idea de como funciona:
numero_romano = "MCMXCIV"  # 1994
print(romano_a_decimal(numero_romano))
