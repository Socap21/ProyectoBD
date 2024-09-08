import os
import mysql.connector
from mysql.connector import Error

# Función para insertar productos en la tabla productos
def insert_products_in_bulk(df, table_name='productos'):
    if df.empty:
        print("El DataFrame de productos está vacío. No se insertaron datos.")
        return

    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Preparar la consulta de inserción
            insert_query = f"""
            INSERT INTO {table_name} (NombreProducto, Categoria, Precio, Stock)
            VALUES (%s, %s, %s, %s)
            """

            # Convertir el DataFrame a una lista de tuplas
            products_data = df.to_records(index=False).tolist()

            # Ejecutar la consulta en bulk
            cursor.executemany(insert_query, products_data)
            
            # Confirmar la transacción
            connection.commit()

            print(f"{cursor.rowcount} filas insertadas exitosamente en productos.")

    except Error as e:
        print(f"Error al insertar productos: {e}")
        if connection:
            connection.rollback()

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


# Función para insertar clientes en la tabla clientes
def insert_clients_in_bulk(df, table_name='clientes'):
    if df.empty:
        print("El DataFrame de clientes está vacío. No se insertaron datos.")
        return

    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Preparar la consulta de inserción
            insert_query = f"""
            INSERT INTO {table_name} (Nombre, Apellido, Email, Telefono)
            VALUES (%s, %s, %s, %s)
            """

            # Convertir el DataFrame a una lista de tuplas
            clients_data = df.to_records(index=False).tolist()

            # Ejecutar la consulta en bulk
            cursor.executemany(insert_query, clients_data)
            
            # Confirmar la transacción
            connection.commit()

            print(f"{cursor.rowcount} filas insertadas exitosamente en clientes.")

    except Error as e:
        print(f"Error al insertar clientes: {e}")
        if connection:
            connection.rollback()

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


# Ejemplo de uso (supongamos que df_productos y df_clientes son DataFrames que contienen los datos):
# insert_products_in_bulk(df_productos)
# insert_clients_in_bulk(df_clientes)