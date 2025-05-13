import streamlit as st
import pandas as pd
from epic_utils import buscar_jogo_epic
from steam_utils import buscar_jogo_steam
from xbox_utils import buscar_jogo_xbox



if __name__ == "__main__":

    st.title("Buscador de Preço de jogos 🎮")

    nome_jogo = st.text_input("Digite o nome do jogo")

    if st.button("Buscar"):
        with st.spinner("Buscando nas Lojas ..."):
            resultado_epic = buscar_jogo_epic(nome_jogo)
            resultado_xbox = buscar_jogo_xbox(nome_jogo)
            resultado_steam = buscar_jogo_steam(nome_jogo)
            if any ([resultado_epic, resultado_xbox, resultado_steam]):
                for resultado in ([resultado_epic, resultado_xbox, resultado_steam]):
                    if resultado: 
                        df = pd.DataFrame([resultado])
                        st.dataframe(df)
                        st.markdown(f"[ Acessar na {resultado['Loja']}]({resultado['Link']})", unsafe_allow_html=True)
            
