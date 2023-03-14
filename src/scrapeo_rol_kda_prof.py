import pandas as pd
import numpy as np

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
PATH=ChromeDriverManager().install()

import requests
from bs4 import BeautifulSoup


from pymongo import MongoClient
cursor=MongoClient()
final_proj = cursor.lol_scouting                                                   # Nueva base de datos
colec = final_proj.rol_kda_profesional


# Tanto este archivo como el resto de archivos .py, se basan en el archivo 'funciones.py'. El proceso que siguen es el mismo con la única excepción de que cada vez que se ejecutan las diferentes funciones, los datos serán cargados en una base de datos de MongoDB. Con la inclusión de la carga en base de datos no perderemos la información ya recogida en caso de que el código o la página web donde se está scrapeando dejen de funcionar.


def scrapeo_rol_kda(url):
    
    try:
        driver=webdriver.Chrome(PATH)               
        driver.get(url)
        

        name_reg= driver.find_element(By.TAG_NAME, 'h2').text 
        nombre = name_reg.split('(')[0][:-1]
        tabla = driver.find_elements(By.TAG_NAME, 'tbody')[7]
        filas = tabla.find_elements(By.TAG_NAME, 'tr')
        roles = []

        for f in filas:
            elems=f.find_elements(By.TAG_NAME, 'td')

            tmp=[]

            for e in elems:
                tmp.append(e.text)

            roles.append(tmp)


        if len(roles) >= 4:
            rol_1 = roles[1][0]
            rol_2 = roles[2][0]
            rol_3 = roles[3][0]

            games_per_rol_1 = roles[1][1]
            games_per_rol_2 = roles[2][1]
            games_per_rol_3 = roles[3][1]

            winrate_per_rol_1 = roles[1][2][:-1]
            winrate_per_rol_2 = roles[2][2][:-1]
            winrate_per_rol_3 = roles[3][2][:-1]

        elif len(roles) == 3:
            rol_1 = roles[1][0]
            rol_2 = roles[2][0]

            games_per_rol_1 = roles[1][1]
            games_per_rol_2 = roles[2][1]

            winrate_per_rol_1 = roles[1][2][:-1]
            winrate_per_rol_2 = roles[2][2][:-1]

        elif len(roles) == 2:
            rol_1 = roles[1][0]

            games_per_rol_1 = roles[1][1]

            winrate_per_rol_1 = roles[1][2][:-1]
        else:
            pass




        kda_player = [driver.find_elements(By.CLASS_NAME, 'number')[i].text for i in range(len(driver.find_elements(By.CLASS_NAME, 'number')))]

        driver.quit()

        if '/' in kda_player[-4]:

            kills_player_kda = kda_player[-4].split(' / ')[0]
            deaths_player_kda = kda_player[-4].split(' / ')[1]
            assists_player_kda = kda_player[-4].split(' / ')[2]
        else:
            pass



        if len(roles) >= 4:

            data = {
                    'nombre_invocador':nombre,
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
        elif len(roles) == 3:
            data = {
                    'nombre invocador':nombre,
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
        elif len(roles) == 2:
            data = {
                    'nombre_invocador':nombre,
                    'kills_player_kda':kills_player_kda,
                    'deaths_player_kda':deaths_player_kda,
                    'assists_player_kda':assists_player_kda,

                    'rol_1':rol_1,
                    'games_per_rol_1':games_per_rol_1,
                    'winrate_per_rol_1':winrate_per_rol_1
                     }
    
    
        colec.insert_one(data)
    except:
        return None