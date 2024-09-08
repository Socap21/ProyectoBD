import os
import mysql.connector
from mysql.connector import Error

def get_all_the_products():
    """Función para obtener todos los productos de la base de datos"""
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    products = []

    if connection.is_connected():
        try:
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT p.ProductoID, p.NombreProducto, p.Categoría, p.Precio, p.Stock FROM productos as p;
            """
            cursor.execute(query)
            products = cursor.fetchall()
            print(products)
        except Error as e:
            print(f"Error al obtener los productos de la base de datos: {e}")
        finally:
            cursor.close()
            return products
    
        