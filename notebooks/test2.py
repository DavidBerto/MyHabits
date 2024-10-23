import streamlit as st
import openai
from PIL import Image
import cv2
import pandas as pd
import base64

import tempfile
import os
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objects as go

from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')

import pytesseract
# image_path = "C:/Users/david/OneDrive/Área de Trabalho/bife-de-frango-coberto-com-gergelim-branco-ervilhas-tomates-brocolis-e-abobora-em-um-prato-branco-1.jpg" # Substitua pelo caminho da sua imagem
# Configura a chave da sua API OpenAI
openai.api_key = "sk-Hga9cm17EL09pK2y31kxJH-pU9KQMbbb1UnSkVyURYT3BlbkFJwxDL78xLEjn_nrWmYHlCDXdBCUQyx4wUpBAGHOyCAA"#"sk-proj-0KKgL3eDos9U4Zo2HKH6T3BlbkFJS1i1I7VTfZF4hc9zPshs"
#sk-Hga9cm17EL09pK2y31kxJH-pU9KQMbbb1UnSkVyURYT3BlbkFJwxDL78xLEjn_nrWmYHlCDXdBCUQyx4wUpBAGHOyCAA

def describe_image(image_path):
    """Descreve uma imagem usando a API da OpenAI.

    Args:
        image_path: Caminho para a imagem.

    Returns:
        Uma lista de descrições da imagem.
    """

    # Abre a imagem e converte para formato base64
    #image = Image.open(image_path)
    image_array = cv2.imread(image_path)
    _, img_encoded = cv2.imencode('.jpg', image_array)
    base64_string = base64.b64encode(img_encoded).decode('utf-8')
    #with open(image_path, "rb") as image_file:
    #    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    # Cria o prompt para a API
    prompt = f"Descreva os alimentos e tabela nutricional contidos no prato da imagem: {base64_string}"

    # Chama a API para gerar a descrição

    response = openai.OpenAI().completions.create(
        model="gpt-4o-mini",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extrai as descrições da resposta
    descriptions = response.choices[0].text.split('\n')
    return descriptions

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
    uploaded_file = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])
# Carregar a imagem
    if uploaded_file:
        temp_dir = tempfile.mkdtemp()
        path = os.path.join(temp_dir, uploaded_file.name)

        with open(path, "wb") as f:
            f.write(uploaded_file.getvalue())

    image = Image.open(uploaded_file)
    st.image(image, caption='Imagem carregada', use_column_width=True)

    # Botão para gerar a descrição
    if st.button("Gerar Descrição"):
        descriptions = describe_image(path)
        # Cria um DataFrame com as descrições
        df = pd.DataFrame({'Alimentos': descriptions})
        st.table(df)
            
def page_medidas():
    st.title("Medidas")
    st.write("Atualize suas medidas")
    cols = ['Data', 'Peso', 'Altura', 'Abdominal']
    df_medidas = pd.DataFrame(columns=cols)
    
    #st.write("Data")
    df_medidas['Data'] = st.date_input('Data')
    
    #st.text_input("Peso Atual")
    df_medidas['Peso'] = st.number_input('Peso (kg)')
    
    #st.text_input("Altura")
    df_medidas['Altura'] = st.number_input('Altura (m)')
    
    #st.text_input("Circunferência Abdominal")
    df_medidas['Abdominal'] = st.number_input("Circunferência Abdominal (cm)")
    
    if st.button("Salvar"):
        st.write("Medidas Salvas")
        
def page_evolucao():
    st.title("Evolução")
    st.write("Acompanhe sua Evolução")
    
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
    st.plotly_chart(fig)

def page_food_table():
    st.title("Análise Tabela Nutricional")
    # Initialize the camera
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
            menu_title="Menu",
            options=["Home", "Descritivo Prato", "Evolução", "Medidas",'Tabela Nutricional'],
            icons=["house","camera","graph-down","clipboard-pulse","clock-history"],
            menu_icon="heart-eyes-fill",
            default_index = 0
        )
    if selected == "Home":
        page_home()
    if selected == "Descritivo Prato":
        page_descritivo_prato()
    if selected == "Evolução":
        page_evolucao()
    if selected == "Medidas":
        page_medidas()
    if selected == 'Tabela Nutricional':
        page_food_table()
        

if __name__ == "__main__":
    main()

