from pathlib import Path

APP_NAME = "Ciudad Lab"
APP_ICON = "🏙️"

TMP_DIR = Path("/tmp")
DB_PATH = TMP_DIR / "ciudad_lab.db"
CSV_EXPORT_PATH = TMP_DIR / "postulaciones_ciudad_lab.csv"

PAGE_OPTIONS = [
    "Inicio",
    "Explorar proyectos",
    "Match de talento",
    "Confianza y evidencia",
    "Postulaciones",
]

ALL_OPTION = "Todas"
ALL_DISTRICTS_OPTION = "Todos"

MIN_TRUST_SCORE = 0
MAX_TRUST_SCORE = 100
HIGH_TRUST_THRESHOLD = 80
MEDIUM_TRUST_THRESHOLD = 70

MIN_MOTIVATION_LENGTH = 20
MIN_SKILLS_LENGTH = 8

REQUIRED_APPLICATION_FIELDS = [
    "applicant_name",
    "applicant_profile",
    "applicant_email",
    "skills",
    "motivation",
]

USER_PROFILES = {
    "Talento profesional": {
        "description": "Busca proyectos donde aplicar conocimiento y generar impacto visible.",
        "primary_need": "Encontrar oportunidades reales y confiables.",
    },
    "Academia": {
        "description": "Busca llevar investigación, estudiantes y conocimiento al territorio.",
        "primary_need": "Conectar investigación con proyectos aplicados.",
    },
    "Gobierno": {
        "description": "Busca identificar proyectos viables sin cargar toda la ejecución.",
        "primary_need": "Encontrar iniciativas estructuradas y confiables.",
    },
    "Ciudadanía": {
        "description": "Busca participar en iniciativas cercanas a su barrio y ver resultados.",
        "primary_need": "Entender cómo participar y confiar en el proceso.",
    },
    "Inversor": {
        "description": "Busca oportunidades medibles, documentadas y con riesgo claro.",
        "primary_need": "Evaluar monto, plazo, evidencia e impacto.",
    },
}

PROJECTS = [
    {
        "id": "CL-001",
        "name": "Corredores Verdes de Barrio",
        "district": "La Floresta",
        "category": "Regeneración urbana",
        "stage": "Piloto",
        "impact": "Ambiental y comunitario",
        "owner": "Colectivo ciudadano + academia",
        "description": "Transforma calles secundarias en corredores verdes caminables.",
        "needs": ["Urbanismo", "Diseño participativo", "Data urbana", "Comunicación comunitaria"],
        "investment": "Medio",
        "duration": "4 meses",
        "trust_score": 82,
        "evidence": ["Mapa base disponible", "Aliado académico confirmado", "Levantamiento ciudadano realizado"],
    },
    {
        "id": "CL-002",
        "name": "Mapa de Seguridad Barrial",
        "district": "Centro Histórico",
        "category": "Datos de ciudad",
        "stage": "Investigación",
        "impact": "Seguridad y convivencia",
        "owner": "Gobierno local + ciudadanía",
        "description": "Mapea percepción de inseguridad, rutas evitadas y puntos críticos.",
        "needs": ["Research", "Visualización de datos", "UX", "Análisis territorial"],
        "investment": "Bajo",
        "duration": "8 semanas",
        "trust_score": 74,
        "evidence": ["Problema validado", "Datos iniciales", "Requiere protocolo de privacidad"],
    },
    {
        "id": "CL-003",
        "name": "Laboratorio de Agua Comunitaria",
        "district": "Calderón",
        "category": "Resiliencia climática",
        "stage": "Concepto validado",
        "impact": "Agua, sostenibilidad y salud",
        "owner": "Academia + organización territorial",
        "description": "Monitorea consumo, calidad y prácticas de cuidado del agua.",
        "needs": ["Sostenibilidad", "IoT básico", "Educación comunitaria", "Gestión de datos"],
        "investment": "Alto",
        "duration": "6 meses",
        "trust_score": 68,
        "evidence": ["Comunidad interesada", "Problema claro", "Falta modelo financiero"],
    },
    {
        "id": "CL-004",
        "name": "Red de Oficios y Talento Local",
        "district": "Chillogallo",
        "category": "Economía local",
        "stage": "Piloto",
        "impact": "Empleo y comunidad",
        "owner": "Sector privado + ciudadanía",
        "description": "Conecta habilidades locales con microproyectos barriales.",
        "needs": ["Producto digital", "Investigación social", "Operaciones", "Alianzas"],
        "investment": "Medio",
        "duration": "3 meses",
        "trust_score": 79,
        "evidence": ["Necesidad validada", "Aliado privado interesado", "Listado inicial de perfiles"],
    },
]
