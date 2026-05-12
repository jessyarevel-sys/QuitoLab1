import streamlit as st

from config import HIGH_TRUST_THRESHOLD, MEDIUM_TRUST_THRESHOLD


def render_project_summary(project):
    """Renderiza resumen de proyecto. Inputs: proyecto. Outputs: UI. Errores: ninguno."""
    st.markdown(
        f"""
        <div class="soft-card">
            <div class="mini-label">{project["id"]} · {project["district"]} · {project["stage"]}</div>
            <h3>{project["name"]}</h3>
            <p>{project["description"]}</p>
            <p><strong>Categoría:</strong> {project["category"]}</p>
            <p><strong>Impacto:</strong> {project["impact"]}</p>
            <p><strong>Actor impulsor:</strong> {project["owner"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(project["trust_score"] / 100)
    st.caption(f'Índice de confianza: {project["trust_score"]}/100')


def render_project_needs(project):
    """Renderiza necesidades. Inputs: proyecto. Outputs: UI. Errores: ninguno."""
    tags = "".join([f'<span class="tag">{need}</span>' for need in project["needs"]])
    st.markdown(tags, unsafe_allow_html=True)


def render_project_evidence(project):
    """Renderiza evidencia. Inputs: proyecto. Outputs: UI. Errores: ninguno."""
    with st.expander("Ver evidencia antes de participar"):
        for item in project["evidence"]:
            st.write(f"✓ {item}")
        render_trust_message(project["trust_score"])


def render_trust_message(score):
    """Renderiza estado de confianza. Inputs: score. Outputs: UI. Errores: ninguno."""
    if score >= HIGH_TRUST_THRESHOLD:
        st.success("Este proyecto tiene una base clara para activar participación.")
    elif score >= MEDIUM_TRUST_THRESHOLD:
        st.warning("Este proyecto es prometedor, pero necesita reforzar documentación.")
    else:
        st.error("Este proyecto necesita más evidencia antes de pedir participación amplia.")


def render_application_form(project, profiles):
    """Renderiza formulario. Inputs: proyecto y perfiles. Outputs: dict o None. Errores: ninguno."""
    with st.form(f'application_form_{project["id"]}'):
        st.write("**Manifiesta interés**")
        applicant_name = st.text_input(
            "Nombre completo",
            help="Usaremos este dato para identificar tu postulación.",
        )
        applicant_profile = st.selectbox(
            "Perfil",
            list(profiles.keys()),
            help="Elige el rol desde el que quieres vincularte al proyecto.",
        )
        applicant_email = st.text_input(
            "Correo electrónico",
            help="Debe tener formato nombre@dominio.com.",
        )
        skills = st.text_area(
            "Habilidades o recursos que puedes aportar",
            help="Ejemplo: UX research, visualización de datos, gestión comunitaria.",
        )
        motivation = st.text_area(
            "¿Por qué te interesa este proyecto?",
            help="Cuenta qué te mueve y cómo podrías aportar.",
        )
        submitted = st.form_submit_button("Registrar mi interés")

    if not submitted:
        return None

    return {
        "applicant_name": applicant_name,
        "applicant_profile": applicant_profile,
        "applicant_email": applicant_email,
        "skills": skills,
        "motivation": motivation,
    }


def render_empty_state(title, body):
    """Renderiza estado vacío. Inputs: título y cuerpo. Outputs: UI. Errores: ninguno."""
    st.info(f"**{title}**\n\n{body}")


def render_error_state(message):
    """Renderiza error visible. Inputs: mensaje. Outputs: UI. Errores: ninguno."""
    st.error(f"No pudimos completar esta acción. {message}")


def render_success_state(message):
    """Renderiza éxito visible. Inputs: mensaje. Outputs: UI. Errores: ninguno."""
    st.success(message)
    st.toast(message, icon="✅")
