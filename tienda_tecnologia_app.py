import streamlit as st
import pandas as pd
import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv 
load_dotenv()

# Función para conectarse a la base de datos
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

# Conectar a la base de datos al iniciar la app
conexion = conectar_db()

# Título de la app
st.title("Tienda Tecnología - Carga de Tablas Excel")

# Instrucción para el usuario
st.write("Arrastra y suelta tus archivos Excel aquí para combinarlos:")

# Subida de archivos
uploaded_files = st.file_uploader("Cargar el primer archivo Excel", type=["xlsx"], accept_multiple_files=True)

if len(uploaded_files) == 2:
    try:
        file1 = uploaded_files[0]
        file2 = uploaded_files[1]

        dataframe_productos=pd.read_excel(file1)
        dataframe_clientes=pd.read_excel(file2)

        st.dataframe(dataframe_productos)
        st.dataframe(dataframe_clientes)


        dataframe_combine=dataframe_clientes['Nombre']
        st.dataframe(dataframe_combine)

        if st.button('Save to Database'):
            insert_into_db(df_final)
            st.success('Data successfully saved to the database.')

    except Exception as e:
        st.error(f"Error processing the Excel files: {e}")

else:
    st.warning("Please upload exactly two Excel files.")