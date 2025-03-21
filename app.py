import streamlit as st
import requests

st.title("AI Powered Blog Writer")

topic = st.text_input("Enter the topic you want to generate a blog about:")

if st.button("Generate Blog"):
    with st.spinner("Generating blog..."):
        response = requests.post("http://127.0.0.1:5007/generate_blog", json={"topic": topic})
        if response.status_code == 200:
            result = response.json()
            st.subheader(result["message"])
            st.markdown(result["blog"])
        else:
            st.subheader("Error")
            