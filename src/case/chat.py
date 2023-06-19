from langchain import OpenAI, ConversationChain

def chat():
    llm = OpenAI(temperature=0)
    conversation = ConversationChain(llm=llm, verbose=True)
    
    conversation.run("I'm doing well! Just having a conversation with AI.")
    