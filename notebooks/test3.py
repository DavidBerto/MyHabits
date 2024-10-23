import streamlit as st
from PIL import Image
import base64
import requests
import json
import pandas as pd

# Substitua por sua URL e token da API Gemini e da API de Nutrição
GEMINI_API_URL = "https://api.gemini.com/v1/images/analyze"
GEMINI_API_TOKEN = "YOUR_GEMINI_API_TOKEN"
NUTRITION_API_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"
NUTRITION_API_KEY = "YOUR_NUTRITION_API_KEY"

def process_image(image_path):
    """Envia a imagem para a API Gemini e retorna os alimentos identificados."""

    # Codifica a imagem em base64
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    # Cria a requisição para a API Gemini
    headers = {
        "Authorization": f"Bearer {GEMINI_API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "image": encoded_string
    }
    response = requests.post(GEMINI_API_URL, headers=headers, json=data)

    # Processa a resposta da API Gemini
    try:
        response_json = response.json()
        alimentos = response_json['results']['foods']
        return alimentos
    except json.decoder.JSONDecodeError:
        st.error("Erro ao processar a resposta da API Gemini.")
        return []

def get_nutritional_info(alimento):
    """Consulta a API de nutrição e retorna as informações nutricionais."""

    # Cria a requisição para a API de Nutrição (ajuste de acordo com a API específica)
    headers = {
        "api-key": NUTRITION_API_KEY
    }
    params = {
        "query": alimento
    }
    response = requests.get(NUTRITION_API_URL, headers=headers, params=params)

    # Processa a resposta da API de Nutrição (ajuste de acordo com a API específica)
    try:
        response_json = response.json()
        # Extrai as informações nutricionais desejadas (ajuste de acordo com a estrutura da resposta)
        nutritional_info = response_json['foods'][0]['nutrients']
        return nutritional_info
    except (IndexError, KeyError, json.decoder.JSONDecodeError):
        st.error(f"Não foi possível encontrar informações nutricionais para {alimento}.")
        return {}

def main():
    st.title("Analisador Nutricional de Imagens")
    uploaded_file = st.file_uploader("Escolha uma imagem")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Imagem carregada', use_column_width=True)
        if st.button("Analisar Imagem"):
            alimentos = process_image(uploaded_file.name)
            if alimentos:
                df = pd.DataFrame()
                for alimento in alimentos:
                    nutritional_info = get_nutritional_info(alimento)
                    df = pd.concat([df, pd.DataFrame(nutritional_info, index=[alimento])], axis=1)
                st.table(df.T)
            else:
                st.error("Nenhum alimento foi identificado na imagem.")

if __name__ == "__main__":
    main()