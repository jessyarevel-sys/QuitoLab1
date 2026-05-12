import csv
from config import CSV_EXPORT_PATH


def export_applications_to_csv(applications):
    """Exporta postulaciones. Inputs: lista de dicts. Outputs: bytes CSV. Errores: RuntimeError específico."""
    if not applications:
        return b""

    try:
        fieldnames = list(applications[0].keys())
        with open(CSV_EXPORT_PATH, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(applications)

        with open(CSV_EXPORT_PATH, "rb") as csv_file:
            return csv_file.read()
    except OSError as error:
        raise RuntimeError(f"No se pudo exportar el CSV en /tmp: {error}") from error
