import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import streamlit.components.v1 as components

def create_expandable_sidebar(width=300):
    # Criando um container para o botão
    button_container = st.container()

    # Criando a barra lateral
    with st.sidebar:
        # Adicionando espaço vertical para posicionar o conteúdo abaixo do botão
        add_vertical_space(3)
        
        # Conteúdo da barra lateral
        st.title("Barra Lateral Expansível")
        st.write("Este é o conteúdo da sua barra lateral.")

    # Criando o botão para expandir/recolher a barra lateral
    with button_container:
        if st.button("☰"):
            st.session_state.sidebar_state = not st.session_state.get('sidebar_state', False)

    # Aplicando o estado da barra lateral
    sidebar_state = 'expanded' if st.session_state.get('sidebar_state', False) else 'collapsed'

    # Injetando CSS para controlar a visibilidade e largura da barra lateral
    components.html(
        f"""
        <script>
            var sidebar = window.parent.document.querySelector('.css-1544g2n.e1fqkh3o4');
            var content = window.parent.document.querySelector('.css-1d391kg.e1fqkh3o3');
            sidebar.style.width = '{width}px';
            sidebar.style.visibility = '{sidebar_state == "expanded" ? "visible" : "hidden"}';
            sidebar.style.left = '{sidebar_state == "expanded" ? "0px" : "-{width}px"}';
            content.style.marginLeft = '{sidebar_state == "expanded" ? "{width}px" : "0px"}';
        </script>
        """,
        height=0,
    )

# Uso da função
create_expandable_sidebar(width=300)