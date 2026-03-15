from dotenv import load_dotenv
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq
from langchain.agents import create_agent

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")
search = GoogleSerperAPIWrapper()

agent = create_agent(model=model,tools=[search.run],system_prompt="You are an expert agent and search answers for any questions on Google.")

while True:
    query = input("user: ")
    if query.lower() == ["quit","bye"]:
        break
response = agent.invoke({"messages":[{"role":"user","content":query}]})
print(response["messages"][-1].content)