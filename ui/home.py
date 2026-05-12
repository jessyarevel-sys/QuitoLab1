import streamlit as st

from config import APP_NAME
from ui.components import render_empty_state


def render_home_page(projects):
    """Renderiza inicio. Inputs: proyectos. Outputs: UI. Errores: ninguno."""
    st.markdown(
        f"""
        <div class="hero-card">
            <h1>{APP_NAME}: proyectos territoriales con confianza.</h1>
            <p>
            Descubre proyectos reales en Quito, entiende su evidencia y encuentra
            una forma clara de participar según tu perfil.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not projects:
        render_empty_state(
            "Todavía no hay proyectos cargados.",
            "Cuando exista al menos un proyecto, aquí aparecerá el resumen del ecosistema.",
        )
        return

    col1, col2, col3 = st.columns(3)
    col1.metric("Proyectos para demo", len(projects))
    col2.metric("Perfiles conectados", "5")
    col3.metric("Acción crítica", "Postular")

    st.subheader("Por qué importa")
    st.write(
        "En Quito existen iniciativas, talento, conocimiento académico y necesidades urbanas, "
        "pero viven fragmentados. Ciudad Lab convierte esa dispersión en oportunidades visibles, "
        "comparables y accionables."
    )

    st.subheader("Happy path de la demo")
    st.write("1. Explorar proyectos.")
    st.write("2. Revisar evidencia de confianza.")
    st.write("3. Calcular match con habilidades.")
    st.write("4. Manifestar interés.")
    st.write("5. Descargar postulaciones para seguimiento.")

    st.success("Empieza en la sección Explorar proyectos para completar el flujo principal.")
