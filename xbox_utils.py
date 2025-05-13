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

def buscar_jogo_xbox(nome_jogo):
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
        
        chromium_path = r"chrome-win\chrome.exe"

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

        url_busca = f"https://www.xbox.com/pt-br/Search/Results?q={nome_jogo.replace(' ', '+')}"
        driver.get(url_busca)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "commonStyles-module__basicButton___go-bX"))
        )

        soup = BeautifulSoup(driver.page_source, "html.parser")

        driver.quit()

        resultado = soup.find("a", class_="commonStyles-module__basicButton___go-bX")
        if not resultado:
            logger.info(f"Nenhum resultado para: {nome_jogo} na Xbox Store")
            return None

        preco = resultado.find("span", class_="Price-module__boldText___1i2Li")

        preco_texto = preco.text.replace('+', '').strip() if preco else "Preço não encontrado"
        link = resultado["href"]

        titulo = link.split("/store/")[1].split("/")[0].replace("-", " ").title()

        logger.info(f"Jogo {nome_jogo} Localizado na Xbox com preço {preco_texto}")
        return {
            "Loja": "Xbox Store",
            "Jogo": titulo,
            "Preço": preco_texto,
            "Link": link
        }
    except Exception as e:
        logger.error(f"Houve um erro ao localizar o jogo: {nome_jogo} na Xbox: {str(e)}")
        return None