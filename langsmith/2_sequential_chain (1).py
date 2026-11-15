from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
import os
os.environ['LANGCHAIN_PROJECT'] = 'Sequential LLM App'

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY is not set")

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model = ChatOpenAI(
    model="openrouter/free",
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    temperature=0.2,
    max_tokens=4000,
    streaming=True,
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

config = {
'run_name':'Sequential model',
'tags': ['llm app', 'report generation', 'summarization'],
'metadata': {'model1': 'gpt-4o-mini', 'model1_temp':0.7, 'parser': 'stroutputparser'}
}

result = chain.invoke({'topic': 'Employment in pakistan'},config=config)

print(result)
