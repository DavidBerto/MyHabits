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

#image = Image.open("/mount/src/myhabits/app/images/foto_david.jpg")


image = Image.open("C:/Users/david/OneDrive/Projetos/MyHabits/app/images/foto_david.jpg")
pathDBPerfil = "C:/Users/david/OneDrive/Projetos/MyHabits/app/db/pacientes.csv"
pathDBMedidas = "C:/Users/david/OneDrive/Projetos/MyHabits/app/db/medidas.csv"

pacienteID1 = 1
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
    day,month,year = map(int, birthdate.split("-"))
    today = datetime.date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    return age

col1, col2, col3 = st.columns([0.2,0.2, 0.4])

#foto
col1.image(foto_circular(image),width = 200)
feedback = col1.feedback('stars')

#idade = calc_idade(pathDBPerfil["DATA_NASC"])
#data fram do paciente
dbPerfilPac = db_perfil(pacienteID1, pathDBPerfil)
dbMedidasPac = db_perfil(pacienteID1, pathDBMedidas) #pathDBMedidas = pathDBMedidas
#st.header(pathDBPerfil["DATA_NASC"])
st.table(dbPerfilPac)
st.write(str(dbPerfilPac["DATA_NASC"][0]))