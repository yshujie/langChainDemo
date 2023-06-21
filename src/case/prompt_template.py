from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.schema import (
    AIMessage,  
    HumanMessage,
    SystemMessage
)

def case1() -> str:
    template = """/ 
    You are a naming consultant for new companies.
    What is a good name for a company that makes {product}?
    """
    
    prompt = PromptTemplate.from_template(template)
    return prompt.format(product="colorful socks")
    
def case2() -> str:
    # An example  prompt with no input variable
    # 一个没有输入变量的示例提示
    no_input_prompt = PromptTemplate(
        input_variables=[],
        template="Tell me a joke."
    )
    
    return no_input_prompt.format()

def case3() -> str:
    # An example prompt with one input variable
    one_input_prompt = PromptTemplate(
        input_variables=["adjectives"],
        template="Tell me a {adjectives} joke."
    )
    return one_input_prompt.format(adjectives="funny")

def case4() -> str:
    # An example prompt with multiple input variables
    multiple_input_prompt = PromptTemplate(
        input_variables=["adjective", "content"],
        template="Tell me a {adjective} joke about {content}."
    )
    return multiple_input_prompt.format(adjective="funny", content="a dog")

def case5() -> str:
    # use form_template to create a prompt
    template = "Tell me a {adjective} joke about {content}."
    
    prompt_template = PromptTemplate.from_template(template)
    prompt_template.input_variables
    
    return prompt_template.format(adjective="funny", content="a dog")

def case6() -> list:
    # use MessagePrompt to create a prompt
    
    template = "You are a helpful assistant that translates {input_language} to {output_language}."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    
    human_template="{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    return chat_prompt.format_prompt(input_language="English", output_language="Chinese", text="I love programming.").to_messages()
