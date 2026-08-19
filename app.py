import streamlit as st

from home import render as render_home
from subpages.product import render as render_product
from subpages.donate import render as render_donate


st.set_page_config(
    page_title="Care Connect",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ------------------------------------------------------------
# Remove default Streamlit UI / spacing
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


def get_page():
    """Read the page from the URL.

    Examples:
        ?page=home
        ?page=product
    """
    page = st.query_params.get("page", "home")

    # Extra safety in case a list-like value is returned
    if isinstance(page, list):
        page = page[0] if page else "home"

    return str(page).strip().lower()


def main():
    page = get_page()

    if page == "product":
        render_product()
    elif page == "donate":
        render_donate()
    else:
        # Home is the default page for now.
        # Later we can add:
        # elif page == "about":
        #     render_about()
        # elif page == "contact":
        #     render_contact()
        # elif page == "donate":
        #     render_donate()
        render_home()


if __name__ == "__main__":
    main()
