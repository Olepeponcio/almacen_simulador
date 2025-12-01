from lectura_archivo import crear_inventario_desde_archivo 
from producto_perecedero import Producto_Perecedero 

RUTA_JSON_OK = "data/productos.json"
RUTA_JSON_VACIO = "data/productos_vacio.json"

def test_carga_basica():
    # 1) Ejecutar
    inventario = crear_inventario_desde_archivo(RUTA_JSON_OK)

    print(len(inventario.productos))
    for p in inventario.productos:
      print(p)

    # 2) Comprobar número de productos
    assert len(inventario.productos) > 0  # por ejemplo

    # 3) Comprobar algún producto concreto
    #    (nombre, categoría, tipo perecedero/no perecedero, etc.)
    print("OK: test_carga_basica")

def test_perecederos_y_no_perecederos():
    inventario = crear_inventario_desde_archivo(RUTA_JSON_OK)

    perecederos = [p for p in inventario.productos if isinstance(p, Producto_Perecedero)]
    no_perecederos = [p for p in inventario.productos if not isinstance(p, Producto_Perecedero)]

    # asserts básicos
    assert len(perecederos) >= 2
    assert len(no_perecederos) >= 2
    print("OK: test_perecederos_y_no_perecederos")

def test_archivo_inexistente():
    # Aquí verificas que tu función gestiona bien el error:
    # o lanza excepción concreta, o devuelve None, etc.
    print("OK: test_archivo_inexistente (ajústalo a tu lógica)")

def test_json_vacio():
    inventario = crear_inventario_desde_archivo(RUTA_JSON_VACIO)
    assert len(inventario.productos) == 0
    print("OK: test_json_vacio")

def main():
    test_carga_basica()
    test_perecederos_y_no_perecederos()
    test_archivo_inexistente()
    test_json_vacio()
    print("TODAS LAS PRUEBAS EJECUTADAS")

# if __name__ == "__main__":
#     main()
