import sqlite3
from config import DB_PATH


def get_connection():
    """Abre conexión SQLite. Inputs: ninguno. Outputs: conexión SQLite. Errores: RuntimeError específico."""
    try:
        return sqlite3.connect(DB_PATH)
    except sqlite3.Error as error:
        raise RuntimeError(f"No se pudo abrir la base SQLite en /tmp: {error}") from error


def initialize_database():
    """Crea tablas necesarias. Inputs: ninguno. Outputs: None. Errores: RuntimeError específico."""
    try:
        with get_connection() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS applications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id TEXT NOT NULL,
                    project_name TEXT NOT NULL,
                    applicant_name TEXT NOT NULL,
                    applicant_profile TEXT NOT NULL,
                    applicant_email TEXT NOT NULL,
                    skills TEXT NOT NULL,
                    motivation TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )
            connection.commit()
    except sqlite3.Error as error:
        raise RuntimeError(f"No se pudo inicializar la tabla applications: {error}") from error
