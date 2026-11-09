import pandas as pd
import plotly.express as px
import streamlit as st

# Leitura dos dados (o app.py está na raiz, igual ao CSV)
car_data = pd.read_csv('vehicles_us.csv')

# Cabeçalho e descrição do app
st.header('Painel de anúncios de venda de carros')
st.write('Explore os anúncios de carros usados nos EUA: quilometragem, preço e a relação entre os dois.')
