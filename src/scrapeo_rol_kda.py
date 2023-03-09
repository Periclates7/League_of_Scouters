import pandas as pd
import numpy as np

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
PATH=ChromeDriverManager().install()

import requests
from bs4 import BeautifulSoup





def scrapeo_rol_kda(url):
    
    driver=webdriver.Chrome(PATH)               
    driver.get(url)
    
    progress_bar = [driver.find_elements(By.CLASS_NAME, 'progressBarTxt')[i].text for i in range(len(driver.find_elements(By.CLASS_NAME, 'progressBarTxt')))]
    
    rol = [driver.find_elements(By.CLASS_NAME, 'img-align-block')[i].text for i in range(len(driver.find_elements(By.CLASS_NAME, 'img-align-block')))]
    
    
    
    try:
        roles = [e for e in rol if e in ['AD Carry', 'Support', 'Top', 'Mid', 'Jungler']][:3]
    except:
        roles = [e for e in rol if e in ['AD Carry', 'Support', 'Top', 'Mid', 'Jungler']]
    
    if len(roles) == 3:
        rol_1 = roles[0]
        rol_2 = roles[1]
        rol_3 = roles[2]
    elif len(roles) == 2:
        rol_1 = roles[0]
        rol_2 = roles[1]
    elif len(roles) == 1:
        rol_1 = roles[0]
    
    
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
    
    driver.quit()
    
    if '/' in kda_player[-4]:
    
        kills_player_kda = kda_player[-4].split(' / ')[0]
        deaths_player_kda = kda_player[-4].split(' / ')[1]
        assists_player_kda = kda_player[-4].split(' / ')[2]
    else:
        pass
    
    
    
    if len(roles) == 3:
    
        data = {
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

                }
    elif len(roles) == 2:
        data = {
                'kills_player_kda':kills_player_kda,
                'deaths_player_kda':deaths_player_kda,
                'assists_player_kda':assists_player_kda,

                'rol_1':rol_1,
                'games_per_rol_1':games_per_rol_1,
                'winrate_per_rol_1':winrate_per_rol_1,

                'rol_2':rol_2,
                'games_per_rol_2':games_per_rol_2,
                'winrate_per_rol_2':winrate_per_rol_2

                
                }
    elif len(roles) == 1:
        data = {
                'kills_player_kda':kills_player_kda,
                'deaths_player_kda':deaths_player_kda,
                'assists_player_kda':assists_player_kda,

                'rol_1':rol_1,
                'games_per_rol_1':games_per_rol_1,
                'winrate_per_rol_1':winrate_per_rol_1
                 }
    
    return data