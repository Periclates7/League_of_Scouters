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
    lp = int(lp[:-3])                                                            # LPs

    cola = driver.find_element(By.CLASS_NAME, 'queue').text                      # Modalidad de juego
    rank = int(driver.find_element(By.CLASS_NAME, 'highlight').text)             # Rank mundial 
    rank_per = driver.find_element(By.CLASS_NAME, 'topRankPercentage').text      # Rank del jugador en porcentaje
    wins = int(driver.find_element(By.CLASS_NAME, 'winsNumber').text)            # Nº de victorias
    loses = int(driver.find_element(By.CLASS_NAME, 'lossesNumber').text)         # Nº de derrotas
    n_games = int(driver.find_element(By.ID, 'graphDD2').text)                   # Nº de partidas en la Season
    winrate_total = driver.find_element(By.ID, 'graphDD3').text         
    winrate_total = float(winrate_total[:-1])                                    # Winrate total del jugador
    
    
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
    
    regional_rank_1 = int(regional_rank[0])
    regional_rank_2 = int(regional_rank[1])
    regional_rank_3 = int(regional_rank[2])
    regional_rank_4 = int(regional_rank[3])
    regional_rank_5 = int(regional_rank[4])
    regional_rank_6 = int(regional_rank[5])
    regional_rank_7 = int(regional_rank[6])
    regional_rank_8 = int(regional_rank[7])
    
    
    kills = [driver.find_elements(By.CLASS_NAME, 'kills')[i].text for i in range(len(driver.find_elements(By.CLASS_NAME, 'kills')))]
    
    # Asesinatos de los campeones más jugados por el jugador
    
    kills_champs = kills[29:37]
    
    kills_champ_1 = float(kills_champs[0])
    kills_champ_2 = float(kills_champs[1])
    kills_champ_3 = float(kills_champs[2])
    kills_champ_4 = float(kills_champs[3])
    kills_champ_5 = float(kills_champs[4])
    kills_champ_6 = float(kills_champs[5])
    kills_champ_7 = float(kills_champs[6])
    kills_champ_8 = float(kills_champs[7])
    
    
    
    deaths = [driver.find_elements(By.CLASS_NAME, 'deaths')[i].text for i in range(len(driver.find_elements(By.CLASS_NAME, 'deaths')))]

    # Muertes de los campeones más jugados por el jugador
    
    deaths_champs = deaths[29:37]
    
    deaths_champ_1 = float(deaths_champs[0])
    deaths_champ_2 = float(deaths_champs[1])
    deaths_champ_3 = float(deaths_champs[2])
    deaths_champ_4 = float(deaths_champs[3])
    deaths_champ_5 = float(deaths_champs[4])
    deaths_champ_6 = float(deaths_champs[5])
    deaths_champ_7 = float(deaths_champs[6])
    deaths_champ_8 = float(deaths_champs[7])
    
    
    
    assists = [driver.find_elements(By.CLASS_NAME, 'assists')[i].text for i in range(len(driver.find_elements(By.CLASS_NAME, 'assists')))]
    
    # Asistencias de los campeones más jugados por el jugador
    
    assists_champs = assists[29:37]
    
    assists_champ_1 = float(assists_champs[0])
    assists_champ_2 = float(assists_champs[1])
    assists_champ_3 = float(assists_champs[2])
    assists_champ_4 = float(assists_champs[3])
    assists_champ_5 = float(assists_champs[4])
    assists_champ_6 = float(assists_champs[5])
    assists_champ_7 = float(assists_champs[6])
    assists_champ_8 = float(assists_champs[7])
    
    
    
    progress_bar = [driver.find_elements(By.CLASS_NAME, 'progressBarTxt')[i].text for i in range(len(driver.find_elements(By.CLASS_NAME, 'progressBarTxt')))]
    
    driver.quit()
    
    # Número de partidas jugadas de los campeones más jugados por el jugador
    
    games_per_champ = progress_bar[:16:2]
    
    games_champ_1 = int(games_per_champ[0])
    games_champ_2 = int(games_per_champ[1])
    games_champ_3 = int(games_per_champ[2])
    games_champ_4 = int(games_per_champ[3])
    games_champ_5 = int(games_per_champ[4])
    games_champ_6 = int(games_per_champ[5])
    games_champ_7 = int(games_per_champ[6])
    games_champ_8 = int(games_per_champ[7])
    
    
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
    
    winrate_champ_1 = float(winrate_champ_1[:-1])              # Quitamos '%' y transformamos a float
    winrate_champ_2 = float(winrate_champ_2[:-1])
    winrate_champ_3 = float(winrate_champ_3[:-1])
    winrate_champ_4 = float(winrate_champ_4[:-1])
    winrate_champ_5 = float(winrate_champ_5[:-1])
    winrate_champ_6 = float(winrate_champ_6[:-1])
    winrate_champ_7 = float(winrate_champ_7[:-1])
    winrate_champ_8 = float(winrate_champ_8[:-1])
    
    
    # Roles + jugados por el jugador
    
    roles = champs_name[-9:-6]
    
    rol_1 = roles[0]
    rol_2 = roles[1]
    rol_3 = roles[2]
    
    
    # Partidas en cada rol jugado por el jugador
    
    games_per_rol = progress_bar[-6::2]
    
    games_per_rol_1 = int(games_per_rol[0])
    games_per_rol_2 = int(games_per_rol[1])
    games_per_rol_3 = int(games_per_rol[2])
    
    
    # Winrate para cada rol jugado por el jugador
    
    winrate_per_rol = progress_bar[-5::2]
    
    winrate_per_rol_1 = winrate_per_rol[0]
    winrate_per_rol_2 = winrate_per_rol[1]
    winrate_per_rol_3 = winrate_per_rol[2]
    
    winrate_per_rol_1 = float(winrate_per_rol_1[:-1])       # Quitamos '%' y transformamos a float
    winrate_per_rol_2 = float(winrate_per_rol_2[:-1])
    winrate_per_rol_3 = float(winrate_per_rol_3[:-1])
    
    
    #KDA jugador
    
    kills_player_kda = float(kills[-4])
    deaths_player_kda = float(deaths[-4])
    assists_player_kda = float(assists[-4])
    
    
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