🎮 Projeto Busca de Preços de Jogos
Este projeto é um aplicativo desenvolvido com Streamlit que permite buscar e comparar o preço de um jogo nas seguintes lojas digitais:

Steam

Epic Games Store

Xbox Store

O projeto realiza web scraping e automação de navegador para coletar as informações de forma dinâmica.

📁 Estrutura do Projeto
bash
Copiar
Editar
📦 projeto-busca-jogos/
├── chrome-win/             # Navegador Chrome portátil (usado com Selenium)
├── main.py                 # Arquivo principal do Streamlit
├── steam_utils.py          # Função para buscar jogos na Steam
├── epic_utils.py           # Função para buscar jogos na Epic Games Store
├── xbox_utils.py           # Função para buscar jogos na Xbox Store
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo
⚙️ Requisitos
Instale as dependências com:

bash
Copiar
Editar
pip install -r requirements.txt
❗ Importante: Este projeto utiliza uma versão portátil do Chrome dentro da pasta chrome-win. Certifique-se de que o caminho para o binário está correto dentro dos scripts (chrome-win/chrome.exe).

🚀 Como Executar
bash
Copiar
Editar
streamlit run main.py
📦 Bibliotecas Utilizadas
streamlit – Interface web

requests – Requisições HTTP para páginas simples (como a Steam)

beautifulsoup4 – Extração de dados HTML

selenium – Navegação dinâmica (necessário para a Epic Games Store)

📚 Complexidade
Este projeto envolve:

Web scraping com BeautifulSoup

Manipulação de DOM dinâmico com Selenium

Organização modular das funções por loja

Interface interativa com Streamlit

É um projeto ideal para estudos de scraping e construção de interfaces rápidas em Python.