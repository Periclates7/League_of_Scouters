import streamlit as st
import pandas as pd
import pylab as plt
from PIL import Image
import webbrowser
import urllib.request

st.image("img/cabecera_app.png", use_column_width=True)

st.title('LEAGUE OF SCOUTERS')
st.header('SCOUTING SYSTEM FOR LEAGUE OF LEGENDS')


st.subheader('Ranking de jugadores por rol')

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


filtro_grafico_player = st.sidebar.selectbox('Gráfico de jugadores', ['Selecciona un rol','Top', 'Jungle', 'Mid', 'AD Carry', 'Support'])

filtro_grafico_champ = st.sidebar.selectbox('Gráfico de campeones', ['Selecciona un rol','Top', 'Jungle', 'Mid', 'AD Carry', 'Support'])



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
        
        
# Selector de gráficos de mejores jugadores por rol

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
        
        
dataframes_por_rol = {
                      'Top': pd.read_csv('data/cuadro_mando/top_stats_score.csv'),
                      'Jungler': pd.read_csv('data/cuadro_mando/jun_stats_score.csv'),
                      'Mid': pd.read_csv('data/cuadro_mando/mid_stats_score.csv'),
                      'AD Carry': pd.read_csv('data/cuadro_mando/adc_stats_score.csv'),
                      'Support': pd.read_csv('data/cuadro_mando/supp_stats_score.csv')
                      }        


st.subheader('Sistema de sustituciones')

rol_2, invocador = st.columns(2)


selected_rol = rol_2.selectbox('Selecciona un rol', ['Top', 'Jungler', 'Mid', 'AD Carry', 'Support'])
df_seleccionado = dataframes_por_rol[selected_rol]

if selected_rol == 'Top':
    selected_column = invocador.selectbox('Selecciona un invocador', ['Kongenvenderhjem', '칸 나', 'BiIIy Butcher1', 'C9 Fudge', 'FΙGHT'])
    filtered_df = df_seleccionado[['nombre_invocador', 'region', 'liga', 'lps', 'ranking_mundial', 'winrate_total', 'kills_player_kda', 'deaths_player_kda', 'assists_player_kda', 'score', selected_column]].sort_values(by=selected_column, ascending=False)
    st.caption(f'# Los jugadores más parecidos a {selected_column} son:')
    st.dataframe(filtered_df)


elif selected_rol == 'Jungler':
    selected_column = invocador.selectbox('Selecciona un invocador', ['elyoyaaaaaaaaaaa', 'Razørk Activoo', '잘가요 굿바이', 'blaberfish2', 'I Love Uber Eats', 'Maxlore', 'Boukada', 'bluerzor'])
    filtered_df = df_seleccionado[['nombre_invocador', 'region', 'liga', 'lps', 'ranking_mundial', 'winrate_total', 'kills_player_kda', 'deaths_player_kda', 'assists_player_kda', 'score', selected_column]].sort_values(by=selected_column, ascending=False)
    st.caption(f'# Los jugadores más parecidos a {selected_column} son:')
    st.dataframe(filtered_df)


elif selected_rol == 'Mid':
    selected_column = invocador.selectbox('Selecciona un invocador', ['Hide on bush','pleroma chronou','Wesley Warren Jr','GOOD GAME GG EZ','Jænsen','dajor25','Percy Magic','M1dLaoBan','Disabled Chattt','boiat nastana'])
    filtered_df = df_seleccionado[['nombre_invocador', 'region', 'liga', 'lps', 'ranking_mundial', 'winrate_total', 'kills_player_kda', 'deaths_player_kda', 'assists_player_kda', 'score', selected_column]].sort_values(by=selected_column, ascending=False)
    st.caption(f'# Los jugadores más parecidos a {selected_column} son:')
    st.dataframe(filtered_df)
    

elif selected_rol == 'AD Carry':
    selected_column = invocador.selectbox('Selecciona un invocador', ['Jinno Kingdom','Satoru Gojo03','T1 Gumayusi','HAHAHAHHAHA','Kobbe','Beanovich'])
    filtered_df = df_seleccionado[['nombre_invocador', 'region', 'liga', 'lps', 'ranking_mundial', 'winrate_total', 'kills_player_kda', 'deaths_player_kda', 'assists_player_kda', 'score', selected_column]].sort_values(by=selected_column, ascending=False)
    st.caption(f'# Los jugadores más parecidos a {selected_column} son:')
    st.dataframe(filtered_df)


elif selected_rol == 'Support':
    selected_column = invocador.selectbox('Selecciona un invocador', ['FNC Hylissang','TL Honda CoreJJ','Vulcan 01','역천괴','school phobia','mersa777','Targamas','KC Leona','Zaunite Mylo'])
    filtered_df = df_seleccionado[['nombre_invocador', 'region', 'liga', 'lps', 'ranking_mundial', 'winrate_total', 'kills_player_kda', 'deaths_player_kda', 'assists_player_kda', 'score', selected_column]].sort_values(by=selected_column, ascending=False)
    st.caption(f'# Los jugadores más parecidos a {selected_column} son:')
    st.dataframe(filtered_df)


