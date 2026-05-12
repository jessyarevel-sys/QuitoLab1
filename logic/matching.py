def calculate_match_score(project_needs, selected_skills):
    """Calcula match porcentual. Inputs: necesidades y habilidades. Outputs: int 0-100. Errores: ninguno."""
    if not selected_skills or not project_needs:
        return 0

    needs = set(project_needs)
    skills = set(selected_skills)
    overlap = needs.intersection(skills)

    return int((len(overlap) / len(needs)) * 100)


def rank_projects_by_match(projects, selected_skills):
    """Ordena proyectos por match. Inputs: proyectos y habilidades. Outputs: lista de tuplas. Errores: ninguno."""
    scored = [
        (project, calculate_match_score(project["needs"], selected_skills))
        for project in projects
    ]
    return sorted(scored, key=lambda item: item[1], reverse=True)
