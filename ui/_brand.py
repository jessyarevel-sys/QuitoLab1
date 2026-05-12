import streamlit as st


def inject_brand():
    """Aplica el sistema visual de Ciudad Lab en Streamlit."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

        :root {
            --cl-primary: #102A43;
            --cl-secondary: #F4EFE6;
            --cl-accent: #64B6AC;
            --cl-bg: #F8F5EF;
            --cl-surface: #FFFFFF;
            --cl-text: #102A43;
            --cl-muted: #667085;
            --cl-border: #E6E0D4;
            --cl-success: #3A7D44;
            --cl-warning: #D9902F;
            --cl-error: #B42318;

            --space-1: 4px;
            --space-2: 8px;
            --space-3: 12px;
            --space-4: 16px;
            --space-5: 24px;
            --space-6: 32px;
            --space-7: 48px;

            --radius-sm: 4px;
            --radius-md: 8px;
            --radius-lg: 16px;
            --radius-xl: 24px;

            --shadow-sm: 0 1px 2px rgba(16,42,67,.06);
            --shadow-md: 0 8px 24px rgba(16,42,67,.10);
            --shadow-lg: 0 18px 48px rgba(16,42,67,.16);
            --max-width: 1180px;
        }

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            color: var(--cl-text);
        }

        .block-container {
            max-width: var(--max-width);
            padding-top: var(--space-6);
            padding-bottom: var(--space-7);
        }

        h1, h2, h3 {
            font-family: 'Space Grotesk', sans-serif;
            letter-spacing: -0.035em;
            color: var(--cl-primary);
        }

        h1 {
            font-size: 3rem;
            line-height: 1.02;
        }

        h2 {
            font-size: 2rem;
            margin-top: var(--space-6);
        }

        h3 {
            font-size: 1.35rem;
        }

        p, li, label, span {
            font-family: 'Inter', sans-serif;
        }

        code, pre, [data-testid="stMetricValue"] {
            font-family: 'IBM Plex Mono', monospace;
        }

        section[data-testid="stSidebar"] {
            background: var(--cl-primary);
            border-right: 1px solid rgba(255,255,255,.08);
        }

        section[data-testid="stSidebar"] * {
            color: #FFFFFF !important;
        }

        section[data-testid="stSidebar"] .stRadio label {
            border-radius: var(--radius-md);
            padding: var(--space-1) var(--space-2);
        }

        .stButton button {
            background: var(--cl-primary);
            color: #FFFFFF;
            border: 1px solid var(--cl-primary);
            border-radius: var(--radius-lg);
            padding: .72rem 1rem;
            font-family: 'Inter', sans-serif;
            font-weight: 700;
            box-shadow: var(--shadow-sm);
            transition: all .16s ease;
        }

        .stButton button:hover {
            background: #1F5673;
            border-color: #1F5673;
            box-shadow: var(--shadow-md);
            transform: translateY(-1px);
        }

        .stDownloadButton button {
            background: var(--cl-accent);
            color: var(--cl-primary);
            border: 1px solid var(--cl-accent);
            border-radius: var(--radius-lg);
            font-weight: 700;
        }

        .stTextInput input,
        .stTextArea textarea,
        .stSelectbox div[data-baseweb="select"] > div,
        .stMultiSelect div[data-baseweb="select"] > div {
            background: var(--cl-surface);
            border: 1px solid var(--cl-border);
            border-radius: var(--radius-md);
            color: var(--cl-text);
            font-family: 'Inter', sans-serif;
        }

        .stTextInput input:focus,
        .stTextArea textarea:focus {
            border-color: var(--cl-accent);
            box-shadow: 0 0 0 3px rgba(100,182,172,.22);
        }

        div[data-testid="stForm"] {
            background: var(--cl-surface);
            border: 1px solid var(--cl-border);
            border-radius: var(--radius-xl);
            padding: var(--space-5);
            box-shadow: var(--shadow-sm);
        }

        div[data-testid="stMetric"] {
            background: var(--cl-surface);
            border: 1px solid var(--cl-border);
            border-radius: var(--radius-lg);
            padding: var(--space-4);
            box-shadow: var(--shadow-sm);
        }

        div[data-testid="stMetricValue"] {
            color: var(--cl-primary);
            font-weight: 500;
        }

        div[data-testid="stExpander"] {
            border: 1px solid var(--cl-border);
            border-radius: var(--radius-lg);
            background: var(--cl-surface);
            box-shadow: var(--shadow-sm);
        }

        .hero-card {
            padding: var(--space-7);
            border-radius: var(--radius-xl);
            background:
                radial-gradient(circle at 86% 18%, rgba(100,182,172,.28), transparent 24%),
                linear-gradient(135deg, #102A43 0%, #1F5673 100%);
            color: #FFFFFF;
            box-shadow: var(--shadow-lg);
            margin-bottom: var(--space-6);
        }

        .hero-card h1,
        .hero-card p {
            color: #FFFFFF;
        }

        .hero-card p {
            max-width: 760px;
            font-size: 1.08rem;
            line-height: 1.65;
        }

        .soft-card {
            background: var(--cl-surface);
            border: 1px solid var(--cl-border);
            border-radius: var(--radius-xl);
            padding: var(--space-5);
            box-shadow: var(--shadow-sm);
            margin-bottom: var(--space-4);
        }

        .mini-label {
            font-family: 'IBM Plex Mono', monospace;
            color: var(--cl-muted);
            font-size: .75rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: .08em;
        }

        .tag {
            display: inline-block;
            padding: 4px 10px;
            margin: 3px 4px 3px 0;
            border-radius: 999px;
            background: #EAF4F8;
            color: var(--cl-primary);
            font-size: .78rem;
            font-weight: 700;
        }

        .stAlert {
            border-radius: var(--radius-lg);
        }

        hr {
            border-color: var(--cl-border);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
