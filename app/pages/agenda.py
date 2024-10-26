# arquivo: app.py
import streamlit as st
import pandas as pd
import datetime
import json
from streamlit_calendar import calendar
import sqlite3
from datetime import datetime, timedelta


# Inicialização do banco de dados
def init_db():
    conn = sqlite3.connect('appointments.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS appointments
        (id TEXT PRIMARY KEY,
         title TEXT,
         start TEXT,
         end TEXT,
         description TEXT,
         patient_name TEXT,
         phone TEXT)
    ''')
    conn.commit()
    conn.close()

# Função para adicionar novo evento
def add_event(event_data):
    conn = sqlite3.connect('appointments.db')
    c = conn.cursor()
    c.execute('''
        INSERT OR REPLACE INTO appointments
        (id, title, start, end, description, patient_name, phone)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        event_data['id'],
        event_data['title'],
        event_data['start'],
        event_data['end'],
        event_data.get('description', ''),
        event_data.get('patient_name', ''),
        event_data.get('phone', '')
    ))
    conn.commit()
    conn.close()

# Função para carregar eventos
def load_events():
    conn = sqlite3.connect('appointments.db')
    df = pd.read_sql_query("SELECT * FROM appointments", conn)
    conn.close()
    events = df.to_dict('records')
    return events

# Função para deletar evento
def delete_event(event_id):
    conn = sqlite3.connect('appointments.db')
    c = conn.cursor()
    c.execute("DELETE FROM appointments WHERE id=?", (event_id,))
    conn.commit()
    conn.close()

# Inicialização do banco de dados
init_db()

# Título da aplicação
st.title("Agenda de Consultas")

# Seletor de visualização
view = st.radio("Escolha a visualização:", ["Diária", "Semanal"], horizontal=True)

# Configurações do calendário
calendar_options = {
    "headerToolbar": {
        "left": "prev,next today",
        "center": "title",
        "right": "timeGridDay,timeGridWeek"
    },
    "slotMinTime": "08:00:00",
    "slotMaxTime": "18:00:00",
    "initialView": "timeGridDay" if view == "Diária" else "timeGridWeek",
    "selectable": True,
    "editable": True,
    "selectMirror": True,
    "initialDate": datetime.now().strftime("%Y-%m-%d"),
    "weekends": False,
    "slotDuration": "00:30:00",
}

# Carrega eventos existentes
events = load_events()

# Criação do calendário
calendar_data = calendar(events=events, options=calendar_options)

# Tratamento de eventos do calendário
if calendar_data:
    if "eventClick" in calendar_data:
        clicked_event = calendar_data["eventClick"]["event"]
        
        # Criação do popup de edição
        with st.form(key=f"edit_event_{clicked_event['id']}"):
            st.subheader("Editar Consulta")
            
            # Campos do formulário
            title = st.text_input("Título", clicked_event['title'])
            patient_name = st.text_input("Nome do Paciente", 
                                       clicked_event.get('patient_name', ''))
            phone = st.text_input("Telefone", clicked_event.get('phone', ''))
            description = st.text_area("Descrição", 
                                     clicked_event.get('description', ''))
            
            col1, col2 = st.columns(2)
            with col1:
                start_date = st.date_input("Data Início", 
                    datetime.fromisoformat(clicked_event['start'].replace('Z', '')))
                start_time = st.time_input("Hora Início", 
                    datetime.fromisoformat(clicked_event['start'].replace('Z', '')).time())
            
            with col2:
                end_date = st.date_input("Data Fim", 
                    datetime.fromisoformat(clicked_event['end'].replace('Z', '')))
                end_time = st.time_input("Hora Fim", 
                    datetime.fromisoformat(clicked_event['end'].replace('Z', '')).time())
            
            col3, col4, col5 = st.columns(3)
            with col3:
                submit = st.form_submit_button("Salvar")
            with col4:
                delete = st.form_submit_button("Excluir")
            with col5:
                cancel = st.form_submit_button("Cancelar")
            
            if submit:
                # Atualiza o evento
                event_data = {
                    'id': clicked_event['id'],
                    'title': title,
                    'start': datetime.combine(start_date, start_time).isoformat(),
                    'end': datetime.combine(end_date, end_time).isoformat(),
                    'description': description,
                    'patient_name': patient_name,
                    'phone': phone
                }
                add_event(event_data)
                st.experimental_rerun()
            
            elif delete:
                delete_event(clicked_event['id'])
                st.experimental_rerun()
    
    elif "select" in calendar_data:
        # Criação de novo evento
        selected_start = calendar_data["select"]["start"]
        selected_end = calendar_data["select"]["end"]
        
        with st.form(key="new_event"):
            st.subheader("Nova Consulta")
            
            title = st.text_input("Título")
            patient_name = st.text_input("Nome do Paciente")
            phone = st.text_input("Telefone")
            description = st.text_area("Descrição")
            
            if st.form_submit_button("Criar"):
                event_data = {
                    'id': str(datetime.now().timestamp()),
                    'title': title,
                    'start': selected_start,
                    'end': selected_end,
                    'description': description,
                    'patient_name': patient_name,
                    'phone': phone
                }
                add_event(event_data)
                st.experimental_rerun()
    
    elif "eventDrop" in calendar_data:
        # Atualização de evento após drag and drop
        dropped_event = calendar_data["eventDrop"]["event"]
        add_event(dropped_event)
        st.experimental_rerun()

# Instruções de uso
with st.expander("Como usar"):
    st.markdown("""
    ### Instruções de uso:
    1. **Criar nova consulta**: Clique e arraste no calendário
    2. **Editar consulta**: Clique em uma consulta existente
    3. **Remarcar consulta**: Arraste e solte a consulta em um novo horário
    4. **Alternar visualização**: Use os botões acima do calendário
    5. **Navegar**: Use as setas para mudar de dia/semana
    """)

# Requisitos de instalação
requirements = """
streamlit==1.22.0
streamlit-calendar==0.4.0
pandas
sqlite3
"""

with st.expander("Requisitos de instalação"):
    st.code(requirements)
    st.markdown("""
    Para instalar os requisitos:
    1. Salve o conteúdo acima em um arquivo `requirements.txt`
    2. Execute: `pip install -r requirements.txt`
    3. Execute a aplicação: `streamlit run app.py`
    """)