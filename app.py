import os
import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Rodolfo's Sports AI", page_icon="🏀", layout="centered")

st.title("🏆 AI Sports Research Tool")
st.caption("Analyze team matchups, player props, and parlay legs using Gemini.")

# Check Streamlit secrets or environment variables first
default_api_key = st.secrets.get("GEMINI_API_KEY", "") if "GEMINI_API_KEY" in st.secrets else os.getenv("GEMINI_API_KEY", "")

# Sidebar API Key Input (pre-filled if secret/env var exists)
api_key = st.sidebar.text_input("Gemini API Key", value=default_api_key, type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    # Configure model with system instructions
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=(
            "You are an expert sports analyst and odds handicapper. "
            "Provide concise, data-driven analysis focusing on recent team/player trends, "
            "matchup advantages, relevant injuries, and tactical factors. "
            "Structure your output with clear headers and bullet points."
        )
    )
    
    user_input = st.text_input("What are we researching today?", placeholder="e.g., Breakdown for Knicks vs. Celtics or player props")
    
    if user_input:
        with st.spinner('Analyzing stats and matchups...'):
            try:
                response = model.generate_content(user_input)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
else:
    st.info("Please enter your Gemini API key in the sidebar to start.")
