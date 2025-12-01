"""modulo que crear objeto de la clase Producto.
para luego ser usado por módulo Inventario, que maneja
una lista de productos. Clase padre de la que hereda
producto perecedero"""

class Producto:
  """atributos de la clase id, nombre, categoria, precio, stck
  con funcion propia para actualizar stock y para mostrar datos en cadena str"""
  def __init__(self, id_producto, nombre, categoria, precio, stock):
    self.id_producto = str(id_producto)
    self.nombre = nombre
    self.categoria = categoria
    self.precio = int(precio)
    self.stock = int(stock)
    
  def __str__(self):
        return f"""ID: {self.id_producto}
    Nombre: {self.nombre}
    Categoría: {self.categoria}
    Precio: {self.precio} €
    Stock: {self.stock}"""
    


    