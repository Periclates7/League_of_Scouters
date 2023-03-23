import streamlit as st
import pandas as pd
from PIL import Image
import webbrowser
import urllib.request

st.set_page_config(page_icon = '🎮', page_title = 'LoS - Mejores invocadores')

st.image("img/banner.png", use_column_width=True)

st.header('Ranking de jugadores por rol')

top_stats = pd.read_csv('data/visualizacion/top_ss.csv')
jun_stats = pd.read_csv('data/visualizacion/jun_ss.csv')
mid_stats = pd.read_csv('data/visualizacion/mid_ss.csv')
adc_stats = pd.read_csv('data/visualizacion/adc_ss.csv')
supp_stats = pd.read_csv('data/visualizacion/supp_ss.csv')

top_champ = pd.read_csv('data/cuadro_mando/top_champ_app.csv')
jun_champ = pd.read_csv('data/cuadro_mando/jun_champ_app.csv')
mid_champ = pd.read_csv('data/cuadro_mando/mid_champ_app.csv')
adc_champ = pd.read_csv('data/cuadro_mando/adc_champ_app.csv')
supp_champ = pd.read_csv('data/cuadro_mando/supp_champ_app.csv')

dataframes_base = ['Top', 'Jungle', 'Mid', 'AD Carry', 'Support']
dataframes_filtro = ['Stats', 'Champions']



# Creamos los filtros
rol, filtro = st.columns(2)

# Filtro por rol
selected_dataframe = rol.selectbox("Selecciona un rol", ['Top', 'Jungle', 'Mid', 'AD Carry', 'Support'])

# Mostramos el dataframe correspondiente al rol seleccionado
if selected_dataframe == "Top":
   
    # Filtro para mostrar datos de estadísticas o campeones
    selected_filtro = filtro.selectbox("Selecciona qué datos mostrar", ['Stats', 'Champions'])

    # Mostramos los datos correspondientes al filtro seleccionado
    if selected_filtro == 'Stats':
        st.caption('# Best Top Players Stats')
        st.dataframe(top_stats)
    else:
        st.caption('# Best Top Champions')
        st.dataframe(top_champ)

elif selected_dataframe == "Jungle":
    
    # Filtro para mostrar datos de estadísticas o campeones
    selected_filtro = filtro.selectbox("Selecciona qué datos mostrar", ['Stats', 'Champions'])

    # Mostramos los datos correspondientes al filtro seleccionado
    if selected_filtro == 'Stats':
        st.caption('# Best Jungle Players Stats')
        st.dataframe(jun_stats)
    else:
        st.caption('# Best Jungle Champions')
        st.dataframe(jun_champ)

elif selected_dataframe == "Mid":
   
    # Filtro para mostrar datos de estadísticas o campeones
    selected_filtro = filtro.selectbox("Selecciona qué datos mostrar", ['Stats', 'Champions'])
    
    if selected_filtro == 'Stats':
        st.caption('# Best Mid Players Stats')
        st.dataframe(mid_stats)
    else:
        st.caption('# Best Mid Champions')
        st.dataframe(mid_champ)
        
elif selected_dataframe == "AD Carry":
   
    # Filtro para mostrar datos de estadísticas o campeones
    selected_filtro = filtro.selectbox("Selecciona qué datos mostrar", ['Stats', 'Champions'])
    
    if selected_filtro == 'Stats':
        st.caption('# Best ADC Players Stats')
        st.dataframe(adc_stats)
    else:
        st.caption('# Best ADC Champions')
        st.dataframe(adc_champ)
        
elif selected_dataframe == "Support":

    # Filtro para mostrar datos de estadísticas o campeones
    selected_filtro = filtro.selectbox("Selecciona qué datos mostrar", ['Stats', 'Champions'])
    
    if selected_filtro == 'Stats':
        st.caption('# Best Support Players Stats')
        st.dataframe(supp_stats)
    else:
        st.caption('# Best Support Champions')
        st.dataframe(supp_champ)