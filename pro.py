from dotenv import load_dotenv
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
import streamlit as st

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b",streaming=True)
search = GoogleSerperAPIWrapper()
tools = search.run

if "memory" not in st.session_state:
    st.session_state.memory = InMemorySaver()
    st.session_state.history = []

agent = create_agent(model=model,tools=[tools],checkpointer=st.session_state.memory,system_prompt="You are an expert agent and search answers for any questions on Google.")

st.header('AI SMASH')

for message in st.session_state.history:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask Anything !")
if query:
    st.chat_message("user").markdown(query)  
    st.session_state.history.append({"role":"user","content":query})
    response = agent.stream({"messages":[{"role":"user","content":query}]},
                        {"configurable":{"thread_id":"moon"}},
                        stream_mode="messages")
    ai = st.chat_message("ai")
    with ai:
        space = st.empty()
        msg = ""
        for chunk in response:
            msg = msg + chunk[0].content 
            space.write(msg)
        st.session_state.history.append({"role":"ai","content":msg})
