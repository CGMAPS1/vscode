import streamlit as st
import requests

st.title("🧠 Heavy ML Sentiment Classifier")
st.markdown("Using **FastAPI + Streamlit**")

input_text = st.text_area("Enter your text here:")

if st.button("Predict Sentiment"):
    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Sending to model server..."):
            response = requests.post(
                " https://render.com/docs/web-services#port-binding",  # e.g. render or EC2 URL
                json={"text": input_text}
            )
            if response.status_code == 200:
                result = response.json()
                st.success(f"Sentiment: {result['label']} (Confidence: {result['score']:.2f})")
            else:
                st.error("Failed to get prediction.")
