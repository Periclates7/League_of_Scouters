import pandas as pd
import numpy as np

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
PATH=ChromeDriverManager().install()

import requests
from bs4 import BeautifulSoup






def scrapeo(url):
    
    driver=webdriver.Chrome(PATH)               
    driver.get(url)
    
    
    name_reg= driver.find_element(By.TAG_NAME, 'h2').text                        # Nombre de invocador
    nombre = name_reg.split('(')[0][:-1]
    region = name_reg.split('(')[1].rstrip(')')                                  # Región en la que juega el jugador

    liga = driver.find_element(By.CLASS_NAME, 'leagueTier').text
    liga = liga.split(' ')[0]                                                    # Liga (Challenger, GrandMaster, Master ...)

    lp = driver.find_element(By.CLASS_NAME, 'leaguePoints').text
    lp = lp[:-3]                                                                 # LPs

    cola = driver.find_element(By.CLASS_NAME, 'queue').text                      # Modalidad de juego
    rank = driver.find_element(By.CLASS_NAME, 'highlight').text                  # Rank mundial 
    rank_per = driver.find_element(By.CLASS_NAME, 'topRankPercentage').text      # Rank del jugador en porcentaje
    wins = driver.find_element(By.CLASS_NAME, 'winsNumber').text                 # Nº de victorias
    loses = driver.find_element(By.CLASS_NAME, 'lossesNumber').text              # Nº de derrotas
                            
    
    winrate_total = driver.find_element(By.ID, 'graphDD3').text                  # Winrate total del jugador
    
    if '%' in winrate_total:
        winrate_total = driver.find_element(By.ID, 'graphDD3').text[:-1]         # Nº de partidas en la Season
        n_games = driver.find_element(By.ID, 'graphDD2').text
    else:
        n_games = driver.find_element(By.ID, 'graphDD3').text
        winrate_total = driver.find_element(By.ID, 'graphDD4').text[:-1]                                                                     
    
    
    champs_name = [driver.find_elements(By.CLASS_NAME, 'name')[i].text for i in range(len(driver.find_elements(By.CLASS_NAME,       'name')))]
    
    # Nombre de los campeones más jugados por el jugador
    
    campeones = champs_name[1:9]
    
    champ_1 = campeones[0]
    champ_2 = campeones[1]
    champ_3 = campeones[2]
    champ_4 = campeones[3]
    champ_5 = campeones[4]
    champ_6 = campeones[5]
    champ_7 = campeones[6]
    champ_8 = campeones[7]
    
    regional_rank = [driver.find_elements(By.CLASS_NAME, 'regionalRank')[i].text for i in             range(len(driver.find_elements(By.CLASS_NAME, 'regionalRank')))]
    
    # Rank por regiones de los campeones más jugados por el jugador
    
    regional_rank_1 = regional_rank[0]
    regional_rank_2 = regional_rank[1]
    regional_rank_3 = regional_rank[2]
    regional_rank_4 = regional_rank[3]
    regional_rank_5 = regional_rank[4]
    regional_rank_6 = regional_rank[5]
    regional_rank_7 = regional_rank[6]
    regional_rank_8 = regional_rank[7]
    
    
    # KDA de los campeones más jugados por el jugador
    
    kda = [driver.find_elements(By.CLASS_NAME, 'kda')[i].text for i in range(len(driver.find_elements(By.CLASS_NAME, 'kda')))]
    
    contador = 0
    i = len(kda) - 1
    while contador < 8 and i >= 0:
        if kda[i] != '':
            contador += 1
        i -= 1

    if contador == 8:
        resultado = kda[i+1:]
        resultado = result[:8]
    
    
    kda = [e.split(' / ') for e in result]
    
    kills_champ_1 = kda[0][0]
    kills_champ_2 = kda[1][0]
    kills_champ_3 = kda[2][0]
    kills_champ_4 = kda[3][0]
    kills_champ_5 = kda[4][0]
    kills_champ_6 = kda[5][0]
    kills_champ_7 = kda[6][0]
    kills_champ_8 = kda[7][0]
    
    deaths_champ_1 = kda[0][1]
    deaths_champ_2 = kda[1][1]
    deaths_champ_3 = kda[2][1]
    deaths_champ_4 = kda[3][1]
    deaths_champ_5 = kda[4][1]
    deaths_champ_6 = kda[5][1]
    deaths_champ_7 = kda[6][1]
    deaths_champ_8 = kda[7][1]
    
    assists_champ_1 = kda[0][2]
    assists_champ_2 = kda[1][2]
    assists_champ_3 = kda[2][2]
    assists_champ_4 = kda[3][2]
    assists_champ_5 = kda[4][2]
    assists_champ_6 = kda[5][2]
    assists_champ_7 = kda[6][2]
    assists_champ_8 = kda[7][2]
    
    
    
    progress_bar = [driver.find_elements(By.CLASS_NAME, 'progressBarTxt')[i].text for i in range(len(driver.find_elements(By.CLASS_NAME, 'progressBarTxt')))]
    
    
    
    # Número de partidas jugadas de los campeones más jugados por el jugador
    
    games_per_champ = progress_bar[:16:2]
    
    games_champ_1 = games_per_champ[0]
    games_champ_2 = games_per_champ[1]
    games_champ_3 = games_per_champ[2]
    games_champ_4 = games_per_champ[3]
    games_champ_5 = games_per_champ[4]
    games_champ_6 = games_per_champ[5]
    games_champ_7 = games_per_champ[6]
    games_champ_8 = games_per_champ[7]
    
    
    # Winrate de los campeones más jugados por el jugador
    
    winrate_per_champ = progress_bar[1:16:2]
    
    winrate_champ_1 = winrate_per_champ[0]
    winrate_champ_2 = winrate_per_champ[1]
    winrate_champ_3 = winrate_per_champ[2]
    winrate_champ_4 = winrate_per_champ[3]
    winrate_champ_5 = winrate_per_champ[4]
    winrate_champ_6 = winrate_per_champ[5]
    winrate_champ_7 = winrate_per_champ[6]
    winrate_champ_8 = winrate_per_champ[7]
    
    winrate_champ_1 = winrate_champ_1[:-1]             # Quitamos '%' 
    winrate_champ_2 = winrate_champ_2[:-1]
    winrate_champ_3 = winrate_champ_3[:-1]
    winrate_champ_4 = winrate_champ_4[:-1]
    winrate_champ_5 = winrate_champ_5[:-1]
    winrate_champ_6 = winrate_champ_6[:-1]
    winrate_champ_7 = winrate_champ_7[:-1]
    winrate_champ_8 = winrate_champ_8[:-1]
    
    
    # Roles + jugados por el jugador
    
    rol = [driver.find_elements(By.CLASS_NAME, 'img-align-block')[i].text for i in range(len(driver.find_elements(By.CLASS_NAME, 'img-align-block')))]
    
    driver.quit()
    
    try:
        roles = [e for e in rol if e in ['AD Carry', 'Support', 'Top', 'Mid', 'Jungler']][:3]
    except:
        roles = [e for e in rol if e in ['AD Carry', 'Support', 'Top', 'Mid', 'Jungler']]
    
    
    rol_1 = roles[0]
    rol_2 = roles[1]
    rol_3 = roles[2]
    
    
    # Partidas en cada rol jugado por el jugador
    
    games_per_rol = progress_bar[-6::2]
    
    games_per_rol_1 = games_per_rol[0]
    games_per_rol_2 = games_per_rol[1]
    games_per_rol_3 = games_per_rol[2]
    
    
    # Winrate para cada rol jugado por el jugador
    
    winrate_per_rol = progress_bar[-5::2]
    
    winrate_per_rol_1 = winrate_per_rol[0]
    winrate_per_rol_2 = winrate_per_rol[1]
    winrate_per_rol_3 = winrate_per_rol[2]
    
    winrate_per_rol_1 = winrate_per_rol_1[:-1]                 # Quitamos '%' 
    winrate_per_rol_2 = winrate_per_rol_2[:-1]
    winrate_per_rol_3 = winrate_per_rol_3[:-1]
    
    
    #KDA jugador
    
    kda_player = [driver.find_elements(By.CLASS_NAME, 'number')[i].text for i in range(len(driver.find_elements(By.CLASS_NAME, 'number')))]
    
    if '/' in kda_player[-4]:
    
        kills_player_kda = kda_player[-4].split(' / ')[0]
        deaths_player_kda = kda_player[-4].split(' / ')[1]
        assists_player_kda = kda_player[-4].split(' / ')[2]
    else:
        pass
    
    
    data = {'nombre_invocador':nombre,              # Preparamos nuestros datos scrapeados en un diccionario donde la key
            'region':region,                        # será el nombre de la columna y el value una lista con nuestros datos
            'liga': liga,
            'lps':lp,
            'cola':cola,
            'ranking_mundial':rank,
            'ranking_porcentaje':rank_per,
            
            'wins':wins,
            'loses':loses,
            'n_games':n_games,
            'winrate_total':winrate_total,
            
            'kills_player_kda':kills_player_kda,
            'deaths_player_kda':deaths_player_kda,
            'assists_player_kda':assists_player_kda,
            
            'rol_1':rol_1,
            'games_per_rol_1':games_per_rol_1,
            'winrate_per_rol_1':winrate_per_rol_1,
            
            'rol_2':rol_2,
            'games_per_rol_2':games_per_rol_2,
            'winrate_per_rol_2':winrate_per_rol_2,
            
            'rol_3':rol_3,
            'games_per_rol_3':games_per_rol_3,
            'winrate_per_rol_3':winrate_per_rol_3,
            
            'champ_1':champ_1,
            'regional_rank_1':regional_rank_1,
            'kills_champ_1':kills_champ_1,
            'deaths_champ_1':deaths_champ_1,
            'assists_champ_1':winrate_total,
            'games_champ_1':games_champ_1,
            'winrate_champ_1':winrate_champ_1,
            
            'champ_2':champ_2,
            'regional_rank_2':regional_rank_2,
            'kills_champ_2':kills_champ_2,
            'deaths_champ_2':deaths_champ_2,
            'assists_champ_2':assists_champ_2,
            'games_champ_2':games_champ_2,
            'winrate_champ_2':winrate_champ_2,
            
            'champ_3':champ_3,
            'regional_rank_3':regional_rank_3,
            'kills_champ_3':kills_champ_3,
            'deaths_champ_3':deaths_champ_3,
            'assists_champ_3':assists_champ_3,
            'games_champ_3':games_champ_3,
            'winrate_champ_3':winrate_champ_3,
            
            'champ_4':champ_4,
            'regional_rank_4':regional_rank_4,
            'kills_champ_4':kills_champ_4,
            'deaths_champ_4':deaths_champ_4,
            'assists_champ_4':assists_champ_4,
            'games_champ_4':games_champ_4,
            'winrate_champ_4':winrate_champ_4,
            
            'champ_5':champ_5,
            'regional_rank_5':regional_rank_5,
            'kills_champ_5':kills_champ_5,
            'deaths_champ_5':deaths_champ_5,
            'assists_champ_5':assists_champ_5,
            'games_champ_5':games_champ_5,
            'winrate_champ_5':winrate_champ_5,
            
            'champ_6':champ_6,
            'regional_rank_6':regional_rank_6,
            'kills_champ_6':kills_champ_6,
            'deaths_champ_6':deaths_champ_6,
            'assists_champ_6':assists_champ_6,
            'games_champ_6':games_champ_6,
            'winrate_champ_6':winrate_champ_6,
            
            'champ_7':champ_7,
            'regional_rank_7':regional_rank_7,
            'kills_champ_7':kills_champ_7,
            'deaths_champ_7':deaths_champ_7,
            'assists_champ_7':assists_champ_7,
            'games_champ_7':games_champ_7,
            'winrate_champ_7':winrate_champ_7,
            
            'champ_8':champ_8,
            'regional_rank_8':regional_rank_8,
            'kills_champ_8':kills_champ_8,
            'deaths_champ_8':deaths_champ_8,
            'assists_champ_8':assists_champ_8,
            'games_champ_8':games_champ_8,
            'winrate_champ_8':winrate_champ_8,
            }
    
    return data



def roles(url):
    
    driver=webdriver.Chrome(PATH)               
    driver.get(url)
    
    rol = [driver.find_elements(By.CLASS_NAME, 'img-align-block')[i].text for i in range(len(driver.find_elements(By.CLASS_NAME, 'img-align-block')))]
    
    
    
    try:
        roles = [e for e in rol if e in ['AD Carry', 'Support', 'Top', 'Mid', 'Jungler']][:3]
    except:
        roles = [e for e in rol if e in ['AD Carry', 'Support', 'Top', 'Mid', 'Jungler']]
        
        

        
        
        
        

        
def scrapeo_player(url):
    
    driver=webdriver.Chrome(PATH)               
    driver.get(url)
    
    
    name_reg= driver.find_element(By.TAG_NAME, 'h2').text                        # Nombre de invocador
    nombre = name_reg.split('(')[0][:-1]
    region = name_reg.split('(')[1].rstrip(')')                                  # Región en la que juega el jugador

    liga = driver.find_element(By.CLASS_NAME, 'leagueTier').text
    liga = liga.split(' ')[0]                                                    # Liga (Challenger, GrandMaster, Master ...)

    lp = driver.find_element(By.CLASS_NAME, 'leaguePoints').text
    lp = lp[:-3]                                                                 # LPs

    cola = driver.find_element(By.CLASS_NAME, 'queue').text                      # Modalidad de juego
    rank = driver.find_element(By.CLASS_NAME, 'highlight').text                  # Rank mundial 
    rank_per = driver.find_element(By.CLASS_NAME, 'topRankPercentage').text      # Rank del jugador en porcentaje
    wins = driver.find_element(By.CLASS_NAME, 'winsNumber').text                 # Nº de victorias
    loses = driver.find_element(By.CLASS_NAME, 'lossesNumber').text              # Nº de derrotas
                            
    
    winrate_total = driver.find_element(By.ID, 'graphDD3').text                  # Winrate total del jugador
    
    if '%' in winrate_total:
        winrate_total = driver.find_element(By.ID, 'graphDD3').text[:-1]         # Nº de partidas en la Season
        n_games = driver.find_element(By.ID, 'graphDD2').text
    else:
        n_games = driver.find_element(By.ID, 'graphDD3').text
        winrate_total = driver.find_element(By.ID, 'graphDD4').text[:-1]
        
    data = {'nombre_invocador':nombre,              # Preparamos nuestros datos scrapeados en un diccionario donde la key
            'region':region,                        # será el nombre de la columna y el value una lista con nuestros datos
            'liga': liga,
            'lps':lp,
            'cola':cola,
            'ranking_mundial':rank,
            'ranking_porcentaje':rank_per,
            
            'wins':wins,
            'loses':loses,
            'n_games':n_games,
            'winrate_total':winrate_total}
    
    return data




def scrapeo_champs(url):
    
    driver=webdriver.Chrome(PATH)               
    driver.get(url)
    
    champs_name = [driver.find_elements(By.CLASS_NAME, 'name')[i].text for i in range(len(driver.find_elements(By.CLASS_NAME,       'name')))]
    
    # Nombre de los campeones más jugados por el jugador
    
    campeones = champs_name[1:9]
    
    champ_1 = campeones[0]
    champ_2 = campeones[1]
    champ_3 = campeones[2]
    champ_4 = campeones[3]
    champ_5 = campeones[4]
    champ_6 = campeones[5]
    champ_7 = campeones[6]
    champ_8 = campeones[7]
    
    regional_rank = [driver.find_elements(By.CLASS_NAME, 'regionalRank')[i].text for i in             range(len(driver.find_elements(By.CLASS_NAME, 'regionalRank')))]
    
    # Rank por regiones de los campeones más jugados por el jugador
    
    regional_rank_1 = regional_rank[0]
    regional_rank_2 = regional_rank[1]
    regional_rank_3 = regional_rank[2]
    regional_rank_4 = regional_rank[3]
    regional_rank_5 = regional_rank[4]
    regional_rank_6 = regional_rank[5]
    regional_rank_7 = regional_rank[6]
    regional_rank_8 = regional_rank[7]
    
    
    # KDA de los campeones más jugados por el jugador
    
    kda = [driver.find_elements(By.CLASS_NAME, 'kda')[i].text for i in range(len(driver.find_elements(By.CLASS_NAME, 'kda')))]
    
    count = 0
    i = len(kda) - 1
    while count < 8 and i >= 0:
        if kda[i] != '':
            count += 1
        i -= 1

    if count == 8:
        result = kda[i+1:]
        result = result[:8]
    
    
    kda = [e.split(' / ') for e in result]
    
    kills_champ_1 = kda[0][0]
    kills_champ_2 = kda[1][0]
    kills_champ_3 = kda[2][0]
    kills_champ_4 = kda[3][0]
    kills_champ_5 = kda[4][0]
    kills_champ_6 = kda[5][0]
    kills_champ_7 = kda[6][0]
    kills_champ_8 = kda[7][0]
    
    deaths_champ_1 = kda[0][1]
    deaths_champ_2 = kda[1][1]
    deaths_champ_3 = kda[2][1]
    deaths_champ_4 = kda[3][1]
    deaths_champ_5 = kda[4][1]
    deaths_champ_6 = kda[5][1]
    deaths_champ_7 = kda[6][1]
    deaths_champ_8 = kda[7][1]
    
    assists_champ_1 = kda[0][2]
    assists_champ_2 = kda[1][2]
    assists_champ_3 = kda[2][2]
    assists_champ_4 = kda[3][2]
    assists_champ_5 = kda[4][2]
    assists_champ_6 = kda[5][2]
    assists_champ_7 = kda[6][2]
    assists_champ_8 = kda[7][2]
    
    
    
    progress_bar = [driver.find_elements(By.CLASS_NAME, 'progressBarTxt')[i].text for i in range(len(driver.find_elements(By.CLASS_NAME, 'progressBarTxt')))]
    
    driver.quit()
    
    # Número de partidas jugadas de los campeones más jugados por el jugador
    
    games_per_champ = progress_bar[:16:2]
    
    games_champ_1 = games_per_champ[0]
    games_champ_2 = games_per_champ[1]
    games_champ_3 = games_per_champ[2]
    games_champ_4 = games_per_champ[3]
    games_champ_5 = games_per_champ[4]
    games_champ_6 = games_per_champ[5]
    games_champ_7 = games_per_champ[6]
    games_champ_8 = games_per_champ[7]
    
    
    # Winrate de los campeones más jugados por el jugador
    
    winrate_per_champ = progress_bar[1:16:2]
    
    winrate_champ_1 = winrate_per_champ[0]
    winrate_champ_2 = winrate_per_champ[1]
    winrate_champ_3 = winrate_per_champ[2]
    winrate_champ_4 = winrate_per_champ[3]
    winrate_champ_5 = winrate_per_champ[4]
    winrate_champ_6 = winrate_per_champ[5]
    winrate_champ_7 = winrate_per_champ[6]
    winrate_champ_8 = winrate_per_champ[7]
    
    winrate_champ_1 = winrate_champ_1[:-1]             # Quitamos '%' 
    winrate_champ_2 = winrate_champ_2[:-1]
    winrate_champ_3 = winrate_champ_3[:-1]
    winrate_champ_4 = winrate_champ_4[:-1]
    winrate_champ_5 = winrate_champ_5[:-1]
    winrate_champ_6 = winrate_champ_6[:-1]
    winrate_champ_7 = winrate_champ_7[:-1]
    winrate_champ_8 = winrate_champ_8[:-1]
    
    
    data = {
            'champ_1':champ_1,
            'regional_rank_1':regional_rank_1,
            'kills_champ_1':kills_champ_1,
            'deaths_champ_1':deaths_champ_1,
            'assists_champ_1':winrate_total,
            'games_champ_1':games_champ_1,
            'winrate_champ_1':winrate_champ_1,
            
            'champ_2':champ_2,
            'regional_rank_2':regional_rank_2,
            'kills_champ_2':kills_champ_2,
            'deaths_champ_2':deaths_champ_2,
            'assists_champ_2':assists_champ_2,
            'games_champ_2':games_champ_2,
            'winrate_champ_2':winrate_champ_2,
            
            'champ_3':champ_3,
            'regional_rank_3':regional_rank_3,
            'kills_champ_3':kills_champ_3,
            'deaths_champ_3':deaths_champ_3,
            'assists_champ_3':assists_champ_3,
            'games_champ_3':games_champ_3,
            'winrate_champ_3':winrate_champ_3,
            
            'champ_4':champ_4,
            'regional_rank_4':regional_rank_4,
            'kills_champ_4':kills_champ_4,
            'deaths_champ_4':deaths_champ_4,
            'assists_champ_4':assists_champ_4,
            'games_champ_4':games_champ_4,
            'winrate_champ_4':winrate_champ_4,
            
            'champ_5':champ_5,
            'regional_rank_5':regional_rank_5,
            'kills_champ_5':kills_champ_5,
            'deaths_champ_5':deaths_champ_5,
            'assists_champ_5':assists_champ_5,
            'games_champ_5':games_champ_5,
            'winrate_champ_5':winrate_champ_5,
            
            'champ_6':champ_6,
            'regional_rank_6':regional_rank_6,
            'kills_champ_6':kills_champ_6,
            'deaths_champ_6':deaths_champ_6,
            'assists_champ_6':assists_champ_6,
            'games_champ_6':games_champ_6,
            'winrate_champ_6':winrate_champ_6,
            
            'champ_7':champ_7,
            'regional_rank_7':regional_rank_7,
            'kills_champ_7':kills_champ_7,
            'deaths_champ_7':deaths_champ_7,
            'assists_champ_7':assists_champ_7,
            'games_champ_7':games_champ_7,
            'winrate_champ_7':winrate_champ_7,
            
            'champ_8':champ_8,
            'regional_rank_8':regional_rank_8,
            'kills_champ_8':kills_champ_8,
            'deaths_champ_8':deaths_champ_8,
            'assists_champ_8':assists_champ_8,
            'games_champ_8':games_champ_8,
            'winrate_champ_8':winrate_champ_8,
            }
    
    return data