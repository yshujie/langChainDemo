import asyncio 
import time 

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def generate_serially():
    llm = OpenAI(temperature=0.9)
    prompt = PromptTemplate(
        input_variables=['product_name'],
        template="What is a good name for a company that makes {product_name}?"
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    
    for _ in range(3):
        resp = chain.run("cars")
        print(resp)
    
    