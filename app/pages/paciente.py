import streamlit as st
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go


# Configuração da página
#
#foto
def foto(path):
    st.buttom("Editar foto")
    return st.image(path)

def obj_prediction():
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

def update_dataframe(df, index, new_data):
    if index is None:  # Nova linha
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    else:  # Atualizar linha existente
        df.loc[index] = new_data
    return df

#planos alimentares
#with st.expander("Planos Alimentares", expanded=selected_index is not None):
#    with st.form("edit_form"):
#        st.write("Edite os dados abaixo:")
#        nome = st.text_input("Nome", value=selected_row['Nome'])
#        idade = st.number_input("Idade", value=int(selected_row['Idade']), min_value=0, max_value=120)
#        cidade = st.text_input("Cidade", value=selected_row['Cidade'])

#        submitted = st.form_submit_button("Salvar")
#        if submitted:
#            new_data = {'Nome': nome, 'Idade': idade, 'Cidade': cidade}
#            st.session_state.data = update_dataframe(st.session_state.data, selected_index, new_data)
#            st.rerun()  # Reexecutar o app para atualizar a tabela
 
#evolução física            
#with st.expander("Evolução Física", expanded=selected_index is not None):
#    with st.form("edit_form"):
#        st.write("Edite os dados abaixo:")
#        nome = st.text_input("Nome", value=selected_row['Nome'])
#        idade = st.number_input("Idade", value=int(selected_row['Idade']), min_value=0, max_value=120)
#        cidade = st.text_input("Cidade", value=selected_row['Cidade'])

#        submitted = st.form_submit_button("Salvar")
##            new_data = {'Nome': nome, 'Idade': idade, 'Cidade': cidade}
#            st.session_state.data = update_dataframe(st.session_state.data, selected_index, new_data)
#            st.rerun()  # Reexecutar o app para atualizar a tabela

 #anamnese           
#with st.expander("Anamnese", expanded=selected_index is not None):
#    with st.form("edit_form"):
#        st.write("Edite os dados abaixo:")
#        nome = st.text_input("Nome", value=selected_row['Nome'])
#        idade = st.number_input("Idade", value=int(selected_row['Idade']), min_value=0, max_value=120)
#        cidade = st.text_input("Cidade", value=selected_row['Cidade'])

#        submitted = st.form_submit_button("Salvar")
#        if submitted:
#            new_data = {'Nome': nome, 'Idade': idade, 'Cidade': cidade}
#            st.session_state.data = update_dataframe(st.session_state.data, selected_index, new_data)
#            st.rerun()  # Reexecutar o app para atualizar a tabela




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



# Título da aplicação
st.title("Tabela de Busca e Filtro com Streamlit")

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
