import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")

st.header('Carros en venta')

hist_button = st.button("Construir histograma")

if hist_button:
    st.write(
        "Creación de histograma para el conjunto de datos de anuncios de venta de coches")

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Creación de gráfico de dispersión para el conjunto de datos de anuncios de venta de coches")

    fig_1 = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig_1, use_container_width=True)

build_histogram = st.checkbox("Construir histograma")

if build_histogram:

    st.write('Construir un histograma para la columna odómetro')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)
