import streamlit as st
import pandas as pd
import io

# Título de la app
st.title("Tienda Tecnología - Carga de Tablas Excel")

# Instrucción para el usuario
st.write("Arrastra y suelta tus archivos Excel aquí para combinarlos:")

# Subida de archivos
uploaded_file1 = st.file_uploader("Cargar el primer archivo Excel", type=["xlsx"])
uploaded_file2 = st.file_uploader("Cargar el segundo archivo Excel", type=["xlsx"])

# Función para combinar los archivos
def combinar_archivos(file1, file2):
    if file1 is not None and file2 is not None:
        try:
            # Leer los archivos Excel
            df1 = pd.read_excel(file1)
            df2 = pd.read_excel(file2)
            
            # Verificar que ambos DataFrames tienen las mismas columnas
            if list(df1.columns) != list(df2.columns):
                st.error("Los archivos no tienen las mismas columnas. No se pueden combinar.")
                return None
            
            # Combinar los archivos
            df_combinado = pd.concat([df1, df2], ignore_index=True)

            # Mostrar el dataframe combinado
            st.write("Archivos combinados:")
            st.dataframe(df_combinado)

            return df_combinado

        except Exception as e:
            st.error(f"Error al procesar los archivos: {e}")
            return None

# Función para descargar el archivo combinado
def descargar_archivo(df):
    # Crear un archivo Excel en memoria
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Hoja1')
        writer.save()
        buffer.seek(0)
    
    # Enlace de descarga
    st.download_button(
        label="Descargar archivo combinado",
        data=buffer,
        file_name="archivo_combinado.xlsx",
        mime="application/vnd.ms-excel"
    )

# Combinación y visualización de los archivos
if uploaded_file1 and uploaded_file2:
    df_combinado = combinar_archivos(uploaded_file1, uploaded_file2)
    if df_combinado is not None:
        descargar_archivo(df_combinado)
else:
    st.info("Por favor, carga ambos archivos para combinarlos.")