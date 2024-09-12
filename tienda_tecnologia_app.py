import streamlit as st
import pandas as pd
import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv


load_dotenv()


def conectar_db():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if connection.is_connected():
            st.success("Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        st.error(f"Error al conectar a la base de datos: {e}")
        return None



def insert_into_db(df_combinado):
    
    
    connection = conectar_db()
    if connection is None:
        return

    cursor = connection.cursor()

    insert_query = """
    INSERT INTO clientes_pedidos (ID_Cliente, Nombre, Apellido, Email, Telefono, ID_Pedido, Producto, Precio_ud, Cantidad, Precio_total)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
   
    data_to_insert = df_combinado[['ID_Cliente', 'Nombre', 'Apellido', 'Email', 'Telefono', 'ID_Pedido', 'Producto', 'Precio_ud', 'Cantidad', 'Precio_total']].to_records(index=False).tolist()
    
    try:
        cursor.executemany(insert_query, data_to_insert)
        connection.commit()
        st.success(f"{cursor.rowcount} filas insertadas exitosamente en clientes_pedidos.")
    except Error as e:
        connection.rollback()
        st.error(f"Error al insertar datos: {e}")
    finally:
        cursor.close()
        connection.close()



conexion = conectar_db()

st.title("Tienda Tecnología - Carga de Tablas Excel")


st.write("Arrastra y suelta tus archivos Excel aquí para combinarlos:")


uploaded_files = st.file_uploader("Cargar el primer archivo Excel", type=["xlsx"], accept_multiple_files=True)

if len(uploaded_files) == 2:
    try:
        file1 = uploaded_files[0]
        file2 = uploaded_files[1]

        
        dataframe_pedidos = pd.read_excel(file1)
        dataframe_clientes = pd.read_excel(file2)
        st.dataframe(dataframe_pedidos)
        st.dataframe(dataframe_clientes)

        

        
        if 'ID_Cliente' not in dataframe_pedidos.columns or 'ID_Cliente' not in dataframe_clientes.columns:
            st.error("La columna 'ID_Cliente' no está presente en ambos archivos Excel.")
        else:
            
            dataframe_combinado = pd.merge(dataframe_clientes, dataframe_pedidos, on='ID_Cliente', how='inner')

            
            
            st.dataframe(dataframe_combinado)


            
            
            if st.button('Guardar en la Base de Datos'):
                insert_into_db(dataframe_combinado)
    
    except Exception as e:
        st.error(f"Error al procesar los archivos Excel: {e}")

else:
    st.warning("Por favor, sube exactamente dos archivos Excel.")