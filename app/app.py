import streamlit as st

st.set_page_config(page_title="My Habits",
                   page_icon="/mount/src/myhabits/app/images/favicon-32x32.png",
                   #page_icon="C:/Users/david/OneDrive/Projetos/MyHabits/app/images/favicon-32x32.png",
                   layout="wide",
                   initial_sidebar_state="collapsed")

#all graphs we use custom css not streamlit 
theme_plotly = None 

#paginas
#home
home_page = st.Page(
    page = "pages/1_home.py",
    title = "Dashboard",
    icon=":material/dashboard:",
 #   icon="icons/home.jpg",
    default = True  
)
#descritivo de prato
descritivo_page = st.Page(
    page = "pages/2_descritivo_prato.py",
    title = "Descritivo Prato",
    icon = ":material/flip:"  
)
#lista de pacientes
lista_pacientes_page = st.Page(
    page = "pages/lista_pacientes.py",
    title = "Lista de Pacientes" ,
    icon= ":material/group:"
)

paciente_page = st.Page(
    page="pages/paciente1.py",
    title="Paciente",
    icon= ":material/person:"
)

planos_alimentares_page = st.Page(
    page="pages/planos_alimentares.py",
    title="Planos Alimentares",
    icon= ":material/menu_book:"
)

relatorios_page = st.Page(
    page="pages/relatorio.py",
    title="Relatórios",
    icon= ":material/monitoring:"
)

financeiro_page = st.Page(
    page="pages/financeiro.py",
    title="Financeiro",
    icon= ":material/attach_money:"
)

social_media_page = st.Page(
    page="pages/social_media.py",
    title="Mídias Sociais",
    icon= ":material/thumb_up:"
)

agenda_page = st.Page(
    page="pages/agenda.py",
    title="Agenda",
    icon= ":material/calendar_month:"
)

conteudo_page = st.Page(
    page="pages/conteudo.py",
    title="Artigos e Vídeos",
    icon= ":material/local_library:"
)
#LOGO
#st.logo('images/favicon-32x32.png')

#navegação

pg = st.navigation(
    {
        "Início": [home_page], #lista de pacientes
        "Minha Gestão": [agenda_page, financeiro_page, relatorios_page,social_media_page], # Equipe; 
        "Meus Pacientes": [descritivo_page, lista_pacientes_page, paciente_page], 
        "Minhas Consultas": [planos_alimentares_page], #  alertas
        "Meus Conteúdos": [conteudo_page] #video aulas; chat
    }
)
#pg = st.navigation([home_page, descritivo_page])
pg.run()
