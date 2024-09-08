import streamlit as st
import pandas as pd
from insert_data import insert_data_bulk  # Asumiendo que esta función está en insert_data.py

st.title("Subir datos de Productos y Clientes")

def extract_data_from_excel(excel_file, table_name):
    """Extrae la información de productos o clientes del archivo Excel proporcionado."""
    try:
        df = pd.read_excel(excel_file)
    except Exception as e:
        st.write(f"Error leyendo el archivo de Excel: {e}")
        return []

    if table_name == 'productos':
        df = df.rename(columns={
            'ProductoID': 'producto_id',
            'NombreProducto': 'nombre_producto',
            'Categoría': 'categoria',
            'Precio': 'precio',
            'Stock': 'stock'
        })
        df = df[['producto_id', 'nombre_producto', 'categoria', 'precio', 'stock']]
    elif table_name == 'clientes':
        df = df.rename(columns={
            'ClienteID': 'cliente_id',
            'Nombre': 'nombre',
            'Apellido': 'apellido',
            'Email': 'email',
            'Teléfono': 'telefono'
        })
        df = df[['cliente_id', 'nombre', 'apellido', 'email', 'telefono']]
    
    insert_data_bulk(df, table_name)  # Insertar los datos en la tabla correspondiente
    st.write(df)

# Crear un selectbox para elegir entre productos o clientes
table_name = st.selectbox("Selecciona la tabla para cargar datos", ['productos', 'clientes'])

# Subir el archivo de Excel
uploaded_file = st.file_uploader(f"Subir archivo de Excel para {table_name}", type=["xls", "xlsx"])

# Botón para procesar la carga y mostrar los valores
if st.button(f"Guardar {table_name}"):
    if uploaded_file is not None:
        extract_data_from_excel(uploaded_file, table_name)
        st.write(f"Los datos de {table_name} se han guardado correctamente.")