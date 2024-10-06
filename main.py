from libro import*
from gestion import*

def mostrar_menu():
    print("\n--- Menú de Biblioteca ---")
    print("1. Agregar un libro")
    print("2. Listar los libros")
    print("3. Buscar un libro por título")
    print("4. Buscar un libro por autor")
    print("5. Salir")

def main():
    gestion = GestionBiblioteca()
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Introduce el título del libro: ")
            autor = input("Introduce el autor del libro: ")
            isbn = input("Introduce el ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            gestion.agregar_libro(libro)
            print("Libro agregado exitosamente.")

        elif opcion == "2":
            print("\nLista de libros en la biblioteca:")
            gestion.listar_libro(None)

        elif opcion == "3":
            titulo = input("Introduce el título del libro que deseas buscar: ")
            gestion.buscar_por_titulo(titulo)

        elif opcion == "4":
            autor = input("Introduce el autor del libro que deseas buscar: ")
            gestion.buscar_por_autor(autor)

        elif opcion == "5":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
