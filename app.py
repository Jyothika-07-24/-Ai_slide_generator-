import streamlit as st
import openai

# Set your OpenAI API key (securely, e.g., via environment variables)
openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_slides(text):
    prompt = f"Generate a slide deck outline from this text: {text}. Format as: Slide 1: Title\n- Bullet\nSlide 2: etc."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response.choices[0].message.content

st.title("AI Slide Generator from Text")
user_text = st.text_area("Paste your text here:")
if st.button("Generate Slides"):
    if user_text:
        slides = generate_slides(user_text)
        st.markdown(slides)
        st.download_button("Download as Markdown", slides, file_name="slides.md")
    else:
        st.error("Please enter text.")
