import streamlit as st
from logic.projects import find_project_by_name
from ui.components import render_project_summary, render_project_evidence


def render_evidence_page(projects):
    """Renderiza evidencia. Inputs: proyectos. Outputs: UI. Errores: ninguno."""
    st.title("Confianza y evidencia")
    st.write("Cada proyecto debe mostrar quién lo impulsa, qué tiene validado y qué falta.")

    project_names = [project["name"] for project in projects]
    selected_name = st.selectbox("Proyecto", project_names)
    project = find_project_by_name(projects, selected_name)

    if project is None:
        st.error("No se encontró el proyecto seleccionado.")
        return

    render_project_summary(project)
    render_project_evidence(project)

    rows = [
        {
            "Proyecto": item["name"],
            "Barrio": item["district"],
            "Etapa": item["stage"],
            "Confianza": item["trust_score"],
        }
        for item in projects
    ]

    st.subheader("Matriz general")
    st.dataframe(rows, use_container_width=True, hide_index=True)
