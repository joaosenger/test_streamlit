from st_aggrid import AgGrid
import pandas as pd
import streamlit as st

actors = [
    {
        'id': 1,
        'name': 'Leonardo Di Caprio'
    },
    {
        'id': 2,
        'name': 'Chris Rock'
    },
    {
        'id': 3,
        'name': 'Stallone'
    }
]

def show_actors():
    st.write("Lista de Atores/Atrizes:")
    
    AgGrid(
        data = pd.DataFrame(actors),
        reload_data=True,
        columns_auto_size_mode=True,
        key='genres_grid',
        enable_enterprise_modules=False
    )
    
    st.title("Cadastrar novo ator ou atriz")
    name = st.text_input("Nome do ator ou atriz")
    if st.button('Cadastrar'):
        st.success(f"\"{name}\" cadastrado(a) com sucesso")
    