"""modulo objeto producto, atributos propios
es usado por modulo inventario en una lista de productos
"""

from  producto import Producto

class Producto_Perecedero(Producto):
  """hereda de clase Producto. atributo de clase fecha de caducidad
  funcion propia de clase que devuelve el formato str de fecha de caducidad"""
  def __init__(self, id_producto, nombre, categoria, precio, stock, fecha_caducidad):
    super().__init__(id_producto, nombre, categoria, precio, stock)
    self.fecha_caducidad = fecha_caducidad
    
  def esta_caducado(self)->str:
    return self.fecha_caducidad