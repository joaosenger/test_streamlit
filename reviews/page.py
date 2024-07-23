from st_aggrid import AgGrid
import pandas as pd
import streamlit as st

reviews = [
    {
        'id': 1,
        'stars': 5
    },
    {
        'id': 2,
        'stars': 4
    },
    {
        'id': 3,
        'stars': 3
    }
]

def show_reviews():
    st.write("Lista de Avaliações")
    
    AgGrid(
        data = pd.DataFrame(reviews),
        reload_data=True,
        columns_auto_size_mode=True,
        key='genres_grid',
        enable_enterprise_modules=False
    )