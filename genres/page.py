from st_aggrid import AgGrid
import pandas as pd
import streamlit as st
from genres.service import GenreService


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write("Lista de Gêneros:")
        genres_df = pd.json_normalize(genres)
        AgGrid(
            data=genres_df,
            reload_data=True,
            columns_auto_size_mode=True,
            key='genres_grid',
            enable_enterprise_modules=False
        )
    else:
        st.warning("Nenhum gênero encontrado.")

    st.title("Cadastrar novo Gênero")
    name = st.text_input("Nome do Gênero")

    if st.button('Cadastrar'):
        if not name:
            st.error("O nome do gênero não pode estar vazio.")
        else:
            new_genre = genre_service.create_genre(name=name)
            if new_genre:
                st.rerun()
            else:
                st.error("Erro ao cadastrar o gênero.")
