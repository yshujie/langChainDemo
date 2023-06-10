from src.case.generate_name import generateName

def test_generateName():
    print("\ntest generate name: \n")
    result = generateName()
    print("\nresult: ", result)

    # 接下来进行断言
    assert isinstance(result, str)  
    
def test_generateNameWithPrompt():
    print("\ntest generate name with prompt: \n")
    result = generateName()
    print("\nresult: ", result)

    # 接下来进行断言
    assert isinstance(result, str)     