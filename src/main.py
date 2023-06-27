from src.demo import first_chat, history_searcher, document_summarizer, qa_bot, youtube_bot, local_cuisine_recipe_searcher
    
def test_first_chat():
    first_chat.evaluateAI()    

def test_history_searcher():
    history_searcher.searchHistoryOfToday()    

def test_document_summarizer():
    summarizeContent = document_summarizer.summarize("./src/doc/RaAct.txt")
    print(summarizeContent)

def test_qa_bot():
    print(qa_bot.question("方寸的价值观是什么？简述一下"))
 
def test_youtube_bot():
    youtube_bot.chat()    
    

def test_local_cuisine_recipe_searcher():
    local_cuisine_recipe_searcher.start("北京")
    
if __name__ == "__main__":
    test_local_cuisine_recipe_searcher()