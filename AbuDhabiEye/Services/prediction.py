from .llm_service import LLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

def prediction(query):
    llm_instance = LLM(token_limit=3,model="gpt-4o-mini")
    llm = llm_instance.get_llm()
    
    template = """
        You are a assistant how help predict the intent of the user query. 
        
        So the user query will have two kinds of intents 
        1. LLM - which will be normal queries a llm can answer without knowledgebase
        2. DB - where the data is been searched on database and the response is given
        
        The user queries will be mostly on Abu Dhabi Tourism and currently we have these databases
        
        1. cultural events or normal events
        2. travelling groups
        3. tourism places in abu dhabi
        4. car rentals in abu dhabi
        
        Your response should be either just the Intent nothing else like explaination or anything. Just LLM or DB 
        
        Here is the User Query: {Query}   
    """
    
    output_parser = StrOutputParser()
    
    prompt = ChatPromptTemplate.from_template(template)
    
    chain = prompt | llm | output_parser
    
    return chain.invoke({"Query": query})
    
    
    