import streamlit as st
import pandas as pd
import pylab as plt
from PIL import Image
import webbrowser
import urllib.request




st.image("img/banner.png", use_column_width=True)


dataframes_por_rol = {
                      'Top': pd.read_csv('data/cuadro_mando/top_stats_score.csv'),
                      'Jungler': pd.read_csv('data/cuadro_mando/jun_stats_score.csv'),
                      'Mid': pd.read_csv('data/cuadro_mando/mid_stats_score.csv'),
                      'AD Carry': pd.read_csv('data/cuadro_mando/adc_stats_score.csv'),
                      'Support': pd.read_csv('data/cuadro_mando/supp_stats_score.csv')
                      }        


st.header('Buscador de reemplazos')

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