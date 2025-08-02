import streamlit as st
import time

from model import generate_response

st.set_page_config(
    page_title = "chat bot",
    page_icon = "💬",
    layout = "centered"
)

st.title("Chat bot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask anything!")

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.chat_history.append({"role":"user", "content":user_input})
    
    response = generate_response(user_input)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_reply = ""
        for char in response:
            full_reply += char
            message_placeholder.markdown(full_reply)
            time.sleep(0.001) 
        message_placeholder.markdown(full_reply)

    st.session_state.chat_history.append({"role":"assistant", "content":response})