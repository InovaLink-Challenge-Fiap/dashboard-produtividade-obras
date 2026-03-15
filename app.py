import streamlit as st
import pandas as pd

st.title("Dashboard de Produtividade")
st.write("Olá! O dashboard está funcionando.")

df = pd.read_excel("df_diarios.xlsx")
st.dataframe(df.head(10))

















