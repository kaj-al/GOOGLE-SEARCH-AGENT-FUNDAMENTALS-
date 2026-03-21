# GOOGLE SEARCH AI AGENT FUNDAMENTALS

The file demonstrates all of the initial and basics of AI Agents integrated with Google search.

- An AI-powered search agent funadmentals that retrieves live search results from the web using Serper API and generates intelligent answers via a large language model.

## API key
- Using Google Serper API key. It is free of cost and manageable as well.

## Steps

### Environment variables

```python
from dotenv import load_dotenv
load_dotenv()
```
### Integrate with agent 
```python
model = ChatGroq(model="openai/gpt-oss-20b")
search = GoogleSerperAPIWrapper()
tools = search.run

if "memory" not in st.session_state:
    st.session_state.memory = InMemorySaver()
    st.session_state.history = []

agent = create_agent(model=model,tools=[tools],checkpointer=st.session_state.memory,system_prompt="You are an expert agent and search answers for any questions on Google.")
```
### chat part with ui
```python
st.header('AI SMASH')

for message in st.session_state.history:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask Anything !")
if query:
    st.chat_message("user").markdown(query)  
    st.session_state.history.append({"role":"user","content":query})
    response = agent.invoke({"messages":[{"role":"user","content":query}]},
                        {"configurable":{"thread_id":"moon"}})
    answer = response["messages"][-1].content
    st.chat_message("ai").markdown(answer)  
    st.session_state.history.append({"role":"ai","content":answer})
```

### with streaming(typing effect)
```python
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
```

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Environment Configuration

Create a `.env` file in the project root with:

```env
GROQ_API_KEY=your_api_key_here
SERPER_API_KEY=your_api_key_here
```

### 3. Getting Your API Key

- Register at [Groq](https://groq.ai)
- Register at [Serper](https://serper.dev/)
- Generate your API key
- Add it to your `.env` file

## File Structure

- `pro.py` - Main file
- `.env` - Environment variables (local only, not in git)
- `.gitignore` - Git ignore rules
- `requirements.txt` - Python dependencies
- `readme.md` - this documentation


