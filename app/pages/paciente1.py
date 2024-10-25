import streamlit as st
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

#foto
col1.image(image,width = 200)

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

colPerfilEmail, colChatVideo = col3.columns(2)
if colPerfilEmail.button('Perfil'):
    colPerfilEmail.write('Perfil')
if colPerfilEmail.button('E-mail'):
    colPerfilEmail.write('E-mail')
if colChatVideo.button('Chat'):
    colChatVideo.write('Chat')
if colChatVideo.button('Videochamada'):
    colChatVideo.write('Videochamada')
    
    
#Gráfico de evolução de peso
st.subheader("Evolução")

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
        st.write("Plano adicionado com sucesso!")

with st.expander("Anamnese"):
    colInicio, colData = st.columns([3,1])
    colInicio.text_input("Caso Clínico")
    colData.date_input("Data", format="DD/MM/YYYY")
    patologias = ["Ansiedade", "Cancer", "Gasrite", "DIabetes", "Gota"]
    dfPatologia = st.multiselect("Patologias",patologias)
    dfOutrasPatologia = st.text_area("Outras Patologias")  
    dfMedicamentos = st.text_area("Medicamentos")    
    dfHisto = st.text_input("HIstórico Familiar")
    if st.button('Salvar'):
        st.write("Registros Salvos!")
    
    
    
    
    
    
    
    
# Criação de dados de exemplo
data = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos', 'Ana'],
    'Idade': [25, 30, 35, 28, 40, 99],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Curitiba','São Paulo'],
    'Profissão': ['Engenheiro', 'Médica', 'Professor', 'Advogada', 'Arquiteto', 'Ana']
}
df = pd.DataFrame(data)

# Barra de busca
search_term = st.text_input("Buscar", "")

# Criação de opções de filtro para cada coluna
filter_options = {}
for column in df.columns:
    unique_values = df[column].unique().tolist()
    filter_options[column] = st.multiselect(f"Filtrar por {column}", unique_values)

# Filtragem do DataFrame com base no termo de busca e nos filtros
filtered_df = filter_dataframe(df, search_term, filter_options)

# Exibição da tabela editável
edited_df = st.data_editor(
    filtered_df,
    num_rows="dynamic",
    use_container_width=True
)
