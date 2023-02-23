import openai
import streamlit as st

def summarize(prompt):
    augmented_prompt = f"summarize this text and end with a period: {prompt}"
    try:
        st.session_state["summary"] = openai.Completion.create(
            model="text-davinci-003",
            prompt=augmented_prompt,
            temperature=.5,
            max_tokens=110,
            stop=". ",
        )["choices"][0]["text"]
    except:
        st.write('There was an error =(')