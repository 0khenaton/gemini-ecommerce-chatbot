import streamlit as st
from chatbot import ask_bot

st.set_page_config(page_title="E-Ticaret Destek Chatbot", page_icon="🛒")
st.title("🛒 E-Ticaret Destek Chatbot (Gemini RAG)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if query := st.chat_input("Sipariş, iade veya teslimatla ilgili sorunuzu yazın:"):
    
    st.session_state.messages.append({"role": "user", "content": query})
    
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        with st.spinner("Cevap hazırlanıyor..."):
            response = ask_bot(query)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})