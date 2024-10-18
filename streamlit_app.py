import streamlit as st
import streamlit.components.v1 as components

def render_html(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        html_content = f.read()
    components.html(html_content, height=600)

st.title("Sustentrade - Revenda de Produtos Recicláveis")

menu = ["Home", "Quem Somos Nós?", "Novidades", "Downloads do App", "Notificações", "Login", "Cadastrar-se"]
choice = st.sidebar.selectbox("Selecione uma página", menu)

if choice == "Home":
    render_html("index.html")
elif choice == "Quem Somos Nós?":
    render_html("quem_somos.html")
elif choice == "Novidades":
    render_html("novidades.html")
elif choice == "Downloads do App":
    render_html("downloads.html")
elif choice == "Notificações":
    render_html("notificacoes.html")
elif choice == "Login":
    render_html("login.html")
elif choice == "Cadastrar-se":
    render_html("cadastro.html")
