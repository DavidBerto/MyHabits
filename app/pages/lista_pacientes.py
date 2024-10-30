import streamlit as st
import pandas as pd
import numpy as np
#import paciente 
from PIL import Image, ImageDraw
import base64
import os

#pathPhoto = "/mount/src/myhabits/app/images/foto_david.jpg"
#pathDB = "/mount/src/myhabits/app/db/pacientes.csv"

pathPhotoURL = "C:/Users/david/OneDrive/Projetos/MyHabits/app/images/"
pathDB = "C:/Users/david/OneDrive/Projetos/MyHabits/app/db/pacientes.csv"

def base_connect():
    
    cols = ['ID','photo','APELIDO','NOME', 'GENDER', 'STATUS','TAGS','FOTO_URL']
    #df_pacientes = pd.read_csv("/mount/src/myhabits/app/db/pacientes.csv", sep=";")
    df_pacientes = pd.read_csv(pathDB, sep=";")
    listaFoto64 = []
    for i in df_pacientes["FOTO_URL"]:
        pathPhoto = pathPhotoURL+str(i)+".jpg"
        if os.path.exists(pathPhoto):
            with open(pathPhoto, "rb") as image_file:
                base64_image = base64.b64encode(image_file.read()).decode('utf-8')
            listaFoto64.append(f"data:image/jpeg;base64,{base64_image}")
        else: listaFoto64.append("")
    df_pacientes["photo"] = listaFoto64
    #df_pacientes = df_pacientes.loc[df_pacientes['Nome'] == nome]
    return df_pacientes[['photo','NOME','APELIDO', 'GENDER', 'STATUS','TAGS']]

#def novo_paciente():
    # Nome, Endereço, medidas

#def busca():

#def exportar():

#def filtros():

st.title("Lista de Pacientes")
left_col, right_col = st.columns([5,1])

query = left_col.text_input("Busca","")

def filter_dataframe(df, search_term):
    
    return df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]

def filtro_tabela(df):
    Allcol = df.columns
    col = st.selectbox("Escolha a coluna da tabela", Allcol)
    return col

if right_col.button('Novo paciente'):
    st.switch_page("pages/paciente1.py")
    
#if right_col.button("filtro avançado"):
#    filtro_tabela(base_connect())
#    st.multiselect(f'Buscar por {filtro_tabela(base_connect())}:',
#               base_connect()[filtro_tabela(base_connect())].unique().tolist())
if query:
    #mask = base_connect().applymap(lambda x: query in str(x).lower()).any(axis=1)
    #df = base_connect()[mask]
    filtered_df = filter_dataframe(base_connect(), query)
else:
    filtered_df = base_connect()

st.data_editor(
    filtered_df,
    column_config={
        "photo": st.column_config.ImageColumn(
            "FOTO", help="Streamlit app preview screenshots"
        ),
        "ID": st.column_config.Column(
            "Registro",
            width="small",
        ),
        "GENDER": st.column_config.Column(
            "GÊNERO"
        )},
    hide_index=True,
    num_rows="dynamic",
    use_container_width=True
    #disabled = True
    )                             
#filtro

#filtered_df = base_connect()[base_connect()['Nome'].isin(options)]

#st.table(filtered_df)


#print(type(options))
#st.table(base_connect().loc[base_connect()['Nome'] == options])

#if __name__ == "__main__":
        

        
    