from src.demo import first_chat, history_searcher
    
def test_first_chat():
    first_chat.evaluateAI()    

def test_history_searcher():
    history_searcher.searchHistoryOfToday()    
    
    
if __name__ == "__main__":
    test_history_searcher()