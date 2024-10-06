"""
Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
formato. (Los métodos de cadena le serán de utilidad)
    
"""

def obtener_calificaciones():
    while True:
        try:
            entrada = input("Ingrese una lista de calificaciones separadas por comas: ")

            calificaciones_lista = entrada.split(',')

   
            calificaciones = [int(calificacion.strip()) for calificacion in calificaciones_lista]

            return calificaciones

        except ValueError:
            
            print("Error: Una o más calificaciones no son válidas. Solo ingrese números enteros separados por comas.")

if __name__ == '__main__':
    calificaciones = obtener_calificaciones()
    print(f"Lista de calificaciones: {calificaciones}")
