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
    title = "Início",
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
    title="Relatórios (Em Breve)",
    icon= ":material/monitoring:"
)

financeiro_page = st.Page(
    page="pages/financeiro.py",
    title="Financeiro (Em Breve)",
    icon= ":material/attach_money:"
)

social_media_page = st.Page(
    page="pages/social_media.py",
    title="Mídias Sociais (Em Breve)",
    icon= ":material/thumb_up:"
)

agenda_page = st.Page(
    page="pages/agenda.py",
    title="Agenda (Em Breve)",
    icon= ":material/calendar_month:"
)

conteudo_page = st.Page(
    page="pages/conteudo.py",
    title="Artigos e Vídeos (Em Breve)",
    icon= ":material/local_library:"
)

time_page = st.Page(
    page="pages/equipe.py",
    title="Equipe (Em Breve)",
    icon= ":material/groups:"
)
#LOGO
#st.logo('images/favicon-32x32.png')

#navegação
hide_st_style = """
                <style>
                #MainMenu {visibility : hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                [data-testid="stToolbar"] {visibility: hidden;}
                [data-testid="appCreatorAvatar"] {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


pg = st.navigation(
    {
        "Início": [home_page], 
        "Minha Gestão": [agenda_page, financeiro_page, relatorios_page,time_page,social_media_page], # Equipe; 
        "Meus Pacientes": [planos_alimentares_page, descritivo_page, lista_pacientes_page, paciente_page], 
        "Meus Conteúdos": [conteudo_page] #video aulas; chat
    }, expanded= False
)
#pg = st.navigation([home_page, descritivo_page])
st.markdown(hide_st_style, unsafe_allow_html=True)
pg.run()

#menu superior

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #49708a;">
  <a class="navbar-brand" href="https://myhabits.com.br/" target="_blank" img = "https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1380&t=st=1688825493~exp=1688826093~hmac=cb486d2646b48acbd5a49a32b02bda8330ad7f8a0d53880ce2da471a45ad08a4">My Habits</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#"> Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://myhabits.com.br/" target="_blank"> </a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://myhabits.com.br/" target="_blank">Suporte</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)
button_style = """
    .stButton > button {
        border-radius: 5%;
        width: 100px;
        height: 75px;
        background-color: #d0e0eb;
        color: gray;
        font-size: 20px;
        box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }

"""
st.markdown(f"<style>{button_style}</style>", unsafe_allow_html=True)
