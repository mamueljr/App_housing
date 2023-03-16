import streamlit as st
import pandas as pd
import time
#import os


from funciones import *
#from funciones import predict,housing,fetch_housing_data,load_housing_data

# Despliegue de la app
st.title('Prediccion Precios de Casas')
st.write(housing.head())
st.sidebar.header('Datos de Entrada:')
#st.header('Datos de entrada de usuario:')
#col1, col2 = st.columns(2)
#with col1:
longitude = st.sidebar.slider('Longitud', value=-122.23)
latitude = st.sidebar.slider('Latitud', value=37.88)
housing_median_age = st.sidebar.slider('Edad media de la vivienda', value=41)
total_rooms = st.sidebar.slider('Total de habitaciones', value=880)
total_bedrooms = st.sidebar.slider('Total de camas', value=129)
#with col2:
population = st.sidebar.slider('Poblacion', value=322)
households = st.sidebar.slider('Cajas', value=126)
median_income = st.sidebar.slider('Ingreso medio', value=8.33)
ocean_proximity = st.selectbox('Proximidad al mar', [
                               '1<H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'], index=3)
st.header('Modelos')
model = st.selectbox('Modelo', [
                     'Linear Regressor', 'Random Forest Regressor', 'Decision Tree Regressor'])
#result = 0

if st.button('Predecir el precio de la casa'):
    data = pd.DataFrame({
        'longitude': [longitude],
        'latitude': [latitude],
        'housing_median_age': [housing_median_age],
        'total_rooms': [total_rooms],
        'total_bedrooms': [total_bedrooms],
        'population': [population],
        'households': [households],
        'median_income': [median_income],
        'ocean_proximity': [ocean_proximity]
    })
    if model == 'Linear Regressor':
        result = predict(data, 'LR.sav')
    elif model == 'Random Forest Regressor':
        result = predict(data, 'RFR.sav')
    elif model == 'Decision Tree Regressor':
        result = predict(data, 'DTR.sav')
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        #    Update the progress bar with each iteration.
        latest_iteration.text(f'Calculando el precio de la casa {i+1}%')
        bar.progress(i + 1)
        time.sleep(0.05)

    #st.text(f'El precio predecido de la casa es: $ {result[0]}')
    st.subheader(f'El precio predecido de la casa es: $ {result[0]:.2f}')
    