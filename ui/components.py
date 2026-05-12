import streamlit as st
from config import HIGH_TRUST_THRESHOLD, MEDIUM_TRUST_THRESHOLD


def render_project_summary(project):
    """Renderiza resumen de proyecto. Inputs: proyecto. Outputs: UI. Errores: ninguno."""
    st.subheader(project["name"])
    st.caption(f'{project["id"]} · {project["district"]} · {project["stage"]}')
    st.write(project["description"])
    st.write(f'**Categoría:** {project["category"]}')
    st.write(f'**Impacto:** {project["impact"]}')
    st.write(f'**Actor impulsor:** {project["owner"]}')
    st.write(f'**Duración:** {project["duration"]}')
    st.write(f'**Inversión:** {project["investment"]}')
    st.progress(project["trust_score"] / 100)
    st.caption(f'Confianza: {project["trust_score"]}/100')


def render_project_needs(project):
    """Renderiza necesidades. Inputs: proyecto. Outputs: UI. Errores: ninguno."""
    st.write("**Necesita:**")
    st.write(" · ".join(project["needs"]))


def render_project_evidence(project):
    """Renderiza evidencia. Inputs: proyecto. Outputs: UI. Errores: ninguno."""
    with st.expander("Ver evidencia"):
        for item in project["evidence"]:
            st.write(f"✓ {item}")
        render_trust_message(project["trust_score"])


def render_trust_message(score):
    """Renderiza estado de confianza. Inputs: score. Outputs: UI. Errores: ninguno."""
    if score >= HIGH_TRUST_THRESHOLD:
        st.success("Base de confianza alta para activar participación.")
    elif score >= MEDIUM_TRUST_THRESHOLD:
        st.warning("Debe fortalecer documentación antes de escalar.")
    else:
        st.error("Necesita más evidencia antes de pedir participación amplia.")


def render_application_form(project, profiles):
    """Renderiza formulario. Inputs: proyecto y perfiles. Outputs: dict o None. Errores: ninguno."""
    with st.form(f'application_form_{project["id"]}'):
        applicant_name = st.text_input("Nombre completo")
        applicant_profile = st.selectbox("Perfil", list(profiles.keys()))
        applicant_email = st.text_input("Correo electrónico")
        skills = st.text_area("Habilidades o recursos que puedes aportar")
        motivation = st.text_area("¿Por qué te interesa este proyecto?")
        submitted = st.form_submit_button("Enviar interés")

    if not submitted:
        return None

    return {
        "applicant_name": applicant_name,
        "applicant_profile": applicant_profile,
        "applicant_email": applicant_email,
        "skills": skills,
        "motivation": motivation,
    }
