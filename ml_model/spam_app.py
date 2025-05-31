import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("spam_classifier_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.title("📨 Spam Message Classifier")

msg = st.text_area("Enter your message:")

if st.button("Check"):
    if msg.strip():
        vec = vectorizer.transform([msg])
        result = model.predict(vec)
        st.success("🔴 Spam" if result[0] == 1 else "🟢 Ham")
    else:
        st.warning("Please enter a message.")
