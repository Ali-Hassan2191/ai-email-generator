# %%writefile app.py

import streamlit as st
from groq import Groq



# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Email Generator",
    page_icon="✉️",
    layout="wide"
)


# ============================================================
# GROQ API
# ============================================================

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=GROQ_API_KEY)



# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       MAIN APP
       ======================================================== */

    .stApp {
        background: linear-gradient(
            135deg,
            #f5f7ff 0%,
            #eef6ff 35%,
            #fff8fb 100%
        );
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }


    /* ========================================================
       HEADER
       ======================================================== */

    .header-shell {
        padding: 1.4rem 1.5rem 1rem 1.5rem;
        border-radius: 24px;
        background: rgba(255, 255, 255, 0.72);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(148, 163, 184, 0.2);
        box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08);
        margin-bottom: 1.5rem;
    }

    .mini-badge {
        display: inline-block;
        font-size: 11px;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        font-weight: 700;
        color: #5b5bd6;
        background: rgba(91, 91, 214, 0.08);
        border: 1px solid rgba(91, 91, 214, 0.15);
        border-radius: 999px;
        padding: 0.35rem 0.7rem;
        margin-bottom: 0.75rem;
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 8px;
        color: #111827;
        letter-spacing: -0.04em;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #475569;
        margin-bottom: 0.2rem;
        line-height: 1.6;
    }


    /* ========================================================
       SECTION TITLES
       ======================================================== */

    .section-title {
        font-size: 24px;
        font-weight: 700;
        margin-top: 10px;
        margin-bottom: 14px;
        color: #0f172a !important;
    }


    /* ========================================================
       MAIN AREA LABELS
       ======================================================== */

    /* All labels in main Email Information area */
    .main .stTextInput label,
    .main .stTextArea label,
    .main .stSelectbox label,
    .main .stTextInput p,
    .main .stTextArea p,
    .main .stSelectbox p,
    .stMainContainer label,
    .stMainContainer p {
        color: #000000 !important;
    }


    /* ========================================================
       MAIN INPUT FIELDS
       ======================================================== */

    .main .stTextInput input,
    .main .stTextArea textarea,
    .stMainContainer .stTextInput input,
    .stMainContainer .stTextArea textarea,
    .stMainContainer [data-baseweb="select"] > div,
    .stMainContainer .stSelectbox [data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid rgba(148, 163, 184, 0.4) !important;
        border-radius: 14px !important;
        box-shadow: 0 8px 18px rgba(15, 23, 42, 0.04);
    }

    .main .stTextInput input::placeholder,
    .main .stTextArea textarea::placeholder,
    .stMainContainer .stTextInput input::placeholder,
    .stMainContainer .stTextArea textarea::placeholder {
        color: #64748b !important;
        opacity: 1;
    }

    .main .stTextInput input:focus,
    .main .stTextArea textarea:focus,
    .stMainContainer .stTextInput input:focus,
    .stMainContainer .stTextArea textarea:focus {
        border-color: rgba(99, 102, 241, 0.8) !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.14) !important;
    }


    /* ========================================================
       MAIN SELECTBOX
       ======================================================== */

    .main .stSelectbox label {
        color: #000000 !important;
    }

    .main .stSelectbox [data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 14px !important;
        border: 1px solid rgba(148, 163, 184, 0.4) !important;
    }


    /* ========================================================
       SIDEBAR
       ======================================================== */

    [data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #0f172a 0%,
            #111827 100%
        );
    }

    [data-testid="stSidebar"] .stMarkdown,
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        color: #ffffff !important;
    }


    /* ========================================================
       SIDEBAR SELECTBOX
       ======================================================== */

    [data-testid="stSidebar"] .stSelectbox label {
        color: #ffffff !important;
    }

    [data-testid="stSidebar"]
    .stSelectbox
    [data-baseweb="select"] {
        background-color: #ffffff !important;
        border-radius: 12px !important;
    }

    [data-testid="stSidebar"]
    .stSelectbox
    [data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 12px !important;
    }


    /* ========================================================
       SIDEBAR SELECTBOX TEXT
       ======================================================== */

    [data-testid="stSidebar"]
    [data-baseweb="select"] span {
        color: #000000 !important;
    }

    [data-testid="stSidebar"]
    [data-baseweb="select"] input {
        color: #000000 !important;
    }


    /* ========================================================
       SIDEBAR DROPDOWN ARROW
       Dark sidebar + white arrow when open.
       Black arrow when sidebar is hidden.
       ======================================================== */

    [data-testid="stSidebar"] [data-baseweb="select"] svg,
    [data-testid="stSidebar"] [data-baseweb="select"] path,
    [data-testid="stSidebar"] [data-baseweb="select"] polyline,
    [data-testid="stSidebar"] [data-baseweb="select"] line,
    [data-testid="stSidebar"] [data-baseweb="select"] circle {
        fill: #ffffff !important;
        stroke: #ffffff !important;
        color: #ffffff !important;
    }


    /* ========================================================
       SIDEBAR DROPDOWN MENU
       ======================================================== */

    [data-baseweb="popover"] {
        background-color: #ffffff !important;
    }

    [data-baseweb="popover"] [role="option"] {
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    [data-baseweb="popover"] [role="option"]:hover {
        background-color: #f1f5f9 !important;
        color: #000000 !important;
    }


    /* ========================================================
       SIDEBAR INFO / TIP BOX
       ======================================================== */

    [data-testid="stSidebar"] .stAlert {
        background: #ffffff !important;
        border: 1px solid rgba(15, 23, 42, 0.12) !important;
        border-radius: 12px !important;
        color: #000000 !important;
    }

    [data-testid="stSidebar"] .stAlert p,
    [data-testid="stSidebar"] .stAlert div,
    [data-testid="stSidebar"] .stAlert span,
    [data-testid="stSidebar"] .stAlert strong {
        color: #000000 !important;
    }


    /* ========================================================
       SIDEBAR DIVIDER
       ======================================================== */

    [data-testid="stSidebar"] hr {
        border-color: rgba(255, 255, 255, 0.2) !important;
    }


    /* ========================================================
       BUTTON
       ======================================================== */

    .stButton > button {
        width: 100%;
        border: none;
        border-radius: 14px;
        font-weight: 700;
        height: 48px;
        background: linear-gradient(
            135deg,
            #4f46e5 0%,
            #7c3aed 100%
        );
        color: white !important;
        box-shadow: 0 12px 24px rgba(79, 70, 229, 0.22);
        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 15px 28px rgba(79, 70, 229, 0.3);
    }


    /* ========================================================
       DOWNLOAD BUTTON
       ======================================================== */

    .stDownloadButton > button {
        border-radius: 14px;
        font-weight: 700;
        border: 1px solid rgba(99, 102, 241, 0.2);
        background: white;
        color: #1f2937 !important;
    }


    /* ========================================================
       ALERTS
       ======================================================== */

    .stAlert {
        border-radius: 14px;
        background: rgba(255, 255, 255, 0.8);
        border: 1px solid rgba(148, 163, 184, 0.25);
    }


    /* ========================================================
       TEXT AREA
       ======================================================== */

    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    .stTextArea textarea::placeholder {
        color: #64748b !important;
    }


    /* ========================================================
       SIDEBAR COLLAPSE BUTTON
       Open state = white arrow
       Closed state = black arrow
       ======================================================== */

    button[aria-label*="Close sidebar"],
    button[aria-label*="Collapse sidebar"],
    button[aria-label*="Close side bar"],
    button[aria-label*="Collapse side bar"] {
        color: #ffffff !important;
        background: transparent !important;
        border: none !important;
    }

    button[aria-label*="Close sidebar"] svg,
    button[aria-label*="Collapse sidebar"] svg,
    button[aria-label*="Close side bar"] svg,
    button[aria-label*="Collapse side bar"] svg,
    button[aria-label*="Close sidebar"] path,
    button[aria-label*="Collapse sidebar"] path,
    button[aria-label*="Close side bar"] path,
    button[aria-label*="Collapse side bar"] path {
        fill: #ffffff !important;
        stroke: #ffffff !important;
        color: #ffffff !important;
    }

    button[aria-label*="Open sidebar"],
    button[aria-label*="Open side bar"] {
        color: #000000 !important;
        background: transparent !important;
        border: none !important;
    }

    button[aria-label*="Open sidebar"] svg,
    button[aria-label*="Open side bar"] svg,
    button[aria-label*="Open sidebar"] path,
    button[aria-label*="Open side bar"] path {
        fill: #000000 !important;
        stroke: #000000 !important;
        color: #000000 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)




# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="header-shell">'
    '<div class="main-title">✉️ AI Email Generator</div>'
    '<div class="subtitle">Create professional, natural and personalized emails in seconds.</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ Email Settings")

    email_type = st.selectbox(
        "Email Type",
        [
            "Professional",
            "Follow-up",
            "Job Application",
            "Cold Email",
            "Meeting Request",
            "Thank You",
            "Apology",
            "Complaint",
            "Sales",
            "Request",
            "General"
        ]
    )

    tone = st.selectbox(
        "Tone",
        [
            "Professional",
            "Friendly",
            "Formal",
            "Casual",
            "Persuasive",
            "Polite",
            "Confident"
        ]
    )

    length = st.selectbox(
        "Email Length",
        [
            "Short",
            "Medium",
            "Detailed"
        ]
    )

    language = st.selectbox(
        "Language",
        [
            "English",
            "Urdu",
            "Roman Urdu"
        ]
    )

    st.divider()

    st.info(
        "💡 Tip: Give the AI enough information about "
        "your purpose and important points for better results."
    )


# ============================================================
# INPUT SECTION
# ============================================================

st.markdown(
    '<div class="section-title">📝 Email Information</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:

    recipient = st.text_input(
        "Recipient",
        placeholder="e.g. Client, Manager, Professor"
    )

    sender_name = st.text_input(
        "Your Name",
        placeholder="e.g. Ali Hassan"
    )

    subject_hint = st.text_input(
        "Subject / Main Topic",
        placeholder="e.g. Follow-up regarding my proposal"
    )


with col2:

    purpose = st.text_area(
        "Purpose",
        placeholder=(
            "Explain what you want to communicate..."
        ),
        height=120
    )

    key_points = st.text_area(
        "Key Points",
        placeholder=(
            "Write the important information "
            "you want to include..."
        ),
        height=120
    )


# ============================================================
# GENERATE EMAIL FUNCTION
# ============================================================

def generate_email(
    email_type,
    recipient,
    sender_name,
    subject_hint,
    purpose,
    key_points,
    tone,
    length,
    language
):

    prompt = f"""
You are an expert professional email writer.

Your task is to write a high-quality, natural and
human-sounding email.

==================================================
EMAIL INFORMATION
==================================================

Email Type:
{email_type}

Recipient:
{recipient}

Sender Name:
{sender_name}

Subject / Main Topic:
{subject_hint}

Purpose:
{purpose}

Important Points:
{key_points}

Tone:
{tone}

Length:
{length}

Language:
{language}

==================================================
INSTRUCTIONS
==================================================

1. Write a clear and natural email.
2. Make the email sound like it was written by a real person.
3. Follow the requested tone.
4. Do not use unnecessary complicated vocabulary.
5. Keep the email appropriate for the recipient.
6. Include a suitable subject line.
7. Include a proper greeting.
8. Include a clear email body.
9. Include a suitable closing.
10. Use the sender's name when provided.
11. Do not invent facts that were not provided.
12. Do not explain your reasoning.
13. Do not mention that AI generated the email.
14. Return ONLY the final email.

==================================================
OUTPUT FORMAT
==================================================

Subject: [subject]

[Greeting]

[Email body]

[Closing]
[Sender Name]
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional email writing "
                    "assistant who creates natural, "
                    "clear and effective emails."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=1200
    )

    return response.choices[0].message.content


# ============================================================
# GENERATE BUTTON
# ============================================================

st.divider()

generate_button = st.button(
    "✨ Generate Email",
    type="primary",
    use_container_width=True
)


# ============================================================
# GENERATION
# ============================================================

if generate_button:

    if not recipient:
        st.warning("Please enter the recipient.")

    elif not purpose:
        st.warning("Please describe the purpose of the email.")

    else:

        with st.spinner("✨ Writing your email..."):

            try:

                generated_email = generate_email(
                    email_type=email_type,
                    recipient=recipient,
                    sender_name=sender_name,
                    subject_hint=subject_hint,
                    purpose=purpose,
                    key_points=key_points,
                    tone=tone,
                    length=length,
                    language=language
                )

                st.session_state["generated_email"] = generated_email

            except Exception as e:

                st.error(
                    "Something went wrong while generating "
                    "the email."
                )

                st.exception(e)


# ============================================================
# OUTPUT SECTION
# ============================================================

if "generated_email" in st.session_state:

    st.divider()

    st.markdown(
        '<div class="section-title">📨 Generated Email</div>',
        unsafe_allow_html=True
    )

    generated_email = st.text_area(
        "Your Email",
        value=st.session_state["generated_email"],
        height=400
    )

    # Update session state if user edits email
    st.session_state["generated_email"] = generated_email

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            label="📥 Download Email",
            data=generated_email,
            file_name="generated_email.txt",
            mime="text/plain",
            use_container_width=True
        )

    with col2:

        if st.button(
            "🔄 Generate Again",
            use_container_width=True
        ):

            with st.spinner("Generating another version..."):

                try:

                    new_email = generate_email(
                        email_type=email_type,
                        recipient=recipient,
                        sender_name=sender_name,
                        subject_hint=subject_hint,
                        purpose=purpose,
                        key_points=key_points,
                        tone=tone,
                        length=length,
                        language=language
                    )

                    st.session_state["generated_email"] = new_email

                    st.rerun()

                except Exception as e:

                    st.error(
                        "Could not generate another email."
                    )

                    st.exception(e)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "✉️ AI Email Generator • Powered by Groq"
)
