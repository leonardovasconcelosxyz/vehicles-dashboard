import pandas as pd
import plotly.express as px
import streamlit as st

# Leitura dos dados (o app.py está na raiz, igual ao CSV)
car_data = pd.read_csv('vehicles_us.csv')

# Cabeçalho e descrição do app
st.header('Painel de anúncios de venda de carros')
st.write('Explore os anúncios de carros usados nos EUA: quilometragem, preço e a relação entre os dois.')

# Caixa de seleção que mostra o histograma da quilometragem
build_histogram = st.checkbox('Mostrar histograma da quilometragem')

if build_histogram:  # se a caixa for marcada
    st.write('Distribuição da quilometragem (odometer) dos anúncios')
    fig = px.histogram(car_data, x='odometer', title='Distribuição da quilometragem')
    st.plotly_chart(fig)

    # Caixa de seleção que mostra a dispersão preço × quilometragem
build_scatter = st.checkbox('Mostrar dispersão preço × quilometragem')

if build_scatter:  # se a caixa for marcada
    st.write('Relação entre a quilometragem (odometer) e o preço (price) dos anúncios')
    fig = px.scatter(car_data, x='odometer', y='price', title='Preço × quilometragem')
    st.plotly_chart(fig)