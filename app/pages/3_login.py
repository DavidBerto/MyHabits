import streamlit as st

# Variável para controlar o estado do menu
menu_expanded = False

# Função para expandir/retratar o menu
def toggle_menu():
    global menu_expanded
    menu_expanded = not menu_expanded

# Botão para expandir/retratar o menu
st.button("☰", key="toggle_menu", on_click=toggle_menu)

# Conteúdo do menu (apenas visível quando expandido)
if menu_expanded:
    st.sidebar.title("Menu")
    st.sidebar.markdown("Opções do menu:")
    st.sidebar.button("Opção 1")
    st.sidebar.button("Opção 2")
    st.sidebar.button("Opção 3")

# Conteúdo principal da página
st.title("Página Principal")
st.write("Este é o conteúdo principal da página.")