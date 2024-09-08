import streamlit as st
import pandas as pd
from insert_data import insert_data_bulk  # Asumiendo que esta función está en insert_data.py

st.title("Subir datos de Productos y Clientes")

def extract_data_from_excel(excel_file, table_name):
    """Extrae la información de productos o clientes del archivo Excel proporcionado."""
    try:
        df = pd.read_excel(excel_file)
        if df.empty:
            st.error("El archivo está vacío. Por favor, sube un archivo con datos.")
            return
    except Exception as e:
        st.error(f"Error leyendo el archivo de Excel: {e}")
        return

    # Verificar columnas según la tabla seleccionada
    expected_columns_productos = ['ProductoID', 'NombreProducto', 'Categoría', 'Precio', 'Stock']
    expected_columns_clientes = ['ClienteID', 'Nombre', 'Apellido', 'Email', 'Teléfono']

    if table_name == 'productos' and not all(col in df.columns for col in expected_columns_productos):
        st.error("El archivo no contiene las columnas esperadas para productos.")
        return
    elif table_name == 'clientes' and not all(col in df.columns for col in expected_columns_clientes):
        st.error("El archivo no contiene las columnas esperadas para clientes.")
        return

    # Renombrar y filtrar las columnas
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

    # Insertar los datos en la tabla correspondiente
    try:
        insert_data_bulk(df, table_name)
        st.success(f"Se han guardado {len(df)} registros en la tabla {table_name} correctamente.")
        st.write(df)
    except Exception as e:
        st.error(f"Error al insertar los datos en la base de datos: {e}")

# Crear un selectbox para elegir entre productos o clientes
table_name = st.selectbox("Selecciona la tabla para cargar datos", ['productos', 'clientes'])

# Subir el archivo de Excel
uploaded_file = st.file_uploader(f"Subir archivo de Excel para {table_name}", type=["xls", "xlsx"])

# Botón para procesar la carga y mostrar los valores
if st.button(f"Guardar {table_name}"):
    if uploaded_file is not None:
        extract_data_from_excel(uploaded_file, table_name)
    else:
        st.warning("Por favor, sube un archivo antes de continuar.")