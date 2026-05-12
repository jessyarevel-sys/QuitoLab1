from dataclasses import dataclass


@dataclass(frozen=True)
class Application:
    """Representa una postulación. Inputs: campos del formulario. Outputs: objeto inmutable. Errores: ninguno."""
    project_id: str
    project_name: str
    applicant_name: str
    applicant_profile: str
    applicant_email: str
    skills: str
    motivation: str
    created_at: str


@dataclass(frozen=True)
class ValidationResult:
    """Representa validación. Inputs: estado booleano y mensaje. Outputs: resultado inmutable. Errores: ninguno."""
    is_valid: bool
    message: str
