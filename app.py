import streamlit as st
import librosa
import matplotlib.pyplot as plt
import numpy as np
from google import genai
from google.genai import types
import io

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="PulsePrint AI", layout="wide", page_icon="🫀")

# Custom CSS to give it a "Medical Dashboard" feel
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border-radius: 10px; padding: 15px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. HELPER FUNCTIONS ---
@st.cache_data
def load_and_plot_audio(file_bytes):
    """Loads audio and generates a clean waveform plot."""
    y, sr = librosa.load(io.BytesIO(file_bytes))
    duration = len(y) / sr
    time = np.linspace(0, duration, len(y))
    
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(time, y, color='#ff4b4b', linewidth=0.5)
    ax.set_facecolor('#0e1117')
    ax.set_xlabel("Time (s)", color='white')
    ax.set_ylabel("Amplitude", color='white')
    ax.grid(alpha=0.2)
    fig.patch.set_facecolor('#0e1117')
    return fig, y, sr

# --- 3. SIDEBAR (Settings) ---
with st.sidebar:
    st.title("⚙️ Settings")
    api_key = st.text_input("AIzaSyDKqMnaBBiS5NwC6yNTQPD90C2N69BlHEM", type="password")
    model_choice = st.selectbox("Reasoning Engine", ["gemini-2.5-flash", "gemini-3-pro-preview"])
    st.info("The Pro model provides deeper clinical correlation.")

# --- 4. MAIN INTERFACE ---
st.title("🫀 PulsePrint: Biomedical Sound Analysis")
st.write("Extract the 'Biomedical Sound Print' from raw heart recordings.")

uploaded_file = st.file_uploader("Upload Heart Sound (.wav)", type=["wav"])

if uploaded_file and api_key:
    client = genai.Client(api_key=api_key)
    file_bytes = uploaded_file.read()

    # --- TOP METRICS ---
    col1, col2, col3 = st.columns(3)
    # Note: These values would ideally be parsed from the AI JSON response
    col1.metric("Signal Status", "Received", "Clean")
    col2.metric("Analysis Mode", "Clinical", "Active")
    #col3.metric("BPM Est.", "--", "Calculating")

    # --- WAVEFORM & AUDIO PLAYER ---
    st.subheader("Phonocardiogram (PCG) Visualization")
    fig, y, sr = load_and_plot_audio(file_bytes)
    st.pyplot(fig)
    st.audio(file_bytes, format="audio/wav")

    # --- AI REASONING SECTION ---
    st.markdown("---")
    if st.button("Generate Diagnostic Print"):
        with st.spinner("AI is analyzing the rhythm and valves..."):
            try:
                # Re-upload for API processing
                uploaded_file.seek(0)
                ai_file = client.files.upload(
                    file=uploaded_file,
                    config=types.UploadFileConfig(mime_type="audio/wav")
                )
                
                prompt = """
                You are a cardiologist. Analyze this recording:
                1. Identify S1 (Lub) and S2 (Dub) timestamps.
                2. Evaluate the rhythm regularity (Check for AFib patterns).
                3. Note any murmurs or background noise artifacts.
                Return a structured clinical summary.
                """
                
                response = client.models.generate_content(
                    model=model_choice,
                    contents=[prompt, ai_file]
                )
                
                left_co, right_co = st.columns([2, 1])
                with left_co:
                    st.subheader("📋 Clinical Reasoning")
                    st.markdown(response.text)
                with right_co:
                    st.subheader("🔍 AI Observations")
                    st.success("Analysis Complete")
                    st.warning("Note: This is an AI aid, not a final medical diagnosis.")
            
            except Exception as e:
                st.error(f"Error: {e}")

elif not api_key:
    st.warning("Please enter your API Key in the sidebar to begin.")
