from src.case.chains import (
    loading_from_langChainHub,
    router
)

def testLoadFromLangChainHub():
    loading_from_langChainHub.calc()    

def testRouter():
    router.route()
    
if __name__ == "__main__":
    testRouter()