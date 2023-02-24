import openai
import streamlit as st

def summarize(prompt):
    augmented_prompt = f"Summarize the following text in only one single sentence: {prompt}"
    try:
        st.session_state["summary"] = openai.Completion.create(
            model="text-davinci-003",
            prompt=augmented_prompt,
            temperature=.5,
            max_tokens=500,
        )["choices"][0]["text"]
    except:
        st.write('There was an error =(')
