import streamlit as st
import pickle

# Load the vectorizer
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit UI
st.title("SMS Spam Classifier")

msg = st.text_area("Enter your SMS message:")

if st.button("Predict"):
    if msg.strip() == "":
        st.warning("Please enter a message to classify.")
    else:
        # Transform input
        vector = vectorizer.transform([msg])
        # Predict
        result = model.predict(vector)[0]

        # Map numeric label to text
        if result == 1:
            st.error("🚫 This is SPAM!")
        else:
            st.success("✅ This is NOT spam.")
