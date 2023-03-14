import pandas as pd
import numpy as np

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
PATH=ChromeDriverManager().install()

import requests
from bs4 import BeautifulSoup


def scrapeo_links():
    pags = [f'https://www.leagueofgraphs.com/es/rankings/summoners/page-{i}' for i in range(1, 11)]  # Navegamos por el                                                                                                                índice   
    links_total = []
    for url in pags:
        
        driver=webdriver.Chrome(PATH)               
        driver.get(url)
        
        links_invo = [driver.find_elements(By.TAG_NAME, 'a')[i].get_attribute('href') for i in range(len(driver.find_elements(By.TAG_NAME, 'a')))]
        
        driver.quit()
        
        links = links_invo[302:-23]                                                                # Filtramos y me quedo con                                                                                                       los url que me interesan
        links_total.append(links)
        return links_total