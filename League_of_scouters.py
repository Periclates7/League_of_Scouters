import streamlit as st
import pandas as pd
import pylab as plt
from PIL import Image
import webbrowser
import urllib.request


st.set_page_config(page_icon = '🎮', page_title = 'League of Scouters')

st.image("img/banner.png", use_column_width=True)

#st.title('LEAGUE OF SCOUTERS')
col_1, col_2 = st.columns(2)

with col_1:    
    st.header('¿Qué es League of Scouters?')
    st.write('###### League of Scouters es una plataforma diseñada para ayudar a los equipos profesionales de League of Legends a encontrar jugadores con potencial para fichar. La plataforma utiliza datos y estadísticas para identificar a los jugadores que destacan en su juego y que podrían tener un buen desempeño en un entorno profesional. Esto permite a los equipos encontrar y contratar a nuevos talentos de manera más efectiva, lo que puede llevar a un mayor éxito en el ámbito competitivo.')

with col_2:
    st.image("img/streamlit/fiora.png", use_column_width=True)
    
st.write('\n')
st.write('\n')



col_3, col_4 = st.columns(2)

with col_3:
    st.image("img/streamlit/blitz.png", use_column_width=True)

with col_4:    
    st.markdown("<h2 style='text-align: right;'>¿Cómo utilizar League of Scouters?</h2>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: right;'>Mi aplicación cuenta con varias secciones. La primera es un ranking de jugadores potenciales que funciona a través de filtros por rol, estadísticas y campeones. La segunda sección es un recomendador de sustitutos que también utiliza filtros por rol y por jugadores profesionales a reemplazar. Por último, la tercera sección es un banco de gráficos donde se pueden visualizar las estadísticas de manera rápida y clara.</h6>", unsafe_allow_html=True)






    
    
    

st.write('\n')
st.write('\n')


col4, col5, col6 = st.columns(3)

# Agregar una imagen a cada columna
with col4:
    if st.button("Mejores jugadores"):
        webbrowser.open_new_tab('http://localhost:8501/Mejores_jugadores')
with col5:
    if st.button("Reemplazos"):
        webbrowser.open_new_tab('http://localhost:8501/Buscador_de_reemplazos')
with col6:    
    if st.button("Banco de gráficos"):
        webbrowser.open_new_tab('http://localhost:8501/Graficos')