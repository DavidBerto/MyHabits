import streamlit as st
from streamlit_carousel import carousel

def atalhos():
    col1, col2, col3, col4 = st.columns(4)

    if col1.button("Relatórios"):
        st.switch_page("pages/relatorio.py")

    if col2.button("Descritivo de prato"):
        st.switch_page("pages/2_descritivo_prato.py")

    if col3.button("Lista de Pacientes"):
        st.switch_page("pages/lista_pacientes.py")
        
    if col4.button("Novo Paciente"):
        st.switch_page("pages/paciente1.py")
        
    if col1.button("Agenda"):
        st.switch_page("pages/agenda.py")

st.header("Transformando Hábitos em Saúde")

col7, col8 = st.columns([2,1])
with col7:
    st.subheader("Como posso te ajudar hoje?")
    atalhos()

with col8:
    st.subheader("Notícias da Semana")
    test_items = [
        dict(
            title="Aniversários",
            text="Joana / Pedrinho                                                                    ",
            img="https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1380&t=st=1688825493~exp=1688826093~hmac=cb486d2646b48acbd5a49a32b02bda8330ad7f8a0d53880ce2da471a45ad08a4"
            #link="https://discuss.streamlit.io/t/new-component-react-bootstrap-carousel/46819",
        ),
        dict(
            title="Agendamentos",
            text="10:00 Maria / 11:00 Joãozinho                                                        ",
            img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1"
            #link="https://github.com/thomasbs17/streamlit-contributions/tree/master/bootstrap_carousel",
        ),
        dict(
            title="Inadimplentes",
            text="Pedrinho / Luizinho                                                                   ",
            img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0"
            #link="https://github.com/thomasbs17/streamlit-contributions/tree/master",
        ),
        dict(
            title="Atualizações",
            text="Maria pisou na jaca                                                                    ",
            img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0"
        ),
    ]

    carousel(items=test_items)