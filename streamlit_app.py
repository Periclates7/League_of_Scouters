import streamlit as st
import pandas as pd
import pylab as plt
from PIL import Image
import webbrowser
import urllib.request

st.title('FINAL PROJECT')
st.header('SCOUTING FOR LEAGUE OF LEGENDS')

df_top = pd.read_csv('data/cuadro_mando/top_mando.csv')
df_jun = pd.read_csv('data/cuadro_mando/jun_mando.csv')
df_mid = pd.read_csv('data/cuadro_mando/mid_mando.csv')
df_adc = pd.read_csv('data/cuadro_mando/adc_mando.csv')
df_supp = pd.read_csv('data/cuadro_mando/supp_mando.csv')

dataframes = ['Top', 'Jungle', 'Mid', 'AD Carry', 'Support']


    
selected_dataframe = st.selectbox("Rol", dataframes)

# mostrar dataframe seleccionado
if selected_dataframe == "Top":
    st.caption('# Best Top Players')
    st.dataframe(df_top)
elif selected_dataframe == "Jungle":
    st.caption('# Best Jungler Players')
    st.dataframe(df_jun)
elif selected_dataframe == "Mid":
    st.caption('# Best Mid Players')
    st.dataframe(df_mid)
elif selected_dataframe == "AD Carry":
    st.caption('# Best ADC Players')
    st.dataframe(df_adc)
else:
    st.caption('# Best Support Players')
    st.dataframe(df_supp)


