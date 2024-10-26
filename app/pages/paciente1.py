import streamlit as st
from streamlit_quill import st_quill
import pandas as pd
from datetime import datetime
from PIL import Image

import plotly.express as px
import plotly.graph_objects as go


# Configuração da página
#
#foto
def foto(path):
    st.buttom("Editar foto")
    return st.image(path)

def obj_prediction(col):
    df_peso = pd.DataFrame(
        {
            #'Peso': [[90, 85, 82, 85, 83],],
            'Peso': [90, 85, 82, 85, 83, 75],
            'Data': ['2022-01-01', '2022-02-02', '2022-03-03', '2022-04-04', '2022-05-05', '2022-06-06'],
            'Ideal': [90, 86, 83, 80, 79, 70]
        }
    )
    
    # Criar o gráfico de linhas
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_peso['Data'], y=df_peso['Peso'], mode='lines', name='Peso Atual'))
    fig.add_trace(go.Scatter(x=df_peso['Data'], y=df_peso['Ideal'], mode='lines', name='Peso Previsto'))
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1),
            margin=dict(l=10, r=10, t=20, b=10)
        )
# Mostrar o gráfico no Streamlit
    col.plotly_chart(fig)

def update_dataframe(df, index, new_data):
    if index is None:  # Nova linha
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    else:  # Atualizar linha existente
        df.loc[index] = new_data
    return df

def page_medidas():
    st.write("Atualize suas medidas")
    cols = ['Data', 'Peso', 'Altura', 'Abdominal','Tríceps','Subescapular','Bíceps','Axilar média',
            'Torácica ou peitoral','Supra-ilíaca','Supra-espinal','Coxa','Panturrilha medial']
    col10, col11, col12 = st.columns(3)
    df_medidas = pd.DataFrame(columns=cols)
    #st.write("Data")
    df_medidas['Data'] = col10.date_input('Data')
    df_medidas['Peso'] = col10.number_input('Peso (kg)')
    df_medidas['Altura'] = col10.number_input('Altura (m)')
    df_medidas['Abdominal'] = col10.number_input("Circunferência Abdominal (cm)")
    df_medidas['Tríceps'] = col10.number_input("Tríceps (cm)")
    df_medidas['Subescapular'] = col11.number_input("Subescapular (cm)")
    df_medidas['Bíceps'] = col11.number_input("Bíceps (cm)")
    df_medidas['Axilar média'] = col11.number_input("Axilar média (cm)")
    df_medidas['Torácica ou peitoral'] = col11.number_input("Torácica ou peitoral (cm)")
    df_medidas['Supra-ilíaca'] = col12.number_input("Supra-ilíaca (cm)")
    df_medidas['Panturrilha medial'] = col12.number_input("Panturrilha medial (cm)")
    df_medidas['Supra-espinal'] = col12.number_input("Supra-espinal (cm)")
    df_medidas['Coxa'] = col12.number_input("Coxa (cm)")

    if st.button("Salvar"):
        st.write("Medidas Salvas")
        st.toast("Medidas Salvas")
#def suporte():       


# Função para filtrar o DataFrame com base no termo de busca e nos filtros selecionados
def filter_dataframe(df, search_term, filters):
    filtered_df = df.copy()
    
    # Aplicar filtros de coluna
    for column, values in filters.items():
        if values:
            filtered_df = filtered_df[filtered_df[column].isin(values)]
    
    # Aplicar termo de busca
    if search_term:
        filtered_df = filtered_df[filtered_df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
    
    return filtered_df

col1, col2, col3 = st.columns([0.2,0.2, 0.4])

image = Image.open("/mount/src/myhabits/app/images/foto_david.jpg")
#image = Image.open("C:/Users/david/OneDrive/Projetos/MyHabits/app/images/foto_david.jpg")
#foto
col1.image(image,width = 200)
feedback = col1.feedback('stars')

#info gerais
paciente_nome = "David Berto"
col2.subheader(paciente_nome, divider="gray")

peso = 70
altura = 1.70
idade = 30
genero = "Macho"
col2.write("Peso: "+str(peso)+"Kg")
col2.write("Altura: "+str(altura)+"m")
col2.write("Idade: "+str(idade)+" anos")
col2.write("Gênero: "+str(genero))

#resumo
col3.markdown("##### Resumo")
col3.markdown("""
            * Caloteiro 
            * Não come ovo
            * não atualiza o diário a 7 dias""")

@st.dialog("Informações Pessoais", width='large')
def perfil():
    tab1, tab2, tab3 = st.tabs(['Perfil', 'Endereço', 'Prontuário'])
    with tab1:
        apelido = st.text_input("Apelido")
        
        colperfil1, colperfil2 = st.columns(2)
        nome = colperfil1.text_input("Nome")
        sobrenome = colperfil2.text_input("Sobrenome")
        genero = colperfil1.selectbox("Gênero", ["Masculino", "Feminino", "Outro"])
        email = colperfil2.text_input("E-mail")
        telefone = colperfil1.text_input("Telefone")
        data_nasc = colperfil2.date_input("Data de Nascimento")
        cpf = colperfil1.number_input("CPF")
        tags = colperfil1.selectbox('Tags', ["Moleque piranha", "Nutri Jõao", "Bixo Grilo"])
        obs = st.text_area("Observações")
        
    with tab2:
        rua = st.text_input('Rua')
        numero = st.text_input("Número")
        complemento = st.text_input("Compl.")
        bairro = st.text_input("Bairro")
        cidade = st.text_input("Cidade")
        estado = st.text_input("Estado")
        
    with tab3:
        st.write("Prontuário")
        prontuario = st_quill("")
        
    if st.button("Salvar Informações"):
            st.session_state.perfil = 'perfil'
            st.rerun()
            
colPerfilEmail, colChatVideo = col3.columns(2)

if "perfil" not in st.session_state:
    if colPerfilEmail.button("Info. Pessoais"):
        perfil()

if colPerfilEmail.button('E-mail'):
    colPerfilEmail.write('E-mail')
if colChatVideo.button('Chat'):
    colChatVideo.write('Chat')
if colChatVideo.button('Videochamada'):
    colChatVideo.write('Videochamada')
    
    
#Gráfico de evolução de peso
colEvol, colEvolBut = st.columns([0.5,3])
colEvol.markdown("### Evolução")
if colEvolBut.button("Detalhes da Evolução"):
    st.toast("Ta indo bem!!!")
obj_prediction(st)

with st.expander("Medidas Antropométricas"):
    _, col4, col5 = st.columns([3,0.5,0.5])
    if col4.button("Detalhes das Medidas"):
        st.write("Medidas adicionados com sucesso!")
    if col5.button('Adicionar Medidas'):
        page_medidas()
        
with st.expander("Planos alimentares"):
    st.write("Planos alimentares")
    _, col6, col7 = st.columns([3,0.5,0.5])
    if col7.button("Adicionar Plano"):
        st.toast("Plano adicionado com sucesso!")

with st.expander("Anamnese"):
    colInicio, colData = st.columns([3,1])
    colInicio.text_input("Caso Clínico")
    colData.date_input("Data", format="DD/MM/YYYY")
    patologias = ["Ansiedade", "Cancer", "Gasrite", "DIabetes", "Gota"]
    dfPatologia = st.multiselect("Patologias",patologias)
    dfOutrasPatologia = st.text_area("Outras Patologias")  
    dfMedicamentos = st.text_area("Medicamentos")    
    dfHisto = st.text_input("HIstórico Familiar")
    if st.button('Salvar Dados'):
        st.write("Registros Salvos!")
        st.toast("Registros Salvos!")

with st.expander("Permissões App"):
    checkAssistente = st.checkbox("Assistente Virtual")
    checkAlertaAgua = st.checkbox("Alerta de Água")
    checkAlertaDiario = st.checkbox("Alerta Atualização Refeição")
    checkAlerta = st.checkbox("Alerta ")
    
    _, col8, col9 = st.columns([3,0.5,0.5])
    
    if col9.button("Salvar Modificações"):
        st.toast("Salvo com Sucesso!")
 