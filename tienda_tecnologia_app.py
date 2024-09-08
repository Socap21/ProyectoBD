from dotenv import load_dotenv
import streamlit as st
import pandas as pd

# Cargar las variables de entorno
load_dotenv()

# Título de la aplicación
st.title("Tienda Tecnología - Gestión de Productos")

# Mostrar la versión de pandas
st.write("Versión de Pandas:", pd.__version__)
