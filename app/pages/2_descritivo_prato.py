import streamlit as st
import openai
from PIL import Image

import pandas as pd
import numpy as np
import base64

import tempfile
import os

import requests
from dotenv import load_dotenv

load_dotenv()

# image_path = "C:/Users/david/OneDrive/Área de Trabalho/bife-de-frango-coberto-com-gergelim-branco-ervilhas-tomates-brocolis-e-abobora-em-um-prato-branco-1.jpg" # Substitua pelo caminho da sua imagem
# Configura a chave da sua API OpenAI
api_key = os.environ.get("OPENAI_API_KEY2")

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
    #table = (response.json())
    st.markdown(table)
    
    if st.button("Registrar"):
        None
    if st.button("Cancelar"):
        describe_image(image_path)
    #return response.json()['choices'][0]['message']['content'].


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
