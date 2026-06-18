import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv('vehicles.csv')
hist_button = st.button('Criar histograma')

st.header('Car sales')

if hist_button:
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
