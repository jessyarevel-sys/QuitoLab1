from data.models import ValidationResult
from config import REQUIRED_APPLICATION_FIELDS


def is_blank(value):
    """Detecta vacío. Inputs: cualquier valor. Outputs: bool. Errores: ninguno."""
    return value is None or str(value).strip() == ""


def validate_email(email):
    """Valida email básico. Inputs: email. Outputs: ValidationResult. Errores: ninguno."""
    if is_blank(email):
        return ValidationResult(False, "El correo es obligatorio.")
    if "@" not in email or "." not in email:
        return ValidationResult(False, "El correo no tiene un formato válido.")
    return ValidationResult(True, "Correo válido.")


def validate_application_form(form_data):
    """Valida formulario. Inputs: dict. Outputs: ValidationResult. Errores: ninguno."""
    for field in REQUIRED_APPLICATION_FIELDS:
        if field not in form_data or is_blank(form_data[field]):
            return ValidationResult(False, "Completa todos los campos antes de enviar.")

    email_result = validate_email(form_data["applicant_email"])
    if not email_result.is_valid:
        return email_result

    return ValidationResult(True, "Formulario válido.")
