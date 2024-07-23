import streamlit as st
from api.service import Auth


def login(username, password):
    auth_service = Auth()
    response = auth_service.get_token(
        username=username,
        password=password
    )
    if response.get('error'):
        st.error(f"Usuário ou senha incorretos, verifique e tente novamente.")
    else:
        st.session_state.access_token = response.get('access')
        st.rerun()


def logout():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()
