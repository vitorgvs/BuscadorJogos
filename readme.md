# 🔍 Buscador de Jogos - Steam, Epic Games e Xbox

Este projeto é uma aplicação Python com Streamlit que busca preços de jogos nas lojas **Steam**, **Epic Games Store** e **Xbox**.

## 🎮 Funcionalidades

- Busca simultânea do nome do jogo nas três lojas.
- Exibe o preço atual e o link direto para compra.
- Interface simples via navegador usando Streamlit.

## 🧠 Estrutura

- `main.py`: Arquivo principal com a interface e orquestração.
- `steam_utils.py`: Lógica de scraping para Steam.
- `epic_utils.py`: Lógica de scraping para Epic.
- `xbox_utils.py`: Lógica de scraping para Xbox.

## 📦 Bibliotecas utilizadas

- `streamlit`
- `requests`
- `beautifulsoup4`
- `selenium`
- `webdriver-manager` (opcional, se usar navegador instalado)
- `lxml`
- `logging`

## ⚠️ Complexidade

A busca nas lojas exige técnicas de **web scraping**, e algumas páginas utilizam carregamento dinâmico via JavaScript. Em alguns casos, é necessário utilizar o Selenium com um navegador local para obter as informações corretamente.

# Como rodar

## Instale as dependências
pip install -r requirements.txt

## Rode o Streamlit
streamlit run main.py



---

## 🚫 Importante: Chrome local

Por questões de limite de tamanho do GitHub, a pasta `chrome-win/` (onde está o navegador Chromium usado pelo Selenium) **não está incluída neste repositório**.

Para utilizar corretamente o projeto:

1. Baixe o Chromium manualmente:
   - [https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html](https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html)
2. Extraia o conteúdo em uma pasta chamada `chrome-win` dentro do projeto.
3. Certifique-se de que o caminho do executável esteja referenciado corretamente no código:

```python
chromium_path = os.path.join(os.getcwd(), "chrome-win", "chrome.exe")



