from src.case.generate_name import generateName

def test_generateName():
    result = generateName()
    print("\nresult: ", result)

    # 接下来进行断言
    assert isinstance(result, str)    