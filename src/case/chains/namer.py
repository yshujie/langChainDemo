from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def giveNameForCompany():
    # 初始化 llm
    llm = OpenAI(temperature=0.9)
    
    # 设置 Prompt
    prompt = PromptTemplate(
        input_variables=['product_name'],
        template="What is a good name for a company that males {product_name}?"
    )
    
    # 初始化链
    chain = LLMChain(llm=llm, prompt=prompt)
    
    # 执行链
    return chain.run("cars")    