from src.case import function_explainer

    
def test_function_explainer():
    fn_explainer = function_explainer.FunctionExplainerPromptTemplate(input_variables=["function_name"])    
    
    # Generate a prompt for the function "get_source_code"
    prompt = fn_explainer.format(function_name=function_explainer.get_source_code)  
    
    print(prompt)
    
    
from src.case import few_shot_prompt_template    
def test_few_shot_prompt_template():
    few_shot_prompt_template.using_example_selector()
    
    
from src.case import few_shot_examples_for_chat_models
def test_few_shot_examples_for_chat_models():
    few_shot_examples_for_chat_models.alternationHumanAndAIMessage()    
    
if __name__ == "__main__":
    test_few_shot_examples_for_chat_models()