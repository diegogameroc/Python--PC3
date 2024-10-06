from problema3 import*
from problema4 import*

def validar_entrada(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Error: El valor debe ser un número positivo.")
        except ValueError:
            print("Error: Ingresa un valor valido.")

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            radio = validar_entrada("Ingrese el radio del círculo: ")
            circulo = CIRCULO(radio)
            circulo.Imprimir()
        
        elif opcion == "2":
            largo = validar_entrada("Ingrese el largo del rectángulo: ")
            ancho = validar_entrada("Ingrese el ancho del rectángulo: ")
            rectangulo = RECTANGULO(largo, ancho)
            rectangulo.Imprimir()
        
        elif opcion == "3":
            lado = validar_entrada("Ingrese el lado del cuadrado: ")
            cuadrado = CUADRADO(lado)
            cuadrado.Imprimir()
        
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opcion incorrecta, elige de nuevo.")


if __name__ == '__main__':
    menu()