import streamlit as st
import pandas as pd
import pylab as plt
from PIL import Image
import webbrowser
import urllib.request



img = Image.open("img/logo.png")
st.sidebar.image(img, caption='Título de la imagen')

filtro_grafico_player = st.sidebar.selectbox('Gráfico de jugadores', ['Selecciona un rol','Top', 'Jungle', 'Mid', 'AD Carry', 'Support'])

filtro_grafico_champ = st.sidebar.selectbox('Gráfico de campeones', ['Selecciona un rol','Top', 'Jungle', 'Mid', 'AD Carry', 'Support'])



if filtro_grafico_player == 'Top':
    imagen = Image.open('img/p_grafico_top.png')
    st.caption('# 10 mejores jugadores en Top')
    st.image(imagen, caption='Imagen Top', use_column_width=True)        

elif filtro_grafico_player == 'Jungle':
    imagen = Image.open('img/p_grafico_jun.png')
    st.caption('# 10 mejores jugadores en Jungla')
    st.image(imagen, caption='Imagen Jun', use_column_width=True)

elif filtro_grafico_player == 'Mid':
    imagen = Image.open('img/p_grafico_mid.png')
    st.caption('# 10 mejores jugadores en Mid')
    st.image(imagen, caption='Imagen Mid', use_column_width=True)

elif filtro_grafico_player == 'AD Carry':
    imagen = Image.open('img/p_grafico_adc.png')
    st.caption('# 10 mejores jugadores en ADC')
    st.image(imagen, caption='Imagen ADC', use_column_width=True)

elif filtro_grafico_player == 'Support':
    imagen = Image.open('img/p_grafico_supp.png')
    st.caption('# 10 mejores jugadores en Support')
    st.image(imagen, caption='Imagen Supp', use_column_width=True)
        

# Selector de gráficos campeones más jugados por rol
        
if filtro_grafico_champ == 'Top':
    imagen = Image.open('img/c_grafico_top.png')
    st.caption('# 10 campeones más jugados en Top')
    st.image(imagen, caption='Imagen Top c', use_column_width=True)        

elif filtro_grafico_champ == 'Jungle':
    imagen = Image.open('img/c_grafico_jun.png')
    st.caption('# 10 campeones más jugados en Jungla')
    st.image(imagen, caption='Imagen Jun c', use_column_width=True)

elif filtro_grafico_champ == 'Mid':
    imagen = Image.open('img/c_grafico_mid.png')
    st.caption('# 10 campeones más jugados en Mid')
    st.image(imagen, caption='Imagen Mid c', use_column_width=True)

elif filtro_grafico_champ == 'AD Carry':
    imagen = Image.open('img/c_grafico_adc.png')
    st.caption('# 10 campeones más jugados en ADC')
    st.image(imagen, caption='Imagen ADC c', use_column_width=True)

elif filtro_grafico_champ == 'Support':
    imagen = Image.open('img/c_grafico_supp.png')
    st.caption('# 10 campeones más jugados en Support')
    st.image(imagen, caption='Imagen Supp c', use_column_width=True)