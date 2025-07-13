import streamlit as st
from inference import generate_response

st.set_page_config(page_title="Customer Support Chatbot", page_icon="🤖")

st.title("💬 Customer Support Chatbot")
st.write("Ask anything related to our service!")

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("You:", key="input")

if user_input:
    response = generate_response(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

# Display chat history
for speaker, msg in st.session_state.history:
    if speaker == "You":
        st.markdown(f"**🧑 {speaker}:** {msg}")
    else:
        st.markdown(f"**🤖 {speaker}:** {msg}")