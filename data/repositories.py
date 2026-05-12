import sqlite3
from datetime import datetime
from data.database import get_connection
from data.models import Application


def create_application(application):
    """Guarda postulación. Inputs: Application. Outputs: None. Errores: RuntimeError específico."""
    try:
        with get_connection() as connection:
            connection.execute(
                """
                INSERT INTO applications (
                    project_id, project_name, applicant_name, applicant_profile,
                    applicant_email, skills, motivation, created_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    application.project_id,
                    application.project_name,
                    application.applicant_name,
                    application.applicant_profile,
                    application.applicant_email,
                    application.skills,
                    application.motivation,
                    application.created_at,
                ),
            )
            connection.commit()
    except sqlite3.Error as error:
        raise RuntimeError(f"No se pudo guardar la postulación: {error}") from error


def build_application(project, form_data):
    """Construye Application. Inputs: proyecto y formulario. Outputs: Application. Errores: KeyError si falta campo."""
    try:
        return Application(
            project_id=project["id"],
            project_name=project["name"],
            applicant_name=form_data["applicant_name"],
            applicant_profile=form_data["applicant_profile"],
            applicant_email=form_data["applicant_email"],
            skills=form_data["skills"],
            motivation=form_data["motivation"],
            created_at=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        )
    except KeyError as error:
        raise RuntimeError(f"Falta un campo para construir la postulación: {error}") from error


def list_applications():
    """Lista postulaciones. Inputs: ninguno. Outputs: lista de dicts. Errores: RuntimeError específico."""
    try:
        with get_connection() as connection:
            connection.row_factory = sqlite3.Row
            rows = connection.execute(
                """
                SELECT project_name, applicant_name, applicant_profile,
                       applicant_email, skills, motivation, created_at
                FROM applications
                ORDER BY created_at DESC
                """
            ).fetchall()
            return [dict(row) for row in rows]
    except sqlite3.Error as error:
        raise RuntimeError(f"No se pudieron leer las postulaciones: {error}") from error
