"""
A simple Streamlit chat UI for testing the researcher agent with Pinecone and OpenAI.
"""
import streamlit as st
from vectordb import query_agent

st.title("Electronic supply store Agent Chat UI")

if "history" not in st.session_state:
    st.session_state["history"] = []

user_input = st.text_input("Ask a question:")

if st.button("Send") and user_input:
    # Query the agent (Pinecone + OpenAI)
    st.session_state["history"].append(("user", user_input))
    # Capture output
    import io
    import sys
    buffer = io.StringIO()
    sys.stdout = buffer
    query_agent(user_input, "electronicsupplyv2")
    sys.stdout = sys.__stdout__
    agent_response = buffer.getvalue()
    st.session_state["history"].append(("agent", agent_response))

# Display chat history
for role, msg in st.session_state["history"]:
    if role == "user":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**Agent:** {msg}")
