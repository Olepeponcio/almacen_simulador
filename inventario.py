"""modulo que maneja una lista de la clase Producto
y funciones propias para la gestión de los  atributos de 
los objetos. Utiliza la clase Producto y Producto_Perecedero"""

from producto import Producto

class Inventario:
  """atributo propio de la clase Producto formato list"""
  def __init__(self, productos = None):
     self.productos = productos if productos is not None else []
    
  def agregar_producto(self, producto):
    """Añade producto si no existe ya un producto con el mismo id_producto"""
    for e in self.productos:
        if e.id_producto == producto.id_producto:
            # Ya existe, no lo añadimos de nuevo
            return
    # Si hemos terminado el bucle sin encontrar duplicado, lo añadimos una vez
    self.productos.append(producto)
    
      
  def eliminar_producto(self, id_producto):
    """in -> id_producto. 
    recorre la lista Producto, si encuentra coincidencia
    por id_producto
    elimina el elemento de la lista"""
    for e in self.productos:
      if e.id_producto == id_producto:
        self.productos.pop(e)
        
  def buscar_por_categoria(self, categoria)->list[Producto]:
    """recorre la lista de productos y devuelve una lista con 
    los productos y las categorias encontradas. out list[Producto]"""
    return [
      producto
      for producto in self.productos
      if producto.categoria == categoria
  ]
    
  def obtener_ids_unicos(self)->set[str]:
    """recorre la lista productos y añade los id_producto
    a un set str que es devuelta. out->set[str]"""
    return {p.id_producto for p in self.productos}
  
  def listar_productos(self):
    if len(self.productos) == 0:
      print("No hay productos en la lista.")
      return
    
    for p in self.productos:
      print(p) 
      
  def actualizar_stock(self, id_producto: str, cantidad: int):
    producto = None
    for p in self.productos:
      if id_producto == p.id_producto:
        producto = p
        
    if not producto == None:
      producto.stock = cantidad
    else:
      print("Producto no encontrado")