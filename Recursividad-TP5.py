
from stack import Stack

roman_values = {
    'I': 1, 'V': 5, 'X': 10,
    'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

def roman_to_decimal_stack(stack):
    if stack.size() == 0:
        return 0

    current = roman_values[stack.pop()]
    if stack.size() == 0:
        return current

    next_value = roman_values[stack.on_top()]
    if current > next_value:
        return current - roman_to_decimal_stack(stack)
    else:
        return current + roman_to_decimal_stack(stack)

def convertir_romano_con_stack(roman_str):
    stack = Stack()
    for ch in reversed(roman_str):
        stack.push(ch)
    return roman_to_decimal_stack(stack)

# Prueba
if __name__ == "__main__":
    romano = 'XIV'
    resultado = convertir_romano_con_stack(romano)
    print(f'{romano} en decimal es {resultado}')
