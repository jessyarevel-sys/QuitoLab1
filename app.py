import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime
from pathlib import Path


# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

st.set_page_config(
    page_title="Ciudad Lab",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

DB_PATH = Path("ciudad_lab.db")


# ============================================================
# ESTILOS
# ============================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main {
        background-color: #F7F5EF;
    }

    .hero {
        padding: 2rem 2rem;
        border-radius: 24px;
        background: linear-gradient(135deg, #112D4E 0%, #1B4965 55%, #5FA8D3 100%);
        color: white;
        margin-bottom: 2rem;
    }

    .hero h1 {
        font-size: 3rem;
        line-height: 1.05;
        margin-bottom: 1rem;
        font-weight: 800;
    }

    .hero p {
        font-size: 1.1rem;
        line-height: 1.6;
        max-width: 850px;
    }

    .metric-card {
        padding: 1.2rem;
        border-radius: 18px;
        background: white;
        border: 1px solid #E8E3D8;
        box-shadow: 0px 6px 18px rgba(0,0,0,0.04);
    }

    .project-card {
        padding: 1.4rem;
        border-radius: 20px;
        background: #FFFFFF;
        border: 1px solid #E6E0D4;
        margin-bottom: 1rem;
        box-shadow: 0px 8px 22px rgba(0,0,0,0.04);
    }

    .tag {
        display: inline-block;
        padding: 0.25rem 0.65rem;
        margin: 0.15rem;
        border-radius: 999px;
        background: #EAF4F8;
        color: #1B4965;
        font-size: 0.78rem;
        font-weight: 600;
    }

    .trust-box {
        padding: 1rem;
        border-radius: 16px;
        background: #F1F8F6;
        border-left: 5px solid #3A7D44;
        margin-top: 1rem;
    }

    .warning-box {
        padding: 1rem;
        border-radius: 16px;
        background: #FFF7E6;
        border-left: 5px solid #F5A623;
        margin-top: 1rem;
    }

    .small-label {
        color: #6B7280;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    .footer {
        color: #6B7280;
        font-size: 0.85rem;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #DDD6C8;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# BASE DE DATOS
# ============================================================

def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id TEXT NOT NULL,
            project_name TEXT NOT NULL,
            applicant_name TEXT NOT NULL,
            applicant_profile TEXT NOT NULL,
            applicant_email TEXT NOT NULL,
            motivation TEXT NOT NULL,
            skills TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )

    conn.commit()
    conn.close()


def save_application(project_id, project_name, applicant_name, applicant_profile, applicant_email, motivation, skills):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO applications (
            project_id,
            project_name,
            applicant_name,
            applicant_profile,
            applicant_email,
            motivation,
            skills,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            project_id,
            project_name,
            applicant_name,
            applicant_profile,
            applicant_email,
            motivation,
            skills,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )

    conn.commit()
    conn.close()


def load_applications():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM applications ORDER BY created_at DESC", conn)
    conn.close()
    return df


init_db()


# ============================================================
# DATA MOCK DEL MVP
# ============================================================

PROJECTS = [
    {
        "id": "CL-001",
        "name": "Corredores Verdes de Barrio",
        "district": "La Floresta",
        "category": "Regeneración urbana",
        "stage": "Piloto",
        "impact": "Ambiental y comunitario",
        "owner": "Colectivo ciudadano + academia",
        "description": "Proyecto para transformar calles secundarias en corredores verdes caminables, conectando comercio local, sombra urbana y puntos de encuentro vecinal.",
        "needs": ["Urbanismo", "Diseño participativo", "Data urbana", "Comunicación comunitaria"],
        "investment": "Medio",
        "duration": "4 meses",
        "trust_score": 82,
        "evidence": [
            "Mapa base del barrio disponible",
            "Aliado académico confirmado",
            "Primer levantamiento ciudadano realizado"
        ]
    },
    {
        "id": "CL-002",
        "name": "Mapa de Calor de Seguridad Barrial",
        "district": "Centro Histórico",
        "category": "Datos de ciudad",
        "stage": "Investigación",
        "impact": "Seguridad y convivencia",
        "owner": "Gobierno local + ciudadanía",
        "description": "Iniciativa para mapear zonas de percepción de inseguridad, rutas evitadas y puntos críticos desde la experiencia ciudadana.",
        "needs": ["Research", "Visualización de datos", "UX", "Análisis territorial"],
        "investment": "Bajo",
        "duration": "8 semanas",
        "trust_score": 74,
        "evidence": [
            "Problema validado con vecinos",
            "Datos cualitativos iniciales",
            "Necesita protocolo de privacidad"
        ]
    },
    {
        "id": "CL-003",
        "name": "Laboratorio de Agua Comunitaria",
        "district": "Calderón",
        "category": "Resiliencia climática",
        "stage": "Concepto validado",
        "impact": "Agua, sostenibilidad y salud",
        "owner": "Academia + organización territorial",
        "description": "Laboratorio vivo para monitorear consumo, calidad y prácticas de cuidado del agua en comunidades con presión de crecimiento urbano.",
        "needs": ["Sostenibilidad", "IoT básico", "Educación comunitaria", "Gestión de datos"],
        "investment": "Alto",
        "duration": "6 meses",
        "trust_score": 68,
        "evidence": [
            "Comunidad interesada",
            "Problema territorial claro",
            "Falta modelo financiero"
        ]
    },
    {
        "id": "CL-004",
        "name": "Red de Oficios y Talento Local",
        "district": "Chillogallo",
        "category": "Economía local",
        "stage": "Piloto",
        "impact": "Empleo y comunidad",
        "owner": "Sector privado + ciudadanía",
        "description": "Sistema para conectar habilidades locales con microproyectos barriales, fortaleciendo empleabilidad, confianza y colaboración cercana.",
        "needs": ["Producto digital", "Investigación social", "Operaciones", "Alianzas"],
        "investment": "Medio",
        "duration": "3 meses",
        "trust_score": 79,
        "evidence": [
            "Necesidad validada",
            "Aliado privado interesado",
            "Primer listado de perfiles disponible"
        ]
    },
    {
        "id": "CL-005",
        "name": "Escuelas como Nodos de Cuidado",
        "district": "Quitumbe",
        "category": "Cuidado urbano",
        "stage": "Exploración",
        "impact": "Educación, familia y comunidad",
        "owner": "Academia + gobierno local",
        "description": "Proyecto para convertir escuelas en nodos de servicios comunitarios, aprendizaje intergeneracional y cuidado de proximidad.",
        "needs": ["Service design", "Política pública", "Facilitación", "Medición de impacto"],
        "investment": "Alto",
        "duration": "9 meses",
        "trust_score": 71,
        "evidence": [
            "Hipótesis clara",
            "Necesita validación institucional",
            "Alto potencial de impacto"
        ]
    }
]


USER_PROFILES = {
    "Talento profesional": {
        "description": "Busca proyectos donde aplicar conocimiento, construir portafolio y generar impacto visible.",
        "primary_need": "Encontrar oportunidades reales y confiables.",
        "success": "Postularse a un proyecto alineado con sus habilidades."
    },
    "Academia": {
        "description": "Busca llevar investigación, estudiantes y conocimiento al territorio.",
        "primary_need": "Conectar investigación con proyectos aplicados.",
        "success": "Vincular estudiantes, datos o líneas de investigación."
    },
    "Gobierno": {
        "description": "Busca identificar proyectos viables sin asumir toda la ejecución.",
        "primary_need": "Encontrar iniciativas estructuradas y confiables.",
        "success": "Priorizar proyectos donde invertir recursos o apoyo institucional."
    },
    "Ciudadanía": {
        "description": "Busca participar en iniciativas cercanas a su barrio y ver resultados concretos.",
        "primary_need": "Entender cómo participar y confiar en el proceso.",
        "success": "Sumarse a una iniciativa local con reglas claras."
    },
    "Inversor": {
        "description": "Busca oportunidades medibles, documentadas y con retorno o impacto claro.",
        "primary_need": "Evaluar riesgo, evidencia, monto, plazo e impacto.",
        "success": "Identificar proyectos confiables para analizar inversión."
    }
}


# ============================================================
# FUNCIONES DE APOYO
# ============================================================

def projects_to_dataframe():
    rows = []

    for project in PROJECTS:
        rows.append(
            {
                "ID": project["id"],
                "Proyecto": project["name"],
                "Barrio": project["district"],
                "Categoría": project["category"],
                "Etapa": project["stage"],
                "Impacto": project["impact"],
                "Inversión": project["investment"],
                "Duración": project["duration"],
                "Confianza": project["trust_score"],
                "Necesidades": ", ".join(project["needs"])
            }
        )

    return pd.DataFrame(rows)


def filter_projects(projects, search, category, stage, district, skill):
    filtered = projects

    if search:
        search_lower = search.lower()
        filtered = [
            project for project in filtered
            if search_lower in project["name"].lower()
            or search_lower in project["description"].lower()
            or search_lower in project["district"].lower()
            or search_lower in project["category"].lower()
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


def calculate_match_score(project, selected_skills):
    if not selected_skills:
        return 0

    project_skills = set(project["needs"])
    user_skills = set(selected_skills)

    overlap = project_skills.intersection(user_skills)
    score = int((len(overlap) / len(project_skills)) * 100)

    return score


def render_project_card(project, show_apply=True):
    st.markdown(
        f"""
        <div class="project-card">
            <div class="small-label">{project["id"]} · {project["district"]} · {project["stage"]}</div>
            <h3>{project["name"]}</h3>
            <p>{project["description"]}</p>
            <p><strong>Categoría:</strong> {project["category"]}</p>
            <p><strong>Impacto:</strong> {project["impact"]}</p>
            <p><strong>Duración estimada:</strong> {project["duration"]}</p>
            <p><strong>Nivel de inversión:</strong> {project["investment"]}</p>
            <p><strong>Actor impulsor:</strong> {project["owner"]}</p>
            <p><strong>Índice de confianza:</strong> {project["trust_score"]}/100</p>
            <div>
                {"".join([f'<span class="tag">{need}</span>' for need in project["needs"]])}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.expander("Ver evidencia de confianza"):
        for item in project["evidence"]:
            st.write(f"✓ {item}")

        if project["trust_score"] >= 80:
            st.success("Proyecto con buena base de confianza para activar participación.")
        elif project["trust_score"] >= 70:
            st.warning("Proyecto prometedor, pero requiere fortalecer documentación o respaldo.")
        else:
            st.error("Proyecto con potencial, pero todavía necesita evidencia para generar confianza.")

    if show_apply:
        with st.expander("Manifestar interés / Postularme"):
            with st.form(f"apply_form_{project['id']}"):
                applicant_name = st.text_input("Nombre completo")
                applicant_profile = st.selectbox(
                    "Perfil",
                    list(USER_PROFILES.keys())
                )
                applicant_email = st.text_input("Correo electrónico")
                skills = st.text_area(
                    "Habilidades o recursos que puedes aportar",
                    placeholder="Ejemplo: UX research, análisis de datos, gestión comunitaria..."
                )
                motivation = st.text_area(
                    "¿Por qué te interesa este proyecto?",
                    placeholder="Explica brevemente tu motivación y cómo podrías aportar."
                )

                submitted = st.form_submit_button("Enviar interés")

                if submitted:
                    if not applicant_name or not applicant_email or not motivation or not skills:
                        st.error("Completa todos los campos antes de enviar.")
                    else:
                        save_application(
                            project_id=project["id"],
                            project_name=project["name"],
                            applicant_name=applicant_name,
                            applicant_profile=applicant_profile,
                            applicant_email=applicant_email,
                            motivation=motivation,
                            skills=skills
                        )
                        st.success("Tu interés fue registrado. En una versión futura, el equipo del proyecto recibiría esta postulación.")


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🏙️ Ciudad Lab")
st.sidebar.caption("MVP para conectar talento, proyectos y oportunidades de impacto urbano en Quito.")

page = st.sidebar.radio(
    "Navegación",
    [
        "Inicio",
        "Explorar proyectos",
        "Match de talento",
        "Mapa de oportunidades",
        "Confianza y evidencia",
        "Postulaciones recibidas"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Perfiles del ecosistema")
for profile in USER_PROFILES:
    st.sidebar.markdown(f"- {profile}")


# ============================================================
# PÁGINA: INICIO
# ============================================================

if page == "Inicio":
    st.markdown(
        """
        <div class="hero">
            <h1>Ciudad Lab conecta proyectos reales con talento, confianza y acción colectiva.</h1>
            <p>
            Una plataforma para descubrir oportunidades de impacto territorial en Quito,
            entender quién las impulsa, qué evidencia tienen y cómo diferentes actores
            pueden participar de forma clara.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """
            <div class="metric-card">
                <div class="small-label">Proyectos activos</div>
                <h2>5</h2>
                <p>Iniciativas territoriales iniciales para validar el MVP.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="metric-card">
                <div class="small-label">Perfiles conectados</div>
                <h2>5</h2>
                <p>Talento, academia, gobierno, ciudadanía e inversión.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="metric-card">
                <div class="small-label">Función principal</div>
                <h2>Match</h2>
                <p>Conectar habilidades con necesidades reales de proyectos.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            """
            <div class="metric-card">
                <div class="small-label">Valor central</div>
                <h2>Confianza</h2>
                <p>Mostrar evidencia antes de pedir participación.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("## ¿Qué problema resuelve?")

    st.write(
        """
        En Quito existen iniciativas, talento, conocimiento académico, necesidades ciudadanas,
        interés institucional e inversión potencial. El problema es que estos elementos viven
        fragmentados. Ciudad Lab funciona como un punto de encuentro para que los proyectos
        no dependan solo de contactos personales, sino de información clara, evidencia y
        mecanismos simples de participación.
        """
    )

    st.markdown("## Scope del MVP")

    st.markdown(
        """
        Este MVP no intenta resolver toda la plataforma final. Se enfoca en tres acciones críticas:

        1. **Encontrar proyectos reales** filtrando por barrio, categoría, etapa o habilidades requeridas.  
        2. **Evaluar confianza** revisando evidencia básica, actor impulsor e índice de claridad del proyecto.  
        3. **Manifestar interés** para participar, colaborar o postularse según el perfil del usuario.
        """
    )

    st.markdown(
        """
        <div class="trust-box">
        <strong>Principio de producto:</strong> si una funcionalidad no ayuda a encontrar,
        confiar o vincularse a un proyecto, queda fuera del MVP.
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PÁGINA: EXPLORAR PROYECTOS
# ============================================================

elif page == "Explorar proyectos":
    st.title("Explorar proyectos")

    st.write(
        """
        Encuentra iniciativas territoriales según ubicación, categoría, etapa de desarrollo
        o habilidades que necesitan.
        """
    )

    all_categories = sorted(list(set(project["category"] for project in PROJECTS)))
    all_stages = sorted(list(set(project["stage"] for project in PROJECTS)))
    all_districts = sorted(list(set(project["district"] for project in PROJECTS)))
    all_skills = sorted(list(set(skill for project in PROJECTS for skill in project["needs"])))

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        search = st.text_input("Buscar", placeholder="Ejemplo: agua, barrio, datos...")

    with col2:
        category = st.selectbox("Categoría", ["Todas"] + all_categories)

    with col3:
        stage = st.selectbox("Etapa", ["Todas"] + all_stages)

    with col4:
        district = st.selectbox("Barrio", ["Todos"] + all_districts)

    skill = st.selectbox("Habilidad requerida", ["Todas"] + all_skills)

    filtered_projects = filter_projects(PROJECTS, search, category, stage, district, skill)

    st.markdown(f"### {len(filtered_projects)} proyecto(s) encontrados")

    if not filtered_projects:
        st.warning("No se encontraron proyectos con esos filtros. Prueba quitando algún criterio.")
    else:
        for project in filtered_projects:
            render_project_card(project)


# ============================================================
# PÁGINA: MATCH DE TALENTO
# ============================================================

elif page == "Match de talento":
    st.title("Match de talento")

    st.write(
        """
        Selecciona tus habilidades para encontrar proyectos donde tu perfil puede aportar
        valor de forma más directa.
        """
    )

    all_skills = sorted(list(set(skill for project in PROJECTS for skill in project["needs"])))

    selected_profile = st.selectbox(
        "¿Qué tipo de actor eres?",
        list(USER_PROFILES.keys())
    )

    st.info(USER_PROFILES[selected_profile]["description"])

    selected_skills = st.multiselect(
        "Selecciona tus habilidades, recursos o áreas de experiencia",
        all_skills
    )

    if selected_skills:
        scored_projects = []

        for project in PROJECTS:
            score = calculate_match_score(project, selected_skills)
            scored_projects.append((project, score))

        scored_projects = sorted(scored_projects, key=lambda item: item[1], reverse=True)

        st.markdown("## Proyectos recomendados")

        for project, score in scored_projects:
            if score > 0:
                st.markdown(f"### Match: {score}%")
                render_project_card(project)

        if all(score == 0 for _, score in scored_projects):
            st.warning("No hay coincidencias directas. Prueba seleccionando otras habilidades.")
    else:
        st.warning("Selecciona al menos una habilidad para calcular tu match.")


# ============================================================
# PÁGINA: MAPA DE OPORTUNIDADES
# ============================================================

elif page == "Mapa de oportunidades":
    st.title("Mapa de oportunidades")

    st.write(
        """
        Vista inicial de distribución territorial. En esta versión MVP usamos una tabla
        priorizada por barrio, etapa e impacto. En una siguiente iteración puede conectarse
        con un mapa interactivo.
        """
    )

    df = projects_to_dataframe()

    st.dataframe(
        df[
            [
                "ID",
                "Proyecto",
                "Barrio",
                "Categoría",
                "Etapa",
                "Impacto",
                "Confianza"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    st.markdown("## Lectura rápida por barrio")

    district_summary = (
        df.groupby("Barrio")
        .agg(
            Proyectos=("Proyecto", "count"),
            Confianza_promedio=("Confianza", "mean")
        )
        .reset_index()
    )

    district_summary["Confianza_promedio"] = district_summary["Confianza_promedio"].round(1)

    st.dataframe(
        district_summary,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        """
        <div class="warning-box">
        <strong>Nota MVP:</strong> el mapa visual no se incluye todavía para mantener
        el build liviano en Streamlit free tier. La prioridad es validar si la gente
        entiende los proyectos y quiere vincularse.
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PÁGINA: CONFIANZA Y EVIDENCIA
# ============================================================

elif page == "Confianza y evidencia":
    st.title("Confianza y evidencia")

    st.write(
        """
        La confianza es el centro de Ciudad Lab. Antes de pedir participación,
        cada proyecto debe mostrar evidencia mínima: quién lo impulsa, en qué etapa está,
        qué necesita, qué datos existen y qué falta validar.
        """
    )

    df = projects_to_dataframe()

    col1, col2 = st.columns([1, 2])

    with col1:
        selected_project_name = st.selectbox(
            "Selecciona un proyecto",
            [project["name"] for project in PROJECTS]
        )

    selected_project = next(project for project in PROJECTS if project["name"] == selected_project_name)

    with col2:
        st.metric("Índice de confianza", f"{selected_project['trust_score']}/100")

    st.markdown("## Ficha de evidencia")

    st.markdown(f"**Proyecto:** {selected_project['name']}")
    st.markdown(f"**Actor impulsor:** {selected_project['owner']}")
    st.markdown(f"**Etapa:** {selected_project['stage']}")
    st.markdown(f"**Duración estimada:** {selected_project['duration']}")
    st.markdown(f"**Nivel de inversión:** {selected_project['investment']}")

    st.markdown("### Evidencia disponible")

    for evidence in selected_project["evidence"]:
        st.write(f"✓ {evidence}")

    st.markdown("### Riesgo interpretado")

    if selected_project["trust_score"] >= 80:
        st.success("Alta claridad inicial. El proyecto puede activar participación temprana.")
    elif selected_project["trust_score"] >= 70:
        st.warning("Claridad media. Conviene fortalecer documentación antes de pedir inversión o participación amplia.")
    else:
        st.error("Claridad baja. El proyecto debe validar más evidencia antes de escalar.")

    st.markdown("## Matriz general de confianza")

    st.dataframe(
        df[
            [
                "ID",
                "Proyecto",
                "Etapa",
                "Inversión",
                "Duración",
                "Confianza"
            ]
        ].sort_values(by="Confianza", ascending=False),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PÁGINA: POSTULACIONES RECIBIDAS
# ============================================================

elif page == "Postulaciones recibidas":
    st.title("Postulaciones recibidas")

    st.write(
        """
        Esta sección permite revisar las personas que manifestaron interés.
        En una versión real, esta vista sería privada para administradores o equipos de proyecto.
        """
    )

    applications_df = load_applications()

    if applications_df.empty:
        st.info("Todavía no hay postulaciones registradas.")
    else:
        st.metric("Total de postulaciones", len(applications_df))

        st.dataframe(
            applications_df[
                [
                    "created_at",
                    "project_name",
                    "applicant_name",
                    "applicant_profile",
                    "applicant_email",
                    "skills",
                    "motivation"
                ]
            ],
            use_container_width=True,
            hide_index=True
        )

        csv = applications_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Descargar postulaciones en CSV",
            data=csv,
            file_name="postulaciones_ciudad_lab.csv",
            mime="text/csv"
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
    Ciudad Lab · MVP académico para validar descubrimiento de proyectos, confianza y vinculación de talento.
    </div>
    """,
    unsafe_allow_html=True
)
