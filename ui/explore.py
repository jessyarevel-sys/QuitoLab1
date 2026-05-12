import streamlit as st
from config import USER_PROFILES
from data.repositories import build_application, create_application
from logic.projects import get_unique_values, get_unique_skills, filter_projects
from logic.validation import validate_application_form
from ui.components import render_project_summary, render_project_needs, render_project_evidence, render_application_form


def render_explore_page(projects):
    """Renderiza exploración. Inputs: proyectos. Outputs: UI. Errores: muestra error específico."""
    st.title("Explorar proyectos")
    st.write("Filtra oportunidades por barrio, etapa, categoría o habilidad requerida.")

    search = st.text_input("Buscar", placeholder="Ejemplo: agua, barrio, datos")
    category = st.selectbox("Categoría", ["Todas"] + get_unique_values(projects, "category"))
    stage = st.selectbox("Etapa", ["Todas"] + get_unique_values(projects, "stage"))
    district = st.selectbox("Barrio", ["Todos"] + get_unique_values(projects, "district"))
    skill = st.selectbox("Habilidad", ["Todas"] + get_unique_skills(projects))

    filtered = filter_projects(projects, search, category, stage, district, skill)
    st.subheader(f"{len(filtered)} proyecto(s) encontrados")

    for project in filtered:
        with st.container(border=True):
            render_project_summary(project)
            render_project_needs(project)
            render_project_evidence(project)
            form_data = render_application_form(project, USER_PROFILES)

            if form_data:
                validation = validate_application_form(form_data)
                if not validation.is_valid:
                    st.error(validation.message)
                else:
                    try:
                        application = build_application(project, form_data)
                        create_application(application)
                        st.success("Tu interés fue registrado.")
                    except RuntimeError as error:
                        st.error(str(error))
