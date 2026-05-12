# QuitoLab1
Plataforma ejemplo

/
├── app.py — dueño: entry point y router; principio: separación de responsabilidades.
├── config.py — dueño: constantes, paths y seed data; principio: claridad sin números mágicos.
├── /data/models.py — dueño: modelos de datos; principio: determinismo.
├── /data/database.py — dueño: conexión SQLite y migración; principio: resiliencia.
├── /data/repositories.py — dueño: lectura/escritura de postulaciones; principio: I/O aislado.
├── /logic/projects.py — dueño: filtros y lectura de proyectos; principio: reglas puras.
├── /logic/matching.py — dueño: cálculo de match; principio: mismo input, mismo output.
├── /logic/validation.py — dueño: validación de formularios; principio: fallar fuerte.
├── /external/csv_export.py — dueño: exportar postulaciones a CSV; principio: I/O envuelto.
├── /ui/components.py — dueño: componentes Streamlit reutilizables; principio: modularidad.
├── /ui/home.py — dueño: página de inicio; principio: UI sin reglas de negocio.
├── /ui/explore.py — dueño: exploración de proyectos; principio: UI llama lógica.
├── /ui/match.py — dueño: match de talento; principio: UI llama lógica.
├── /ui/evidence.py — dueño: confianza y evidencia; principio: UI presenta datos.
├── /ui/submissions.py — dueño: vista de postulaciones; principio: UI no escribe archivos directo.
├── requirements.txt — dueño: dependencias pineadas; principio: deploy reproducible.
└── runtime.txt — dueño: versión Python para Streamlit Cloud; principio: entorno estable.
