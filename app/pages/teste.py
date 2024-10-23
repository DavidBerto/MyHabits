import streamlit as st
import pandas as pd

# Função para criar ou atualizar uma linha no DataFrame
def update_dataframe(df, index, new_data):
    if index is None:  # Nova linha
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    else:  # Atualizar linha existente
        df.loc[index] = new_data
    return df

# Configuração da página
st.set_page_config(page_title="Editor de Dados Interativo", layout="wide")

# Título da aplicação
st.title("Editor de Dados Interativo com Streamlit")

# Criação de dados de exemplo se não existirem na sessão
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame({
        'Nome': ['João', 'Maria', 'Pedro'],
        'Idade': [30, 25, 35],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
    })

# Exibição da tabela editável
edited_df = st.data_editor(
    st.session_state.data,
    num_rows="dynamic",
    use_container_width=True,
    key="data_editor"
)

# Detectar mudanças na seleção da tabela
if st.session_state.data_editor['edited_rows']:
    selected_index = next(iter(st.session_state.data_editor['edited_rows']))
    selected_row = edited_df.iloc[selected_index]
else:
    selected_index = None
    selected_row = pd.Series({'Nome': '', 'Idade': 0, 'Cidade': ''})

# Expander para editar/adicionar dados
with st.expander("Editar/Adicionar Dados", expanded=selected_index is not None):
    with st.form("edit_form"):
        st.write("Edite os dados abaixo:")
        nome = st.text_input("Nome", value=selected_row['Nome'])
        idade = st.number_input("Idade", value=int(selected_row['Idade']), min_value=0, max_value=120)
        cidade = st.text_input("Cidade", value=selected_row['Cidade'])

        submitted = st.form_submit_button("Salvar")
        if submitted:
            new_data = {'Nome': nome, 'Idade': idade, 'Cidade': cidade}
            st.session_state.data = update_dataframe(st.session_state.data, selected_index, new_data)
            st.rerun()  # Reexecutar o app para atualizar a tabela

# Botão para adicionar nova linha
if st.button("Adicionar Nova Linha"):
    selected_index = None
    st.session_state.data_editor['edited_rows'] = {len(st.session_state.data): {}}
    st.rerun()

# Exibir DataFrame atualizado
st.write("DataFrame Atualizado:")
st.write(st.session_state.data)