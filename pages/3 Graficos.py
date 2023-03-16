import streamlit as st
import pandas as pd
import pylab as plt
from PIL import Image
import webbrowser
import urllib.request
import altair as alt


st.set_page_config(page_title="LoS - Banco de gráficos", page_icon = '🎮')

# Carga dfs
top = pd.read_csv('data/visualizacion/top_ss.csv')
jun = pd.read_csv('data/visualizacion/jun_ss.csv')
mid = pd.read_csv('data/visualizacion/mid_ss.csv')
adc = pd.read_csv('data/visualizacion/adc_ss.csv')
supp = pd.read_csv('data/visualizacion/supp_ss.csv')

conteo_top = pd.read_csv('data/visualizacion/conteo_champs/conteo_champs_top.csv')
conteo_jun = pd.read_csv('data/visualizacion/conteo_champs/conteo_champs_jun.csv')
conteo_mid = pd.read_csv('data/visualizacion/conteo_champs/conteo_champs_mid.csv')
conteo_adc = pd.read_csv('data/visualizacion/conteo_champs/conteo_champs_adc.csv')
conteo_supp = pd.read_csv('data/visualizacion/conteo_champs/conteo_champs_supp.csv')

top_champ_winrate = ('data/visualizacion/winrate_champ/top_winrate_champ.csv')
jun_champ_winrate = ('data/visualizacion/winrate_champ/jun_winrate_champ.csv')
mid_champ_winrate = ('data/visualizacion/winrate_champ/mid_winrate_champ.csv')
adc_champ_winrate = ('data/visualizacion/winrate_champ/adc_winrate_champ.csv')
supp_champ_winrate = ('data/visualizacion/winrate_champ/supp_winrate_champ.csv')



# Banner
st.image("img/banner.png", use_column_width=True)

# Filtros

filtro_grafico_score = st.sidebar.selectbox('Gráfico de jugadores por score', ['Selecciona un rol','Top', 'Jungle', 'Mid', 'AD Carry', 'Support'])

filtro_grafico_champ = st.sidebar.selectbox('Gráfico de campeones', ['Selecciona un rol','Top', 'Jungle', 'Mid', 'AD Carry', 'Support'])

filtro_grafico_champ_winrate = st.sidebar.selectbox('Gráfico winrate campeones', ['Selecciona un rol','Top', 'Jungle', 'Mid', 'AD Carry', 'Support'])


# Gráficos player score

top_score = alt.Chart(top).mark_bar(color = 'red').encode(
    x='nombre_invocador',
    y='score').interactive()

jun_score = alt.Chart(jun).mark_bar(color = 'red').encode(
    x='nombre_invocador',
    y='score').interactive()

mid_score = alt.Chart(mid).mark_bar(color = 'red').encode(
    x='nombre_invocador',
    y='score').interactive()

adc_score = alt.Chart(adc).mark_bar(color = 'red').encode(
    x='nombre_invocador',
    y='score').interactive()

supp_score = alt.Chart(supp).mark_bar(color = 'red').encode(
    x='nombre_invocador',
    y='score').interactive()

# Gráficos champs más jugados

champs_top = alt.Chart(conteo_top).mark_bar(color = 'red').encode(
    x='Champion',
    y='Participaciones').interactive()

champs_jun = alt.Chart(conteo_jun).mark_bar(color = 'red').encode(
    x='Champion',
    y='Participaciones').interactive()

champs_mid = alt.Chart(conteo_mid).mark_bar(color = 'red').encode(
    x='Champion',
    y='Participaciones').interactive()

champs_adc = alt.Chart(conteo_adc).mark_bar(color = 'red').encode(
    x='Champion',
    y='Participaciones').interactive()

champs_supp = alt.Chart(conteo_supp).mark_bar(color = 'red').encode(
    x='Champion',
    y='Participaciones').interactive()


# Gráficos champs winrate

top_champ_winrate_g = alt.Chart(top_champ_winrate).mark_bar(color = 'red').encode(
    x='Champion',
    y='Winrate').interactive()

jun_champ_winrate_g = alt.Chart(jun_champ_winrate).mark_bar(color = 'red').encode(
    x='Champion',
    y='Winrate').interactive()

mid_champ_winrate_g = alt.Chart(mid_champ_winrate).mark_bar(color = 'red').encode(
    x='Champion',
    y='Winrate').interactive()

adc_champ_winrate_g = alt.Chart(adc_champ_winrate).mark_bar(color = 'red').encode(
    x='Champion',
    y='Winrate').interactive()

supp_champ_winrate_g = alt.Chart(supp_champ_winrate).mark_bar(color = 'red').encode(
    x='Champion',
    y='Winrate').interactive()


# Despliegue de gráficos mejores jugadores

if filtro_grafico_score == 'Top':    
    st.caption('# Mejores jugadores en Top')
    st.altair_chart(top_score)
    
elif filtro_grafico_score == 'Jungle':
    st.caption('# Mejores jugadores en Jungla')
    st.altair_chart(jun_score)

elif filtro_grafico_score == 'Mid':
    st.caption('# Mejores jugadores en Mid')
    st.altair_chart(mid_score)

elif filtro_grafico_score == 'AD Carry':
    st.caption('# Mejores jugadores en ADC')
    st.altair_chart(adc_score)

elif filtro_grafico_score == 'Support':
    st.caption('# Mejores jugadores en Support')
    st.altair_chart(supp_score)
        

# Despliegue de gráficos campeones más jugados por rol
        
if filtro_grafico_champ == 'Top':
    st.caption(f'# Campeones más usados en {filtro_grafico_champ}')
    st.altair_chart(champs_top)      

elif filtro_grafico_champ == 'Jungle':
    st.caption(f'# Campeones más usados en {filtro_grafico_champ}')
    st.altair_chart(champs_jun)
    
elif filtro_grafico_champ == 'Mid':
    st.caption(f'# Campeones más usados en {filtro_grafico_champ}')
    st.altair_chart(champs_mid)

elif filtro_grafico_champ == 'AD Carry':
    st.caption(f'# Campeones más usados en {filtro_grafico_champ}')
    st.altair_chart(champs_adc)

elif filtro_grafico_champ == 'Support':
    st.caption(f'# Campeones más usados en {filtro_grafico_champ}')
    st.altair_chart(champs_supp)


# Despliegue de gráficos winrate campeones    

if filtro_grafico_champ_winrate == 'Top':
    st.caption(f'# Winrate campeones en {filtro_grafico_champ}')
    st.altair_chart(top_champ_winrate_g)      

elif filtro_grafico_champ_winrate == 'Jungle':
    st.caption(f'# Winrate campeones en {filtro_grafico_champ}')
    st.altair_chart(jun_champ_winrate_g)
    
elif filtro_grafico_champ_winrate == 'Mid':
    st.caption(f'# Winrate campeones en {filtro_grafico_champ}')
    st.altair_chart(mid_champ_winrate_g)

elif filtro_grafico_champ_winrate == 'AD Carry':
    st.caption(f'# Winrate campeones en {filtro_grafico_champ}')
    st.altair_chart(adc_champ_winrate_g)

elif filtro_grafico_champ_winrate == 'Support':
    st.caption(f'# Winrate campeones en {filtro_grafico_champ}')
    st.altair_chart(supp_champ_winrate_g)
    