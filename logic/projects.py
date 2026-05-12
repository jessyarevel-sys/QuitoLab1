from config import PROJECTS


def get_projects():
    """Devuelve proyectos seed. Inputs: ninguno. Outputs: lista de proyectos. Errores: ninguno."""
    return PROJECTS


def get_unique_values(projects, key):
    """Extrae valores únicos. Inputs: proyectos y key. Outputs: lista ordenada. Errores: ninguno."""
    values = {project[key] for project in projects if key in project}
    return sorted(values)


def get_unique_skills(projects):
    """Extrae habilidades únicas. Inputs: proyectos. Outputs: lista ordenada. Errores: ninguno."""
    skills = {skill for project in projects for skill in project.get("needs", [])}
    return sorted(skills)


def filter_projects(projects, search, category, stage, district, skill):
    """Filtra proyectos. Inputs: filtros simples. Outputs: lista filtrada. Errores: ninguno."""
    filtered = projects
    query = search.strip().lower()

    if query:
        filtered = [
            project for project in filtered
            if query in project["name"].lower()
            or query in project["description"].lower()
            or query in project["district"].lower()
            or query in project["category"].lower()
        ]

    if category != "Todas":
        filtered = [project for project in filtered if project["category"] == category]

    if stage != "Todas":
        filtered = [project for project in filtered if project["stage"] == stage]

    if district != "Todos":
        filtered = [project for project in filtered if project["district"] == district]

    if skill != "Todas":
        filtered = [project for project in filtered if skill in project["needs"]]

    return filtered


def find_project_by_name(projects, name):
    """Busca proyecto por nombre. Inputs: proyectos y nombre. Outputs: dict o None. Errores: ninguno."""
    for project in projects:
        if project["name"] == name:
            return project
    return None
