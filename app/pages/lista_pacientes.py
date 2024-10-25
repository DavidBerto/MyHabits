import streamlit as st
import pandas as pd
#import paciente 

def base_connect():
    cols = ['ID','Nome', 'Gênero', 'Status','tags']
    df_pacientes = pd.read_csv("C:\\Users\david\OneDrive\Projetos\MyHabits\data\pacientes.csv", sep=";")
   # df_pacientes = df_pacientes.loc[df_pacientes['Nome'] == nome]
    return df_pacientes[cols]

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

if query:
    #mask = base_connect().applymap(lambda x: query in str(x).lower()).any(axis=1)
    #df = base_connect()[mask]
    filtered_df = filter_dataframe(base_connect(), query)
else:
    filtered_df = base_connect()

st.data_editor(
    filtered_df,
    hide_index=True,
    num_rows="dynamic",
    use_container_width=True
    #disabled = True
    )                                

def filtro_tabela(col, df):
    options = st.multiselect(f'Buscar por {col}:',
               df[col].unique().tolist())
    return options

if right_col.button('Novo paciente'):
    st.switch_page("paciente.py")
    
if right_col.button("filtro avançado"):
    filtro_tabela()
    

#filtro

#filtered_df = base_connect()[base_connect()['Nome'].isin(options)]

#st.table(filtered_df)


#print(type(options))
#st.table(base_connect().loc[base_connect()['Nome'] == options])

#if __name__ == "__main__":
        

        
    