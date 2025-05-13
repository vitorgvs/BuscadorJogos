from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


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


def buscar_jogo_epic(nome_jogo):
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
        
        chromium_path = r"C:\Users\Irine\Downloads\chrome-win\chrome-win\chrome.exe"

        chrome_options = Options()
        chrome_options.add_argument("--headless=new")  # Modo headless mais confiável
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--enable-webgl")
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
        
        chrome_options.binary_location = chromium_path

        driver = webdriver.Chrome(options=chrome_options)

        termo_busca = nome_jogo.replace(" ", "%20")
        url = f"https://store.epicgames.com/pt-BR/browse?q={termo_busca}&sortBy=relevancy&sortDir=DESC&count=40"
        driver.get(url)

        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "css-g3jcms"))
            )
        except:
            driver.quit()
            logger.error(f"Houve um erro ao localizar o jogo: {nome_jogo} na Epic Games Store: {str(e)}")
            return None

        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()

        primeiro_card = soup.find("a", class_="css-g3jcms")
        if not primeiro_card:
            logger.info(f"No results found for {nome_jogo} on Epic Games Store")
            return None

        nome_div = primeiro_card.find("div", class_="css-rgqwpc")
        nome = nome_div.text.strip() if nome_div else "Nome não encontrado"

        preco_span = primeiro_card.find("span", class_="css-12s1vua")
        preco = preco_span.text.strip().replace(u'\xa0', ' ') if preco_span else "Preço não encontrado"

        link = "https://store.epicgames.com" + primeiro_card["href"]

        logger.info(f"Jogo {nome_jogo} encontrado na Epic Games Store com o preço {preco}")
        return {
            "Loja": "Epic Games Store",
            "Jogo": nome,
            "Preço": preco,
            "Link": link
        }
    except Exception as e:
        logger.error(f"Houve um erro ao localizar o jogo: {nome_jogo} na Epic Games Store: {str(e)}")
        return None
    