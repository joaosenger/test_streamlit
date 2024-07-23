import streamlit as st
from login.service import login


def show_login():
    st.title('Login')

    with st.form(key='login_form'):
        username = st.text_input('Usuário')
        password = st.text_input(
            label='Senha',
            type='password'
        )

        submit_button = st.form_submit_button(label='Login')

        if submit_button:
            login(
                username=username,
                password=password
            )
