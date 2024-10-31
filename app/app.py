import streamlit as st

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Data Professor</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">YouTube</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Twitter</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

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
