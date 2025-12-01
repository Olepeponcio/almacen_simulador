import os
from enum import Enum, auto

from lectura_archivo import crear_inventario_desde_archivo as ia 
from lectura_archivo import crear_inventario_vacio as iv 
from inventario import Inventario
from producto import Producto

#declaracion enum para gestion estados
class MenuOpciones(Enum):
  """enum para gestionar estados según opcion en el 
  bucle principal"""
  AGREGAR     =   auto()
  ELIMINAR    =   auto()
  BUSCAR      =   auto()
  LISTAR      =   auto()
  ACTUALIZAR  =   auto()
  MOSTRAR     =   auto()
  SALIR       =   auto()
  

#declaración variables
opcion = ""
inventario = None
ruta_productos = "data\productos.json"


def limpiar_pantalla():
  """detecta el SO y realiza un cls o un clear de la consola"""
  os.system('cls' if os.name == 'nt' else 'clear')

#mapear enum de opciones en un set
def parse_opcion(op):
  """mapea el menu según argumento in->str
  en un diccionario para devolver la opción out->Enum"""
  mapa = {
      "1": MenuOpciones.AGREGAR,
      "2": MenuOpciones.ELIMINAR,
      "3": MenuOpciones.BUSCAR,
      "4": MenuOpciones.LISTAR,
      "5": MenuOpciones.ACTUALIZAR,
      "6": MenuOpciones.SALIR
  }
  return mapa.get(op)

#funcion para mostrar el menu
def mostrar_menu():
  """imprime en pantalla y muestra el menu de opciones
  encadena con otra función que controla el input"""
  print("Elija una opción: ")
  print(f"""
[1] Agregar Producto
[2] Eliminar Producto
[3] Buscar por categoría
[4] Listar Productos
[5] Actualizar Stock
[6] Salir
        """)



def agregar_producto_datos(inventario):
    """in -> id_producto, nombre, categoria, precio, stock
    inventario - para comprobar el id o derivar a actualizar stock
    out -> dict o None si ya existe
    """
    datos = {
        "id_producto": None,
        "nombre": None,
        "categoria": None,
        "precio": None,
        "stock": None,
    }

    # solicitar id nuevo
    id_producto = input("Introduzca nuevo ID: ").strip()

    # comprobar si el id ya existe
    for p in inventario.productos:
        if id_producto == p.id_producto:
            print("No se ha creado ningún producto (ID duplicado).")
            return None
          
    # si llegamos aquí, el id no está repetido
    datos["id_producto"] = id_producto

    nombre = input("Nombre: ")
    categoria = input("Categoria: ")
    precio = input("Precio: ")
    stock = input("Stock: ")

    datos["nombre"] = nombre
    datos["categoria"] = categoria
    datos["precio"] = precio
    datos["stock"] = stock

    return datos


#declarar el bucle principal
def bucle_principal(inventario):
    estado_actual: MenuOpciones | None = None

    while True:
        mostrar_menu()
        entrada = input("Selecciona una opción: ")
        estado_actual = parse_opcion(entrada)

        if estado_actual is None:
            print("Opción no válida. Inténtalo de nuevo.\n")
            continue

        match estado_actual:
            case MenuOpciones.AGREGAR:
                #limpiar pantalla
                limpiar_pantalla()
                # Estado: AGREGAR
                producto = None #recogera los datos del diccionario
                datos = agregar_producto_datos(inventario)
                #si devuelve None 
                 # Si la función ha devuelto None (id duplicado), no seguimos
                if datos is None:
                    print("vaya a la opción actualizar stock")
                    continue  # volvemos al menú principal
                 # TRY: llamar al método del inventario
                try:
                    producto = Producto(
                        datos["id_producto"],
                        datos["nombre"],
                        datos["categoria"],
                        datos["precio"],
                        datos["stock"]
                    )
                    print("Producto añadido correctamente.")

                except Exception as e:
                    print(f"Error al agregar producto: {e}")
                
                #agregar el objeto a la lista de inventario
                inventario.agregar_producto(producto)

            case MenuOpciones.ELIMINAR:
                # Estado: ELIMINAR
                id_producto = input("introduzca id_producto para eliminar: ")
                # eliminar_producto(inventario)
                try:
                  inventario.eliminar_producto(id_producto)
                  print("Producto eliminado correctamente.")
                except Exception as e:
                  print(f"No se ha podido eliminar producto del inventario. error: {e}")
                

            case MenuOpciones.BUSCAR:
                #input para solicitar categoria
                categoria = input("Introduzca categoria: ")
                # Estado: BUSCAR
                try:
                  productos = inventario.buscar_por_categoria(categoria)
                  for p in productos:
                    print(p)
                except Exception as e:
                  print(f"Categoria introducida no válida. Error: {e}")

            case MenuOpciones.LISTAR:
                limpiar_pantalla()
                inventario.listar_productos()
              
            case MenuOpciones.ACTUALIZAR:
                # Estado: ACTUALIZAR
                id_producto = input("Introduzca ID: ")
                _cantidad = input("Introduzca la cantidad: ")
                cantidad = int(_cantidad)
                inventario.actualizar_stock(id_producto, cantidad)

            case MenuOpciones.SALIR:
                print("Saliendo del programa...")
                break



#cargar datos iniciales de inventario
print("*"*20)
print("¿CARGAR DATOS DE ARCHIVO?")
print("SI: (s) \tNO: (n)")
print("*"*20)
#si crear objeto inventario con lista inicial de productos/productos perecederos
_opcion = input("Introduzca su seleccion: ")
opcion = _opcion.upper()
print(opcion)

if not opcion =="S" and not opcion =="N":
  print("opción introducida no válida.")
else:
  if opcion == "S":
    #cargar inventario de archivo en lista inventario.productos
    inventario = ia(ruta_productos)
  elif opcion == "N":
    #crear inventario vacio con lista inventario.productos = []
    inventario = iv()
  
#bucle principal
bucle_principal(inventario)


