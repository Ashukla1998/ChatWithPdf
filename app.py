# app.py

import streamlit as st 
from qa_engine import extract_text_from_pdf, process_pdf, get_answer

st.set_page_config(page_title="PDF QA Chatbot", layout="centered")
st.title("📄 PDF QA Chatbot (Local & Free)")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with st.spinner("Processing PDF..."):
        text = extract_text_from_pdf(uploaded_file)
        process_pdf(text)
    st.success("PDF processed successfully!")

    question = st.text_input("Ask a question about the PDF:")
    if question:
        with st.spinner("Generating answer..."):
            answer = get_answer(question)
        st.markdown("### ✅ Answer")
        st.write(answer)
