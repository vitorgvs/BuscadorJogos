from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import streamlit as st

import requests
from bs4 import BeautifulSoup
import pandas as pd
from playwright.sync_api import sync_playwright
import selenium 

import logging




def buscar_jogo_steam(nome_jogo):
    


    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("window-size=1920x1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)


        file_handler = logging.FileHandler('buscador_de_preco.log')
        stream_handler = logging.StreamHandler()


        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)


        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
        termo = nome_jogo.replace(" ", "+")
        url_busca = f"https://store.steampowered.com/search/?term={termo}"
        driver.get(url_busca)
        time.sleep(3) 

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        resultado = soup.find("a", class_="search_result_row")

        if not resultado:
            return None

        titulo = resultado.find("span", class_="title").text.strip()
        link_jogo = resultado["href"].split("?")[0]


       
        preco_div = resultado.find("div", class_="discount_final_price")
        if not preco_div:
            preco_div = resultado.find("div", class_="discount_original_price")
        if not preco_div:
            resultado.find("div", class_="game_purchase_price")
   
        preco = preco_div.text.strip() if preco_div else "Preço não encontrado"

        return {
            "Loja": "Steam",
            "Jogo": titulo,
            "Preço": preco,
            "Link": link_jogo
        }
    except Exception as e:
        print(f"Erro ao buscar na Steam: {e}")
        return None
    finally:
        driver.quit()