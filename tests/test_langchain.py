from src.case.generate_name import generateName, genNameWithPrompt, genNameWithChain

def test_generateName():
    print("\ntest generate name: \n")
    result = generateName()
    print("\nresult: ", result)

    # 接下来进行断言
    assert isinstance(result, str)  
    
def test_generateNameWithPrompt():
    print("\ntest generate name with prompt: \n")
    result = genNameWithPrompt()
    print("\nresult: ", result)

    # 接下来进行断言
    assert isinstance(result, str)     
    
def testGenerateNameWithChain():
    print("\ntest generate name with chain: \n")
    result = genNameWithChain()
    print("\nresult: ", result)

    # 接下来进行断言
    assert isinstance(result, str)    