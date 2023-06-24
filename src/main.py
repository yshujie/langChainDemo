from src.case import function_explainer

    
def test_function_explainer():
    fn_explainer = function_explainer.FunctionExplainerPromptTemplate(input_variables=["function_name"])    
    
    # Generate a prompt for the function "get_source_code"
    prompt = fn_explainer.format(function_name=function_explainer.get_source_code)  
    
    print(prompt)
    
if __name__ == "__main__":
    test_function_explainer()