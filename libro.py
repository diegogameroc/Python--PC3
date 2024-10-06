class Libro:
    def __init__ (self,titulo,autor,isbn):
        self.titulo= titulo
        self.autor= autor
        self.isbn = isbn
        print("Se ha creado el libro: ", self.titulo)
        
    def __str__(self):
        return '{} ({} - {})'.format(self.titulo, self.autor, self.isbn)



