'''
Implemente un programa que solicite al usuario una fracción, con
formato X/Y, donde cada uno de X e Y es un número entero, y luego
muestra, como un porcentaje redondeado al número entero más
cercano, donde se indicará la cantidad de combustible en el
tanque. Se debe tener en cuenta los siguientes casos:
- Colocar E en caso X/Y sea menor a 1% del total
- Colocar F en caso X/Y sea mayor a 99%.
- En otro caso, devolver el valor en porcentaje %

También debe tomar en cuenta los siguientes casos:
- X y Y deben ser números enteros
- X debe ser menor o igual a Y, y Y != 0
De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar
cualquier excepción como ValueError o ZeroDivisionError.
Ejemplos:
- Input: 4/0 Acción: Volver a preguntar al usuario dada la excepción ZeroDivisionError
- Input 1.5/3 Acción: Error dado que solo se permiten números enteros ValueError
- Input 5/4 Acción: Volver a preguntar al usuario
- Input 3/4 Output: 75%
- Input 4/4: Output F
Nota: Le será de utilidad aplicar
try:
...
except ValueError:
...
except ZeroDivisionError
'''
def obtener_fraccion():
    while True:
        try:
            entrada = input("Ingrese una fracción en formato X/Y: ")
            x1,y1=entrada.split('/')
            x2=int(x1)
            y2=int(y1)
            
            div=(x2/y2)*100
            div_Redondear= round(div)
            if div_Redondear < 1:
                print('E')
            elif div_Redondear>99:
                print('F')
            else:
                return f"{div_Redondear}%"
            
        except ValueError:
            print("Error dado que solo se permiten números enteros ValueError")
        except ZeroDivisionError:
            print('Volver a preguntar al usuario dada la excepción ZeroDivisionError')
        else:
            # si bloque try finalizo correctamente, ejecuta
            break

if __name__ == '__main__':
    print(obtener_fraccion())

