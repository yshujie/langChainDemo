from src.demo import first_chat, history_searcher, document_summarizer
    
def test_first_chat():
    first_chat.evaluateAI()    

def test_history_searcher():
    history_searcher.searchHistoryOfToday()    

def test_document_summarizer():
    summarizeContent = document_summarizer.summarize("./src/doc/RaAct.txt")
    print(summarizeContent)
    
    
if __name__ == "__main__":
    test_document_summarizer()