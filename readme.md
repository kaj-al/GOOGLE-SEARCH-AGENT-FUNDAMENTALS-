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
agent = create_agent(model=model,tools=[search.run],system_prompt="You are an expert agent and search answers for any questions on Google.")
while True:
    query = input("user: ")
    if query.lower() == ["quit","bye"]:
        break
reply = agent.invoke({"messages":[{"role":"user","content":query}]})
reply["messages"][-1].content
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


