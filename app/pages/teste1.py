import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.grid_options_builder import GridOptionsBuilder
import numpy as np

# Configuração inicial da página
st.set_page_config(page_title="Data Editor com Botões", layout="wide")

# Função para criar dados de exemplo
def criar_dados_exemplo(n_linhas=5):
    return pd.DataFrame({
        'ID': range(1, n_linhas + 1),
        'Nome': [f'Pessoa {i}' for i in range(1, n_linhas + 1)],
        'Idade': np.random.randint(20, 60, n_linhas),
        'Cidade': [f'Cidade {i}' for i in range(1, n_linhas + 1)]
    })

# Criar ou recuperar os dados da sessão
if 'dados' not in st.session_state:
    st.session_state.dados = criar_dados_exemplo()

# Função para lidar com o clique do botão
def handle_click(id_linha):
    st.write(f"Botão clicado para a linha {id_linha}")

# Título da aplicação
st.title("Data Editor com Botões")

# Criar colunas para layout
col1, col2 = st.columns([3, 1])

with col1:
    # Editor de dados
    dados_editados = st.data_editor(
        st.session_state.dados,
        num_rows="dynamic",
        key="editor"
    )

    # Atualizar dados na sessão
    st.session_state.dados = dados_editados

# Criar botões para cada linha usando um loop
with col2:
    st.write("Ações")
    for index, row in dados_editados.iterrows():
        if st.button(f"Ação #{row['ID']}", key=f"btn_{row['ID']}"):
            handle_click(row['ID'])

# Adicionar botão para incluir nova linha
if st.button("Adicionar Nova Linha"):
    nova_linha = pd.DataFrame({
        'ID': [st.session_state.dados['ID'].max() + 1],
        'Nome': ['Novo Nome'],
        'Idade': [30],
        'Cidade': ['Nova Cidade']
    })
    st.session_state.dados = pd.concat([st.session_state.dados, nova_linha], ignore_index=True)
    st.experimental_rerun()

# Mostrar dados atuais (opcional)
st.write("Dados Atuais:")
st.write(st.session_state.dados)
def main():
    st.title('Tabela com Botões')
    
    # Chamando a função para criar a tabela com botões
    create_table_with_buttons()

if __name__ == '__main__':
    main()