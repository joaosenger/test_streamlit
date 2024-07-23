from st_aggrid import AgGrid
import pandas as pd
import streamlit as st

movies = [
    {
        'id': 1,
        'name': 'Titanic'
    },
    {
        'id': 2,
        'name': 'Os Mercenários'
    },
    {
        'id': 3,
        'name': 'De volta para o futuro'
    }
]

def show_movies():
    st.write("Lista de Filmes:")

    AgGrid(
        data = pd.DataFrame(movies),
        reload_data=True,
        columns_auto_size_mode=True,
        key='genres_grid',
        enable_enterprise_modules=False
    )
