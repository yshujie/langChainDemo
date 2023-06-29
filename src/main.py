from src.case.chains import (
    loading_from_langChainHub,
    router,
    film_critic
)

def testLoadFromLangChainHub():
    loading_from_langChainHub.calc()    

def testRouter():
    router.route()

def testFilmCritic():
    film_critic.review()
    
if __name__ == "__main__":
    testFilmCritic()