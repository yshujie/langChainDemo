from langchain import PromptTemplate


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