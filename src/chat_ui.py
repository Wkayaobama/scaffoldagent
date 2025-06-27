"""
A simple Streamlit chat UI for testing the researcher agent with Pinecone and OpenAI.
"""
import streamlit as st
from orchestrator.triage import AgentOrchestrator


st.set_page_config(page_title="Electronics Q&A Chatbot", page_icon="🤖")
st.title("Electronics Q&A Chatbot")

# Initialize orchestrator and agent only once
if "orchestrator" not in st.session_state:
    st.session_state.orchestrator = AgentOrchestrator()
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input at the bottom
if user_input := st.chat_input("Ask a question about electronics..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Get agent response directly from orchestrator
    agent_response = st.session_state.orchestrator.answer_query(user_input)
    st.session_state.messages.append({"role": "assistant", "content": agent_response})
    # st.experimental_rerun()  # No need to rerun since session state handles updates
