from langchain.llms import OpenAI

def generateName():
    llm = OpenAI(temperature=0.9)
    text = "We would be a good company name for a company that make colorful socks."
    
    return llm(text)