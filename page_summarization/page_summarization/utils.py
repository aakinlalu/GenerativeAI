
from langchain import PromptTemplate
from langchain.llms import GPT4All 
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.mapreduce import MapReduceChain
from langchain.docstore.document import Document
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains.summarize import load_summarize_chain

import requests
from bs4 import BeautifulSoup


def get_text(url:str)->str:
    """
    Get the text from a web page using BeautifulSoup

    Args:
        url (str): url of the web page
    Returns:
        str: text from the web page
    
    """
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    paragraph = soup.find_all('p')
    texts = ' '.join([p.text for p in paragraph])
    return texts

def create_docs(texts:list, text_num:int=None)->list:
    """
    Create a list of documents from a list of texts

    Args:
        texts (list): list of texts
        text_num (int, optional): number of texts to use. Defaults to None.
    Returns:
        list: list of documents
    """

    # initialize the text splitter
    text_splitter = CharacterTextSplitter()
    # split the text into smaller chunks
    text_chunks = text_splitter.split_text(texts)
    # Create document  from text chunks
    if text_num is not None:
        docs = [Document(page_content=text) for text in text_chunks[:text_num]]
    else:
        docs = [Document(page_content=text) for text in text_chunks]
    return docs

def summarize(model, 
              docs:Document, 
              chain_type="map_reduce", 
              return_intermediate_steps=False, 
              prompt=None)->str:

    """
    Summarize a list of documents using a summarization chain
    Args:
        model (GPT4All): GPT4All model
        docs (Document): list of documents
        chain_type (str, optional): summarization chain type. Defaults to "map_reduce".
        return_intermediate_steps (bool, optional): return intermediate steps. Defaults to False.
        prompt (PromptTemplate, optional): prompt template. Defaults to None.

    Returns:
        str: summary
    """
    # Load the summarization chain
    chain = load_summarize_chain(model, chain_type=chain_type)

    if prompt and chain_type == "refine":
        chain =load_summarize_chain(model, chain_type=chain_type, question_prompt=prompt)
        # chain.question_prompt = prompt

    if prompt and chain_type == "stuff":
        chain =load_summarize_chain(model, chain_type=chain_type, prompt=prompt)
    # Intermediate steps example
    if return_intermediate_steps:
        chain =load_summarize_chain(model, chain_type=chain_type, return_intermediate_steps=return_intermediate_steps)
        if prompt and chain_type == "refine|stuff":
            chain =load_summarize_chain(model, chain_type=chain_type, prompt=prompt, return_intermediate_steps=return_intermediate_steps)
        return chain({"input_documents": docs}, return_only_outputs=True)
   
    return  chain.run(docs)

def load_llm(model_path:str, callbacks:list=None):
    """
    Load a GPT4All model

    Args:
        model_path (str): path to the model
        callbacks (list, optional): list of callbacks. Defaults to None.
    
    Returns:
        GPT4All: GPT4All model
    """

    callbacks = [StreamingStdOutCallbackHandler()]

    llm = GPT4All(model=model_path, 
    callbacks=callbacks
    )
    return llm


if __name__== '__main__':
    
    url = 'https://truera.com/retrieval-augmented-language-models-need-an-observability-layer/'
    
    # Load the text from a web page
    texts = get_text(url)
    # print(texts)
    docs = create_docs(texts, 1)
    # print(docs)

    # Custom promts example
    template  = """
    Write a concise summary of the following:
    {text}
    CONCISE SUMMARY
    """

    PROMPT = PromptTemplate(template=template, input_variables=["text"])
    
    # Load the model
    llm = load_llm(model_path="./page_summarization/models/ggml-model-gpt4all-falcon-q4_0.bin")

    # Load the summarization chain
    # result = summarize(llm, docs, chain_type="map_reduce")  

    # print(type(result))


    print(summarize(llm, docs, chain_type="refine", prompt=PROMPT))



   