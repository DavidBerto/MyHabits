import streamlit as st
from streamlit_quill import st_quill
import pandas as pd
import numpy as np
from datetime import datetime
from PIL import Image, ImageDraw

import tempfile
import os

import plotly.express as px
import plotly.graph_objects as go


#Path_foto_paciente = "/mount/src/myhabits/app/images/"
#pathDBPerfil = "/mount/src/myhabits/app/db/pacientes.csv"
#pathDBMedidas = "/mount/src/myhabits/app/db/medidas.csv"

Path_foto_paciente = "C:/Users/david/OneDrive/Projetos/MyHabits/app/images/"
pathDBPerfil = "C:/Users/david/OneDrive/Projetos/MyHabits/app/db/pacientes.csv"
pathDBMedidas = "C:/Users/david/OneDrive/Projetos/MyHabits/app/db/medidas.csv"

pacienteID1 = 3
# Configuração da página
#
#foto
def foto_circular(img):
    #st.buttom("Editar foto")
    height,width = img.size
    lum_img = Image.new('L', [height,width] , 0)
    
    draw = ImageDraw.Draw(lum_img)
    draw.pieslice([(0,0), (height,width)], 0, 360, 
                fill = 255, outline = "white")
    img_arr =np.array(img)
    lum_img_arr =np.array(lum_img)
    #Image.fromarray(lum_img_arr).show()
    final_img_arr = np.dstack((img_arr,lum_img_arr))
    return Image.fromarray(final_img_arr)

def obj_prediction(col):
    df_peso = pd.DataFrame(
        {
            #'Peso': [[90, 85, 82, 85, 83],],
            'Peso': [90.2, 85.1, 82.5, 85.9, 83.4, 77],
            'Data': ['2022-01-01', '2022-02-02', '2022-03-03', '2022-04-04', '2022-05-05', '2022-06-06'],
            'Objetivo': [90.0, 86.5, 83.8, 80.4, 79.5, 70.2]
        }
    )
    
    # Criar o gráfico de linhas
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_peso['Data'], y=df_peso['Peso'], mode='lines', name='Peso Atual'))
    fig.add_trace(go.Scatter(x=df_peso['Data'], y=df_peso['Objetivo'], mode='lines', name='Peso Objetivo'))
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
    df_medidas['Data'] = col10.date_input('Data', format="DD/MM/YYYY")
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

def db_perfil(ID, pathDB):
    df = pd.read_csv(pathDB, sep = ";")
    filtered = df.loc[df["ID"] == ID]
    return filtered
def calc_idade(birthdate):
    day,month,year = map(int, str(birthdate).split("-"))
    today = datetime.date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    return age
#data fram do paciente
dbPerfilPac = db_perfil(pacienteID1, pathDBPerfil)
dbMedidasPac = db_perfil(pacienteID1, pathDBMedidas) #pathDBMedidas = pathDBMedidas

col1, col2, col3 = st.columns([0.2,0.2, 0.4])

#foto

idref = pacienteID1-1
image = Image.open(Path_foto_paciente+str(dbPerfilPac["FOTO_URL"][idref])+".jpg")
col1.image(foto_circular(image),width = 200)
col1.write(dbPerfilPac["APELIDO"][idref])
feedback = col1.feedback('stars')

#info gerais (dados de teste)
paciente_nome = str(dbPerfilPac["NOME"][idref]) + str(" ") + str(dbPerfilPac["SOBRENOME"][idref])
col2.subheader(paciente_nome, divider="gray")

peso = dbMedidasPac['PESO'][idref]
altura = dbMedidasPac["ALTURA"][idref]
idade = 30 #calc_idade(dbPerfilPac["DATA_NASC"][0])
genero = dbPerfilPac["GENDER"][idref]
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
    with tab1: #info pessoais
        listTags = ["Moleque piranha", "Nutri João", "Bixo Grilo"]
        colperfil1, colperfil2 = st.columns(2)
        apelido = colperfil1.text_input("Apelido")
        ativo = colperfil2.checkbox("Ativo")
        nome = colperfil1.text_input("Nome")
        sobrenome = colperfil2.text_input("Sobrenome")
        genero = colperfil1.selectbox("Gênero", ["Masculino", "Feminino", "Outro"])
        email = colperfil2.text_input("E-mail")
        telefone = colperfil1.text_input("Telefone")
        data_nasc = colperfil2.date_input("Data de Nascimento", format="DD/MM/YYYY")
        cpf = colperfil1.text_input("CPF")
        tags = st.multiselect('Tags', listTags)
        
        colNovatag, colAddTag = st.columns([5,1])
        if colAddTag.button("Add Tag"):
            tag = colNovatag.text_input("Nova tag")
            listTags.append(tag)
        obs = st.text_area("Observações")    
        
    with tab2: #endereço
        colCEP, _ = st.columns([1,3])
        cep = colCEP.text_input("CEP")
        
        col1Ender, col2End, col3End = st.columns([2.5,0.5, 0.75])
        endereco = col1Ender.text_input('Endereço')
        numero = col2End.text_input("Número")
        complemento = col3End.text_input("Compl.")
        
        colBairro, colCid, colUF = st.columns([2,1.5, 0.35])
        bairro = colBairro.text_input("Bairro")
        cidade = colCid.text_input("Cidade")
        estado = colUF.text_input("UF")
        
    with tab3: #pronturário
        #st.write("Prontuário")
        prontuario = st_quill("")
        
    if st.button("Salvar Informações"):
            st.session_state.perfil = 'perfil'
            st.rerun()
            
colPerfilEmail, colChatVideo = col3.columns(2)

if "perfil" not in st.session_state:
    if colPerfilEmail.button("Info. Pessoais"):
        perfil()
        
if colPerfilEmail.button("Info. Pessoais "):
    perfil()

if colPerfilEmail.button('E-mail'):
    colPerfilEmail.write('E-mail')
if colChatVideo.button('Chat'):
    colChatVideo.write('Chat')
if colChatVideo.button('Videochamada'):
    colChatVideo.write('Videochamada')
if colChatVideo.button('Lista de Pacientes'):
    st.switch_page("pages/lista_pacientes.py")
    
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
    dfHisto = st.text_area("Histórico Familiar")
    dfExame = st.file_uploader("Carregar exame", type=["jpg", "jpeg", "pdf"])
    if dfExame:
        temp_dir = tempfile.mkdtemp()
        path = os.path.join(temp_dir, dfExame.name)

        with open(path, "wb") as f:
            f.write(dfExame)
    _, colexame = st.columns([5,0.5])
    if colexame.button('Salvar exames'):
        st.toast("Exames Salvos!")
        
    if st.button('Salvar Dados'):
        st.write("Registros Salvos!")
        st.toast("Registros Salvos!")

with st.expander("Funcionalidades App"):
    checkAssistente = st.checkbox("Assistente Virtual")
    checkAlertaAgua = st.checkbox("Alerta de Água")
    checkAlertaDiario = st.checkbox("Alerta Atualização Refeição")
    checkAlerta = st.checkbox("Modo Espião (Redes Sociais)")
    
    _, col8, col9 = st.columns([3,0.5,0.5])
    
    if col9.button("Salvar Modificações"):
        st.toast("Salvo com Sucesso!")
 