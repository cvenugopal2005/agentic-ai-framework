import streamlit as st
from flows.summarize_flow import summarize_flow
from flows.research_flow import research_flow
import tempfile
from PyPDF2 import PdfReader

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="AI Agent Framework", page_icon="🤖")

st.markdown("""
<style>

/* ---------- REMOVE STREAMLIT DEFAULT UI ---------- */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

html, body, [class*="css"] {
    margin: 0;
    padding: 0;
}

/* Remove white top & side padding */
.block-container {
    padding-top: 0rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    padding-bottom: 2rem !important;
}

/* ---------- BACKGROUND ---------- */
.stApp {
    background: linear-gradient(135deg, #667eea, #764ba2);
    font-family: 'Segoe UI', sans-serif;
}

/* ---------- CARD ---------- */
.card {
    max-width: 800px;
    margin: 30px auto;
    background: rgba(255, 255, 255, 0.97);
    border-radius: 18px;
    padding: 30px;
    box-shadow: 0 18px 45px rgba(0,0,0,0.18);
}

/* ---------- HEADERS ---------- */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: white;
    margin-top: 10px;
}

.subtitle {
    text-align: center;
    color: #f1f1f1;
    font-size: 16px;
    margin-bottom: 25px;
}

/* ---------- CENTER BUTTON ---------- */
.center-btn {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}

/* ---------- BUTTON STYLE ---------- */
.stButton > button {
    background: linear-gradient(90deg, #667eea, #764ba2);
    color: white;
    border-radius: 12px;
    padding: 0.7em 2em;
    font-size: 17px;
    font-weight: 600;
    border: none;
    transition: 0.3s ease;
}

.stButton > button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #764ba2, #667eea);
}

/* ---------- OUTPUT ---------- */
.output-box {
    background: #f7f9fc;
    border-left: 6px solid #667eea;
    padding: 20px;
    border-radius: 12px;
    font-size: 16px;
    line-height: 1.65;
    color: #333;
    white-space: pre-wrap;
    margin-top: 20px;
}

/* ---------- FOOTER ---------- */
.footer {
    text-align: center;
    color: #eaeaea;
    font-size: 13px;
    margin-top: 35px;
}

</style>
""", unsafe_allow_html=True)



# ---------- HEADER ----------
st.markdown('<div class="title">🤖 AI Agent Framework</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Multi-Agent AI: Summarize • Research •</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

# ---------- AGENT SELECTION ----------
agent_type = st.selectbox(
    "Choose an Agent",
    ["Summarizer Agent", "Research Agent"]
)

# ---------- PDF UTILITY ----------
def extract_text_from_pdf(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file.read())
        tmp_path = tmp.name
    reader = PdfReader(tmp_path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)

# ---------- SUMMARIZER ----------
if agent_type == "Summarizer Agent":
    input_type = st.radio("Input Type", ["Text", "PDF"], horizontal=True)
    text = ""

    if input_type == "Text":
        text = st.text_area("Enter text", height=120)

    else:
        pdf = st.file_uploader("Upload PDF", type=["pdf"])
        if pdf:
            text = extract_text_from_pdf(pdf)

    # ---- Center aligned button ----
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        summarize_clicked = st.button("✨ Summarize", use_container_width=True)

    if summarize_clicked:
        if text.strip():
            with st.spinner("Summarizing..."):
                result = summarize_flow({"text": text})

            st.subheader("📌 Summary")
            st.markdown(
                f'<div class="output">{result.get("summary", "No summary generated.")}</div>',
                unsafe_allow_html=True
            )
        else:
            st.warning("Please provide input")


# ---------- RESEARCHER ----------
else:
    topic = st.text_input(
        "Enter Research Topic",
        placeholder="e.g., Artificial Intelligence in Healthcare"
    )

    # ---- Center aligned button ----
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        research_clicked = st.button("🔍 Research", use_container_width=True)

    if research_clicked:
        if topic.strip():
            with st.spinner("Researching topic..."):
                result = research_flow({"topic": topic})

            st.subheader("📚 Research Output")
            st.markdown(
                f'<div class="output">{result.get("research", "No research generated.")}</div>',
                unsafe_allow_html=True
            )
        else:
            st.warning("Please enter a topic")


st.markdown('</div>', unsafe_allow_html=True)
