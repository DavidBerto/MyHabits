import streamlit as st
import openai
from PIL import Image
import cv2
import pandas as pd
import numpy as np
import base64

import tempfile
import os
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objects as go

import requests
import pytesseract

# image_path = "C:/Users/david/OneDrive/Área de Trabalho/bife-de-frango-coberto-com-gergelim-branco-ervilhas-tomates-brocolis-e-abobora-em-um-prato-branco-1.jpg" # Substitua pelo caminho da sua imagem
# Configura a chave da sua API OpenAI
api_key = "sk-proj-0KKgL3eDos9U4Zo2HKH6T3BlbkFJS1i1I7VTfZF4hc9zPshs"

def describe_image(image_path):
    """Descreve uma imagem usando a API da OpenAI.

    Args:
        image_path: Caminho para a imagem.

    Returns:
        Uma lista de descrições da imagem.
    """
    # Function to encode the image
    
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')

    # Path to your image
    #image_path = "C:/Users/david/OneDrive/Área de Trabalho/bife-de-frango-coberto-com-gergelim-branco-ervilhas-tomates-brocolis-e-abobora-em-um-prato-branco-1.jpg" # Substitua pelo caminho da sua imagem

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Gere uma tabela nutricional com cada alimento dentro do prato"
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    table = (response.json()['choices'][0]['message']['content'])
    
    st.markdown(table)
    
    if st.button("Registrar"):
        None
    if st.button("Cancelar"):
        describe_image(image_path)
    #return response.json()['choices'][0]['message']['content']

def page_home():
    st.title("Bem vindo ao Descritor de Alimentos")
    st.write("Este aplicativo te ajuda a acompanhar sua evolução")
    st.write("Acesse a função desejada pelo menu à esquerda")
    
def load_foto():
    img_file_buffer = st.camera_input("Take a picture")
    if img_file_buffer is not None:
        # To read image file buffer as bytes:
        bytes_data = img_file_buffer.getvalue()
        # Check the type of bytes_data:
        # Should output: <class 'bytes'>
        #st.write(type(bytes_data))
        return bytes_data
    
def page_descritivo_prato():
    
    st.title("Descritivo do Prato")
    st.write("Importe a imagem do prato ou tire uma foto")
            # Carrega a imagem
    #if st.button("Carregar imagem"):
    uploaded_file = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])
    #verifica e converte para jpeg

# Carregar a imagem
    if uploaded_file:
        temp_dir = tempfile.mkdtemp()
        path = os.path.join(temp_dir, uploaded_file.name)

        with open(path, "wb") as f:
            f.write(uploaded_file.getvalue())
        image = Image.open(uploaded_file)
    #image_array = cv2.imread(path)
        st.image(image, caption='Imagem carregada', use_column_width=True)

    # Botão para gerar a descrição
        if st.button("Gerar Descrição"):
            descriptions = describe_image(path)
            # Cria um DataFrame com as descrições
            #df = pd.DataFrame({'Alimentos': descriptions})
                # Botão para gerar a descrição      
            
def page_medidas():
    st.title("Medidas")
    st.write("Atualize suas medidas")
    cols = ['Data', 'Peso', 'Altura', 'Abdominal','Tríceps','Subescapular','Bíceps','Axilar média',
            'Torácica ou peitoral','Supra-ilíaca','Supra-espinal','Coxa','Panturrilha medial']

    df_medidas = pd.DataFrame(columns=cols)
    #st.write("Data")
    df_medidas['Data'] = st.date_input('Data')
    df_medidas['Peso'] = st.number_input('Peso (kg)')
    df_medidas['Altura'] = st.number_input('Altura (m)')
    df_medidas['Abdominal'] = st.number_input("Circunferência Abdominal (cm)")
    df_medidas['Tríceps'] = st.number_input("Tríceps (cm)")
    df_medidas['Subescapular'] = st.number_input("Subescapular (cm)")
    df_medidas['Bíceps'] = st.number_input("Bíceps (cm)")
    df_medidas['Axilar média'] = st.number_input("Axilar média (cm)")
    df_medidas['Torácica ou peitoral'] = st.number_input("Torácica ou peitoral (cm)")
    df_medidas['Supra-ilíaca'] = st.number_input("Supra-ilíaca (cm)")
    df_medidas['Panturrilha medial'] = st.number_input("Panturrilha medial (cm)")
    df_medidas['Supra-espinal'] = st.number_input("Supra-espinal (cm)")
    df_medidas['Coxa'] = st.number_input("Coxa (cm)")
    
    if st.button("Salvar"):
        st.write("Medidas Salvas")
        
def page_evolucao():
    st.title("Evolução")
    st.write("Acompanhe sua Evolução")
    
    df_peso = pd.DataFrame(
        {
            #'Peso': [[90, 85, 82, 85, 83],],
            'Peso': [90, 85, 82, 85, 83, 78, '', '','',''],
            'Data': ['2024-01', '2024-02', '2024-03', '2024-04', '2024-05', '2024-06', '2024-07', '2024-08', '2024-09', '2024-10'],
            'Ideal': [90, 86, 83, 80, 79, 77, 74, 72, 70, 69]
        }
    )
    
    # Criar o gráfico de linhas
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_peso['Data'], y=df_peso['Peso'], mode='lines', name='Peso Atual'))
    fig.add_trace(go.Scatter(x=df_peso['Data'], y=df_peso['Ideal'], mode='lines', name='Peso Previsto'))

# Mostrar o gráfico no Streamlit
    st.plotly_chart(fig)

def page_food_table():
    st.title("Análise Tabela Nutricional")
    # Initialize the camera
    if st.button("Scannear tabela"):
            
        cap = cv2.VideoCapture(0)

        while True:
            # Capture a frame from the camera
            ret, frame = cap.read()
            
            # Display the frame
            st.image(frame, caption='Camera')
            
            # Check for the 'c' key press to capture the table
            if st.button('Capture'):
                break

        # Release the camera and close the window
        cap.release()
        cv2.destroyAllWindows()

        # Pre-process the captured frame to enhance OCR accuracy
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        # Perform OCR using Tesseract
        text = pytesseract.image_to_string(thresh, lang='por', config='--psm 6')

        # Extract the table from the OCR output
        tables = []
        for line in text.split('\n'):
            if '|' in line:
                tables.append([cell.strip() for cell in line.split('|')])

        # Create a Pandas DataFrame from the extracted table
        df = pd.DataFrame(tables[1:], columns=tables[0])

        # Print the resulting DataFrame
        print(df)
            
        # Check if the limits are exceeded
        limits = {'column1': 100, 'column2': 50}  # example limits
        for column, limit in limits.items():
            if df[column].max() > limit:
                st.error("PROIBIDO")
                st.write("Limite excedido!")
                break
        else:
            st.write(df)
          
def main():

    with st.sidebar:
        selected = option_menu(
            menu_title="",
            options=["Home", "Descritivo Prato", "Evolução Física", "Medidas",
                     'Tabela Nutricional', "Chat com Especilista"],
            icons=["house","camera","graph-down","clipboard-pulse","clock-history"],
            menu_icon="heart-eyes-fill",
            default_index = 0
        )
    if selected == "Home":
        page_home()
    if selected == "Descritivo Prato":
        page_descritivo_prato()
    if selected == "Evolução Física":
        page_evolucao()
    if selected == "Medidas":
        page_medidas()
    if selected == 'Tabela Nutricional':
        page_food_table()
    if selected == "Chat com Especilista":
        st.title("Fale com o Especialista")
    
if __name__ == "__main__":
    main()

