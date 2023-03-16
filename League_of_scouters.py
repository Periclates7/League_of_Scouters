import streamlit as st
import pandas as pd
import pylab as plt
from PIL import Image
import webbrowser
import urllib.request

st.image("img/banner.png", use_column_width=True)

st.title('LEAGUE OF SCOUTERS')
st.header('¿Qué es League of Scouters?')





    
    
    
    
    
col1, col2, col3 = st.columns(3)

# Agregar una imagen a cada columna
with col1:
    st.markdown("[![Imagen 1](https://www.pngegg.com/es/png-ccvkn)](http://localhost:8501/Mejores_jugadores)")
with col2:
    st.markdown("[![Imagen 2](https://static.wikia.nocookie.net/leagueoflegends/images/8/84/Let%27s_Do_This_Emote.png/revision/latest?cb=20171120231623)](http://localhost:8501/Sustitutos)")
with col3:
    st.markdown("[![Imagen 3](https://static.wikia.nocookie.net/leagueoflegends/images/e/e4/Catch_Me_If_You_Can%21_Emote.png/revision/latest?cb=20171120233401)](http://localhost:8501/Graficos)")
    
    

# Cargar las imágenes localmente
imagen1 = open("img/streamlit/descarga.jpeg", "rb").read()
imagen2 = open("img/streamlit/descarga.jpeg", "rb").read()
imagen3 = open("img/streamlit/descarga.jpeg", "rb").read()

# Crear las tres columnas
col1, col2, col3 = st.columns(3)

# Agregar una imagen a cada columna y hacer que funcione como botón
if col1.image(imagen1, use_column_width=True, caption="Imagen 1"):
    st.write("<a href='http://localhost:8501/Graficos' target='_blank'>Ir a página 1</a>", unsafe_allow_html=True)

if col2.image(imagen2, use_column_width=True, caption="Imagen 2"):
    st.write("<a href='http://localhost:8501/Graficos' target='_blank'>Ir a página 2</a>", unsafe_allow_html=True)

if col3.image(imagen3, use_column_width=True, caption="Imagen 3"):
    st.write("<a href='http://localhost:8501/Graficos' target='_blank'>Ir a página 3</a>", unsafe_allow_html=True)
    
    


# Cargar la imagen localmente


# Agregar la imagen como botón y hacer que funcione como enlace



col4, col5, col6 = st.columns(3)

# Agregar una imagen a cada columna
with col4:
    if st.button("Ir a la página web1"):
        st.markdown("<a href='http://localhost:8501/Graficos'>", unsafe_allow_html=True)
        st.image(imagen1, use_column_width=True)
        st.markdown("</a>", unsafe_allow_html=True)
with col5:
    if st.button("Ir a la página web2"):
        st.markdown("<a href='http://localhost:8501/Graficos'>", unsafe_allow_html=True)
        st.image(imagen2, use_column_width=True)
        st.markdown("</a>", unsafe_allow_html=True)
with col6:    
    if st.button("Ir a la página web3"):
        st.markdown("<a href='http://localhost:8501/Graficos'>", unsafe_allow_html=True)
        st.image(imagen3, use_column_width=True)
        st.markdown("</a>", unsafe_allow_html=True)