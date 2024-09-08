import os
import mysql.connector
from mysql.connector import Error

def get_all_the_products():
    """Función para obtener todos los productos de la base de datos"""
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        products = []
        
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            query = """
                SELECT p.ProductoID, p.NombreProducto, p.Categoria, p.Precio, p.Stock FROM productos as p;
            """
            cursor.execute(query)
            products = cursor.fetchall()
            cursor.close()
        
    except Error as e:
        print(f"Error al obtener los productos de la base de datos: {e}")
    
    finally:
        if connection.is_connected():
            connection.close()
    
    return products
    
        