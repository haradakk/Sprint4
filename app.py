import pandas as pd
import plotly.express as px
import streamlit as st

# Carregando os dados
car_data = pd.read_csv('vehicles.csv')

# Cabeçalho
st.header('Análise de anúncios de veículos')

# Botão para criar histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Histograma da quilometragem dos veículos')

    fig = px.histogram(
        car_data,
        x='odometer'
    )

    st.plotly_chart(fig, use_container_width=True)


# Botão para criar gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Relação entre preço e quilometragem dos veículos')

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price'
    )

    st.plotly_chart(fig, use_container_width=True)