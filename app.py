from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.title("College grades app")

import pandas as pd
print(pd.__version__)