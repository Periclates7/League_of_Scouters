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
colec = final_proj.profesional_player                                              # Nueva coleccion

# Tanto este archivo como el resto de archivos .py, se basan en el archivo 'funciones.py'. El proceso que siguen es el mismo con la única excepción de que cada vez que se ejecutan las diferentes funciones, los datos serán cargados en una base de datos de MongoDB. Con la inclusión de la carga en base de datos no perderemos la información ya recogida en caso de que el código o la página web donde se está scrapeando dejen de funcionar.


def scrapeo_player_prof(url):
    try:
        driver=webdriver.Chrome(PATH)               
        driver.get(url)

        #equipo_rol= [driver.find_elements(By.CLASS_NAME, 'txt')[i].text for i in range(len(driver.find_elements(By.CLASS_NAME, 'txt')))]
        #equipo_rol = equipo_rol.split(' - ')
        #equipo = equipo_rol[0]
        name_reg= driver.find_element(By.TAG_NAME, 'h2').text                        # Nombre de invocador
        nombre = name_reg.split('(')[0][:-1]
        try:
            region = name_reg.split('(')[1].rstrip(')')                              # Región en la que juega el jugador
        except:
            pass

        liga = driver.find_element(By.CLASS_NAME, 'leagueTier').text
        liga = liga.split(' ')[0]                                                 # Liga (Challenger, GrandMaster, Master ...)

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

        driver.quit()

        data = {'nombre_invocador':nombre,              # Preparamos nuestros datos scrapeados en un diccionario donde la key
                'equipo':equipo,
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
    
        colec.insert_one(data)
    
    except:
        return None