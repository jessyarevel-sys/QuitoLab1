import streamlit as st
from data.repositories import list_applications
from external.csv_export import export_applications_to_csv


def render_submissions_page():
    """Renderiza postulaciones. Inputs: ninguno. Outputs: UI. Errores: muestra error específico."""
    st.title("Postulaciones recibidas")
    st.write("Vista interna para revisar personas interesadas en los proyectos.")

    try:
        applications = list_applications()
    except RuntimeError as error:
        st.error(str(error))
        return

    if not applications:
        st.info("Todavía no hay postulaciones.")
        return

    st.metric("Total de postulaciones", len(applications))
    st.dataframe(applications, use_container_width=True, hide_index=True)

    try:
        csv_bytes = export_applications_to_csv(applications)
        st.download_button(
            label="Descargar CSV",
            data=csv_bytes,
            file_name="postulaciones_ciudad_lab.csv",
            mime="text/csv",
        )
    except RuntimeError as error:
        st.error(str(error))
