import streamlit as st
import promptinjection
import os

if 'app' not in st.session_state:
    st.session_state.app = promptinjection.build_graph()

if 'messages' not in st.session_state:
    st.session_state.messages = []

st.title("CV reviewer chatbot")

api_key = st.sidebar.text_input("Enter your GROQ API key", type="password")

if api_key:
    os.environ["GROQ_API_KEY"] = api_key
    st.sidebar.success("GROQ_API_KEY has been set.")

UPLOAD_FOLDER = "cvs"

pdf_file = st.sidebar.file_uploader("Upload a PDF CV", type=["pdf"])

if pdf_file:

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    file_path = os.path.join(UPLOAD_FOLDER, pdf_file.name)

    with open(file_path, "wb") as f:
        f.write(pdf_file.getbuffer())
    st.sidebar.success(f"CV successfully uploaded")

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter prompt here.."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    result = st.session_state.app.invoke({"prompt": prompt})
    assistant_reply = result.get("final_answer", "No response generated.")

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)
    st.session_state["messages"].append({"role": "assistant", "content": assistant_reply})
