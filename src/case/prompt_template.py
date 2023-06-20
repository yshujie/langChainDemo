
def case1():
    template = """/ 
    You are a naming consultant for new companies.
    What is a good name for a company that makes {product}?
    """
    
    prompt = PromptTemplate.from_template(template)
    prompt.format(product="colorful socks")
    
    