from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate

examples = [
    {
        "question": "Who lived longer, Muhammad Ali or Alan Turing?",
        "answer": 
        """
        Are follow up questions needed here: Yes.
        Follow up: How old was Muhammad Ali when he died?
        Intermediate answer: Muhammad Ali was 74 years old when he died.
        Follow up: How old was Alan Turing when he died?
        Intermediate answer: Alan Turing was 41 years old when he died.
        So the final answer is : Muhammad Ali.
        """
    },
    {
        "question": "When was the founder of craigslist born?",
        "answer": 
        """
        Are follow up questions needed here: Yes.
        Follow up: Who was the founder of craigslist?
        Intermediate answer: Craigslist was founded by Craig Newmark.
        Follow up: When was Craig Newmark born?
        Intermediate answer: Craig Newmark was born on December 6, 1952.
        So the final answer is : December 6, 1952.            
        """
    },
    {
        "question": "Who was the meternal grandfather of the George Washington",
        "answer": 
        """ 
        Are follow up questions needed here: Yes.
        Follow up: Who was the mother of George Washington?
        Intermediate answer: George Washington's mother was Mary Ball Washington.
        Follow up: Who was the father of Mary Ball Washington?
        Intermediate answer: Mary Ball Washington's father was Joseph Ball.
        So the final answer is : Joseph Ball.        
        """
    },
    {
        "question": "Are both the directors of Jaws and Casino Royale from the same country?",
        "answer":
        """
        Are follow up questions needed here: Yes.
        Follow up: Who is the director of Jaws?
        Intermediate answer: The director of Jaws is Steven Spielberg.
        Follow up: Where is Steven Spielberg from?
        Intermediate answer: The United States.
        Follow up: Who is the director of Casino Royale?
        Intermediate answer: The director of Casino Royale is Martin Campbell.
        Follow up: Where is Martin Campbell from?
        Intermediate answer: New Zealand.
        So the final answer is : No.
        """
    }   
]


def print_prompt(): 
    example_prompt = PromptTemplate(
        input_variables=["question", "answer"],
        template="Question: {question}\n {answer}"
    )
    
    print(example_prompt.format(**examples[0]))
    
def feed_examples_and_formatter(): 
    example_prompt = PromptTemplate(
        input_variables=["question", "answer"],
        template="Question: {question}\n {answer}"
    )
    prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        suffix="Question: {input}",
        input_variables=["input"]
    ) 
    
    print(prompt.format(input="Who was the father of Mary Ball Washington?"))
    
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings    
    
def using_example_selector():
    example_selector = SemanticSimilarityExampleSelector.from_examples(
        # This is the list of examples available to select from.
        examples,
        # This is the embedding class used to produce embeddings which are used to measure semantic similarity. 
        OpenAIEmbeddings(),
        # This is the VectorStore class that is used to store the embeddings and do a similarity search over. 
        Chroma,
        # This is the number of examples to produce
        k=1
    )
    
    # Select the most similar example to the input 
    question = "Who was the father of Mary Ball Washington?"
    selected_examples = example_selector.select_examples({"question": question})
    print(f"Examples most similar to the input: {question}")
    
    for example in selected_examples:
       print("\n")
       for k,v in example.items():
           print(f"{k}: {v}")


