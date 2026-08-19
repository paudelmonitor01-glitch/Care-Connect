import streamlit as st

from home import render as render_home


st.set_page_config(
    page_title="Care Connect",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ------------------------------------------------------------
# Streamlit shell cleanup
# ------------------------------------------------------------
st.markdown(
    """
    <style>
        #MainMenu,
        footer,
        header[data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"] {
            display: none !important;
        }

        html, body, .stApp,
        [data-testid="stAppViewContainer"] {
            margin: 0 !important;
            padding: 0 !important;
            background: #ffffff !important;
        }

        [data-testid="stAppViewContainer"] > .main,
        [data-testid="stMain"],
        section.main {
            margin: 0 !important;
            padding: 0 !important;
        }

        [data-testid="stMainBlockContainer"],
        .block-container {
            width: 100% !important;
            max-width: 100% !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        [data-testid="stVerticalBlock"] {
            gap: 0 !important;
        }

        [data-testid="stElementContainer"] {
            margin: 0 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def main():
    # For now there is only the Home page.
    # Later you can add Product.py, About.py, Donate.py, etc.
    render_home()


if __name__ == "__main__":
    main()
