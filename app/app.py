import streamlit as st

st.set_page_config(page_title="My Habits",
                   page_icon="images/favicon-32x32.png",
                   layout="wide",
                   initial_sidebar_state="collapsed")

#all graphs we use custom css not streamlit 
theme_plotly = None 

#paginas
#home
home_page = st.Page(
    page = "pages/1_home.py",
    title = "Dashboard",
 #   icon="icons/home.jpg",
    default = True  
)
#descritivo de prato
descritivo_page = st.Page(
    page = "pages/2_descritivo_prato.py",
    title = "Descritivo Prato"  
)
#lista de pacientes
lista_pacientes_page = st.Page(
    page = "pages/lista_pacientes.py",
    title = "Lista de Pacientes"  
)

paciente_page = st.Page(
    page="pages/paciente1.py",
    title="Paciente"
)

#LOGO
#st.logo('images/favicon-32x32.png')

#navegação
pg = st.navigation(
    {
        "Início": [home_page], #lista de pacientes
        "Gestão": [], #redes sociais; 
        "Meus Pacientes": [descritivo_page, lista_pacientes_page,paciente_page], 
        "Planos Alimentares" : [],
        "Conteúdo": [], # video aulas; chat
        "Agenda": []
    }
)
#pg = st.navigation([home_page, descritivo_page])
pg.run()
