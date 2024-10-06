
def sumar(a, b):
    try:
        return a + b
    except TypeError:
        print("Error: Tipo de dato no válido. Ambos valores deben ser números.")

def restar(a, b):
    try:
        return a - b
    except TypeError:
        print("Error: Tipo de dato no válido. Ambos valores deben ser números.")

def multiplicar(a, b):
    try:
        return a * b
    except TypeError:
        print("Error: Tipo de dato no válido. Ambos valores deben ser números.")

def dividir(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Error: No es posible dividir entre cero.")
        return a / b
    except TypeError:
        print("Error: Tipo de dato no válido. Ambos valores deben ser números.")
    except ZeroDivisionError as e:
        print(e)