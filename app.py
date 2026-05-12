import streamlit as st
from config import APP_NAME, APP_ICON
from data.database import initialize_database
from logic.projects import get_projects
from ui.home import render_home_page
from ui.explore import render_explore_page
from ui.match import render_match_page
from ui.evidence import render_evidence_page
from ui.submissions import render_submissions_page


def initialize_app():
    """Inicializa app y DB. Inputs: ninguno. Outputs: None. Errores: muestra error en UI."""
    st.set_page_config(
        page_title=APP_NAME,
        page_icon=APP_ICON,
        layout="wide",
        initial_sidebar_state="expanded",
    )

    try:
        initialize_database()
    except RuntimeError as error:
        st.error(str(error))
        st.stop()


def render_navigation():
    """Renderiza navegación. Inputs: ninguno. Outputs: página seleccionada. Errores: ninguno."""
    st.sidebar.title(f"{APP_ICON} {APP_NAME}")
    st.sidebar.caption("MVP de proyectos territoriales para Quito.")
    return st.sidebar.radio(
        "Navegación",
        [
            "Inicio",
            "Explorar proyectos",
            "Match de talento",
            "Confianza y evidencia",
            "Postulaciones",
        ],
    )


def main():
    """Ejecuta router principal. Inputs: ninguno. Outputs: UI. Errores: ninguno."""
    initialize_app()
    projects = get_projects()
    page = render_navigation()

    if page == "Inicio":
        render_home_page()
    elif page == "Explorar proyectos":
        render_explore_page(projects)
    elif page == "Match de talento":
        render_match_page(projects)
    elif page == "Confianza y evidencia":
        render_evidence_page(projects)
    elif page == "Postulaciones":
        render_submissions_page()


main()
