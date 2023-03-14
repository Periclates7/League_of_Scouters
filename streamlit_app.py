import streamlit as st
import pandas as pd
import pylab as plt
from PIL import Image
import webbrowser
import urllib.request

st.image("img/cabecera_app.png", use_column_width=True)

st.title('FINAL PROJECT')
st.header('SCOUTING FOR LEAGUE OF LEGENDS')

top_stats = pd.read_csv('data/cuadro_mando/top_stats_app.csv')
jun_stats = pd.read_csv('data/cuadro_mando/jun_stats_app.csv')
mid_stats = pd.read_csv('data/cuadro_mando/mid_stats_app.csv')
adc_stats = pd.read_csv('data/cuadro_mando/adc_stats_app.csv')
supp_stats = pd.read_csv('data/cuadro_mando/supp_stats_app.csv')

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
    #st.caption('# Best Top Players')
    #st.dataframe(top_stats)

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
    #st.caption('# Best Jungler Players')
    #st.dataframe(jun_stats)

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
    #st.caption('# Best Mid Players')
    #st.dataframe(mid_stats)

    # Filtro para mostrar datos de estadísticas o campeones
    selected_filtro = filtro.selectbox("Selecciona qué datos mostrar", ['Stats', 'Champions'])
    
    if selected_filtro == 'Stats':
        st.caption('# Best Mid Players Stats')
        st.dataframe(jun_stats)
    else:
        st.caption('# Best Mid Champions')
        st.dataframe(jun_champ)
        
elif selected_dataframe == "AD Carry":
    #st.caption('# Best ADC Players')
    #st.dataframe(adc_stats)

    # Filtro para mostrar datos de estadísticas o campeones
    selected_filtro = filtro.selectbox("Selecciona qué datos mostrar", ['Stats', 'Champions'])
    
    if selected_filtro == 'Stats':
        st.caption('# Best ADC Players Stats')
        st.dataframe(adc_stats)
    else:
        st.caption('# Best ADC Champions')
        st.dataframe(adc_champ)
        
elif selected_dataframe == "Support":
    #st.caption('# Best Support Players')
    #st.dataframe(supp_stats)

    # Filtro para mostrar datos de estadísticas o campeones
    selected_filtro = filtro.selectbox("Selecciona qué datos mostrar", ['Stats', 'Champions'])
    
    if selected_filtro == 'Stats':
        st.caption('# Best Support Players Stats')
        st.dataframe(supp_stats)
    else:
        st.caption('# Best Support Champions')
        st.dataframe(supp_champ)