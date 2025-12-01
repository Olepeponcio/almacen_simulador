from pathlib import Path
import json
import unicodedata

from producto import Producto as p 
from producto_perecedero import Producto_Perecedero as pp
from inventario import Inventario


def normalizar_categoria(texto: str) -> str:
    """Devuelve la categoría en minúsculas y sin acentos."""
    if texto is None:
        return ""
    # quitar espacios, pasar a minúsculas
    texto = texto.strip().lower()
    # eliminar acentos
    texto = ''.join(
        c for c in unicodedata.normalize("NFD", texto)
        if unicodedata.category(c) != "Mn"
    )
    return texto



def crear_inventario_desde_archivo(ruta: str) -> Inventario:
    """Lectura de archivo y devuelve un objeto del tipo inventario"""
       
    # 1. Leer lista de productos con lectura_archivo
    datos = ""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)    # paso 2 + carga JSON

    except FileNotFoundError:
        print(f"Error: no se encontró el archivo: {ruta}")
        return None

    except json.JSONDecodeError:
        print("Error: el archivo no tiene un formato JSON válido.")
        return None

    except Exception as e:
        print(f"Error inesperado: {e}")
        return None
    
    # 2. Crear objeto Inventario
    inventario = Inventario()
    # 3. Añadir cada producto al inventario
    for item in datos:
        tipo = item.get("tipo", "normal")
        # normalizamos la categoría leída del JSON
        categoria_normalizada = normalizar_categoria(item["categoria"])

        if tipo == "perecedero":
            producto = pp(
                item["id_producto"],
                item["nombre"],
                categoria_normalizada,
                item["precio"],
                item["stock"],
                item["caducidad"]
            )
        else:
            producto = p(
                item["id_producto"],
                item["nombre"],
                categoria_normalizada,
                item["precio"],
                item["stock"]
            )
        inventario.agregar_producto(producto)
    
    # 4. Devolver inventario
    return inventario
    
    
def crear_inventario_vacio() -> Inventario:
    """devuelve Inventario() sin productos"""
    inventario = Inventario()
    return inventario