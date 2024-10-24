import streamlit as st

st.set_page_config(page_title="My Habits",page_icon="images/favicon-32x32.png",layout="wide")

#all graphs we use custom css not streamlit 
theme_plotly = None 

#paginas
home_page = st.Page(
    page = "pages/1_home.py",
    title = "Dashboard",
 #   icon="icons/home.jpg",
    default = True  
)

descritivo_page = st.Page(
    page = "pages/2_descritivo_prato.py",
    title = "Descritivo Prato"  
)

pacientes_page = st.Page(
    page = "pages/lista_pacientes.py",
    title = "Pacientes"  
)

#LOGO
#st.logo('images/favicon-32x32.png')

#navegação
pg = st.navigation(
    {
        "Início": [home_page], #lista de pacientes
        "Gestão": [], #redes sociais; 
        "Pacientes": [descritivo_page, pacientes_page],
        "Conteúdo": [], # video aulas; chat
        "Planos Alimentares" : [],
        "Agenda": []
    }
)
#pg = st.navigation([home_page, descritivo_page])
pg.run()
