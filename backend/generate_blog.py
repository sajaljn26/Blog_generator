from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.schema.runnable import RunnableLambda
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_blog(topic):
    """Generates a full blog post based on a given topic using an LLM."""

    template = """Write a detailed blog post on the topic "{topic}".
    - Include an engaging introduction
    - Provide 3 key points with explanations
    - Use SEO-friendly keywords
    - End with a conclusion and call to action

    Return the blog in structured markdown format.
    """

    prompt = PromptTemplate(input_variables=["topic"], template=template)
    llm = ChatGroq(model="gemma2-9b-it", api_key=GROQ_API_KEY)

    # Updated for LangChain 0.1.17+
    chain = prompt | llm | RunnableLambda(lambda x: x.content)
    
    return chain.invoke({"topic": topic})