class GestionBiblioteca:
    libros=[]
    def __init__(self,libros=[]):
        self.libros=libros
        pass

    def agregar_libro(self,libro):
        self.libros.append(libro)

    def listar_libro(self,libro):
        for libro in self.libros:
            print(libro)

    def buscar_por_titulo(self,titulo):
     print(f"Libro buscado {titulo}:")
     hay_libro = False  
     for libro in self.libros:
            if libro.titulo == titulo:
                print(libro)
                hay_libro = True 
            if not hay_libro:
                print("No hay libros con el titulo especificado")
    

    def buscar_por_autor(self,autor):
     print(f"Libro buscado {autor}:")
     hay_libro = False  
     for libro in self.libros:
            if libro.autor == autor:
                print(libro)
                hay_libro = True 
            if not hay_libro:
                print("No hay libros con el autor especificado")
            

