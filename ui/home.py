import streamlit as st
from config import APP_NAME


def render_home_page():
    """Renderiza inicio. Inputs: ninguno. Outputs: UI. Errores: ninguno."""
    st.title(f"{APP_NAME}: proyectos territoriales con confianza")
    st.write(
        "Un MVP para descubrir proyectos reales en Quito, entender su evidencia "
        "y permitir que talento, academia, ciudadanía, gobierno e inversión se vinculen."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Proyectos base", "4")
    col2.metric("Perfiles del ecosistema", "5")
    col3.metric("Acción crítica", "Postular")

    st.header("Problema")
    st.write(
        "En Quito hay talento, conocimiento, necesidades urbanas y proyectos posibles, "
        "pero viven fragmentados. Ciudad Lab organiza oportunidades con información clara."
    )

    st.header("Scope del MVP")
    st.write(
        "El MVP se limita a encontrar proyectos, revisar evidencia y manifestar interés. "
        "Todo lo que no ayude a esas tres acciones queda fuera."
    )
