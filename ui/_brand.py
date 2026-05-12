import streamlit as st


def inject_brand_styles():
    """Inyecta estilos visuales. Inputs: ninguno. Outputs: CSS en UI. Errores: ninguno."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        .hero-card {
            padding: 2rem;
            border-radius: 24px;
            background: linear-gradient(135deg, #102A43 0%, #1F5673 55%, #64B6AC 100%);
            color: white;
            margin-bottom: 1.5rem;
        }

        .hero-card h1 {
            font-size: 2.6rem;
            line-height: 1.05;
            margin-bottom: 0.8rem;
        }

        .soft-card {
            padding: 1.1rem;
            border: 1px solid #E6E0D4;
            border-radius: 18px;
            background: #FFFFFF;
            margin-bottom: 0.8rem;
        }

        .mini-label {
            color: #667085;
            font-size: 0.78rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }

        .tag {
            display: inline-block;
            padding: 0.25rem 0.65rem;
            margin: 0.12rem;
            border-radius: 999px;
            background: #EAF4F8;
            color: #1F5673;
            font-size: 0.78rem;
            font-weight: 600;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
