import streamlit as st
from config import USER_PROFILES
from logic.projects import get_unique_skills
from logic.matching import rank_projects_by_match
from ui.components import render_project_summary, render_project_needs, render_project_evidence


def render_match_page(projects):
    """Renderiza match. Inputs: proyectos. Outputs: UI. Errores: ninguno."""
    st.title("Match de talento")
    st.write("Selecciona habilidades para ver dónde puedes aportar con mayor claridad.")

    profile = st.selectbox("¿Qué tipo de actor eres?", list(USER_PROFILES.keys()))
    st.info(USER_PROFILES[profile]["description"])

    selected_skills = st.multiselect(
        "Habilidades o recursos",
        get_unique_skills(projects),
    )

    if not selected_skills:
        st.warning("Selecciona al menos una habilidad.")
        return

    ranked_projects = rank_projects_by_match(projects, selected_skills)
    visible_matches = [(project, score) for project, score in ranked_projects if score > 0]

    if not visible_matches:
        st.warning("No hay coincidencias directas. Prueba con otras habilidades.")
        return

    for project, score in visible_matches:
        with st.container(border=True):
            st.metric("Match", f"{score}%")
            render_project_summary(project)
            render_project_needs(project)
            render_project_evidence(project)
