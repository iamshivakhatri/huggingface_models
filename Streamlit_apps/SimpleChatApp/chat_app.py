import ollama
import streamlit as st

st.title("Simple Chat App")

# initialize history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Init models
if "model" not in st.session_state:
    st.session_state["model"] = ""

models = [model["name"] for model in ollama.list()["models"]]
st.session_state["model"] = st.selectbox("Select model", models)

def model_res_generator():
    stream = ollama.chat(model=st.session_state["model"], messages=st.session_state["messages"], stream=True)
    for chunk in stream:
        yield chunk["message"]["content"]


# Render chat messages from history on app
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Whats up?"):
    # Add latest message to history in format {role, content}
    st.session_state["messages"].append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # response = ollama.chat(model=st.session_state["model"], messages=st.session_state["messages"])
        # message = response["message"]["content"]
        message = st.write_stream(model_res_generator())
        # st.markdown(message)
        st.session_state["messages"].append({"role": "assistant", "content": message})
