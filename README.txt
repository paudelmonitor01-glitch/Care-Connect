CARE CONNECT - STREAMLIT VERSION

Files:
- app.py         -> Streamlit launcher / wrapper
- index.html     -> your frontend HTML
- style.css      -> your frontend CSS
- requirements.txt
- RUN_APP.bat    -> double-click launcher for Windows

FIRST TIME ONLY:
1. Open Command Prompt in this folder.
2. Run:
       pip install -r requirements.txt

TO START THE APP:
Option A:
       streamlit run app.py

Option B on Windows:
       Double-click RUN_APP.bat

EDITING THE FRONTEND:
- Change index.html for structure/text.
- Change style.css for appearance.
- app.py reads those files every Streamlit rerun.
- When Streamlit's file watcher notices saved changes, the page will normally rerun automatically.

IMPORTANT:
This version preserves the HTML/CSS design inside Streamlit. HTML anchor links such as Home/About/Donate scroll normally. Raw HTML buttons are visual HTML controls; connect them to Streamlit/Python logic later if you want donation forms, database saving, login, admin panels, etc.
