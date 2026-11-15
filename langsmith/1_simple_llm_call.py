from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
import os

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY is not set")

# Simple one-line prompt
prompt = PromptTemplate.from_template("{question}")

model = ChatOpenAI(
    model="openrouter/free",
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    temperature=0.2,
    max_tokens=4000,
    streaming=True,
)
parser = StrOutputParser()

# Chain: prompt → model → parser It uses the LCEL LangChain Expression Language pipe operator (|) to connect different steps of an AI pipeline together like an assembly line.
chain = prompt | model | parser

# Run it
result = chain.invoke({"question": "What is the capital of pakistan?"})
print(result)
