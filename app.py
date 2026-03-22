import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Rodolfo's Sports AI", page_icon="🏀")

st.title("🏆 AI Sports Research Tool")
st.write("Analyze teams, players, and parlays with Gemini.")

# Input for your Gemini API Key
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    user_input = st.text_input("What are we researching today?")
    
    if user_input:
        with st.spinner('Analyzing stats...'):
            response = model.generate_content(f"You are a sports betting expert. Research: {user_input}")
            st.markdown(response.text)
else:
    st.info("Please enter your Gemini API key in the sidebar to start.")
