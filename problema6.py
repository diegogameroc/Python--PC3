"""
Problema 6:
Una tienda de autopartes necesita un programa para catalogar sus productos, crear la clase
Catálogo y Producto, realizar un objeto dentro de un catálogo productos el cual debe tener un
método para agregar productos y otra para mostrar toda la lista de productos.
Agregar 2 funcionalidades al catálogo (por ejemplo, filtro según año) , asi mismo se puede
agregar más atributos a los productos para que se puedan hacer otras funcionalidades.
Cree 3 objetos de tipo producto y agregalos al catálogo. Colocar ejemplos empleandolos
métodos de catálogo.
    
"""
class Producto:
    def __init__(self, codproducto,nombre,año):
        self.codproducto= codproducto
        self.nombre= nombre
        self.año = año
        print("Se ha creado el producto: ", self.nombre)
        
    def __str__(self):
        return '{} ({} - {})'.format(self.codproducto, self.nombre, self.año)

class CatalogoProductos:
    productos=[]
    def __init__(self,productos=[]):
        self.productos=productos
        
#Metodos del catalogo
    def agregar(self,p):
        self.productos.append(p)
        
    def mostrar(self):
        for p in self.productos:
            print(p)
            
    def filtrar_por_año(self, año):
        print(f"Productos del año {año}:")
        hay_productos = False  
        for p in self.productos:
         if p.año == año:
            print(p)
            hay_productos = True 
        if not hay_productos:
            print("No hay productos del año especificado.")

            
if __name__ == '__main__':
# Creación de productos
    p1 = Producto("12456", "ZAPATOS ADIDAS 45", 2020)
    p2 = Producto("14566", "Zapatillas Adidas 789", 2021)
    p3 = Producto("15678", "Zapatillas Nike", 2020)

    # Creación del catálogo y adición de productos
    Catalogo_Adidas = CatalogoProductos()
    Catalogo_Adidas.agregar(p1)
    Catalogo_Adidas.agregar(p2)
    Catalogo_Adidas.agregar(p3)

    # Mostrar todos los productos en el catálogo
    Catalogo_Adidas.mostrar()

    # Filtrar productos por año
    Catalogo_Adidas.filtrar_por_año(2020)