<<<<<<< HEAD
import uuid

from langchain.vectorstores import Chroma 
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, TextLoader, WebBaseLoader
from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
=======
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, TextLoader, WebBaseLoader
from langchain.embeddings import HuggingFaceEmbeddings

>>>>>>> c104dbc5914d66cd663c11322c03f17169302329

from fire import Fire

import chromadb

from chromadb.config import Settings

client = chromadb.HttpClient(settings=Settings(allow_reset=True))
# client.reset()

# Create embedding function
embedding_fn = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2",
    model_kwargs={"device": "cpu"}
 )

<<<<<<< HEAD
def load_n_split_doc(filename:str, chunk_size=1000, chunk_overlap=0):
=======

def load_n_split_doc(filename: str, chunk_size=1000, chunk_overlap=0):
>>>>>>> c104dbc5914d66cd663c11322c03f17169302329
    """Load the document and split it into chunks

    Args:
        filename (str): A filename could be pdf file, txt file or a url

    Raises:
        ValueError: Unsupported file format

    Returns:
         list : list of documents
    """
    # load the document and split it into chunks
    if filename.endswith(".pdf"):
        loader = PyPDFLoader(filename)
<<<<<<< HEAD
        
    elif filename.endswith(".txt"):
        loader = TextLoader(filename)
        

    elif filename.startswith("http"):
        loader = WebBaseLoader(filename)

    else:
        raise ValueError("Unsupported file format")
=======
    elif filename.endswith(".txt"):
        loader = TextLoader(filename)
    elif filename.startswith("http"):
        loader = WebBaseLoader(filename)
>>>>>>> c104dbc5914d66cd663c11322c03f17169302329
    
    documents = loader.load()

    # split the document into chunks
<<<<<<< HEAD
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
=======
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap
        )
>>>>>>> c104dbc5914d66cd663c11322c03f17169302329
    docs = text_splitter.split_documents(documents)
    return docs


<<<<<<< HEAD

def load_doc_to_db(documents, embedding_fn=embedding_fn, collection_name:str="my_collection", client=client):
=======
def load_doc_to_db(documents,
                   embedding_fn=embedding_fn,
                   collection_name: str = "my_collection",
                   client=client
                   ):
>>>>>>> c104dbc5914d66cd663c11322c03f17169302329
    """Load the document into the database
    
    Args:
        filename (str): A filename could be pdf file, txt file or a url
<<<<<<< HEAD
        collection_name (str, optional): [description]. Defaults to "my_collection".
=======
        collection_name (str, optional): [description]. Defaults to
        "my_collection".
>>>>>>> c104dbc5914d66cd663c11322c03f17169302329
        client ([type], optional): [description]. Defaults to client.
    
    Returns:
    """
    return Chroma.from_documents(
            documents,
<<<<<<< HEAD
            embedding_fn, 
            collection_name=collection_name, 
            client=client)

def get_db(collection_name:str="my_collection", client=client, embedding_fn=embedding_fn):
    """Get the database

    Args:
        collection_name (str, optional): [description]. Defaults to "my_collection".
=======
            embedding_fn,
            collection_name=collection_name,
            client=client
        )


def get_db(
        collection_name: str = "my_collection",
        client=client,
        embedding_fn=embedding_fn
    ):
    """Get the database

    Args:
        collection_name (str, optional): [description]. 
        Defaults to "my_collection".
>>>>>>> c104dbc5914d66cd663c11322c03f17169302329
        client ([type], optional): [description]. Defaults to client.
    
    Returns:
    """
<<<<<<< HEAD
    return Chroma(client=client, collection_name=collection_name, embedding_function=embedding_fn)


def perform_search(query:str, collection_name:str="my_collection", k:int=1):
=======
    return Chroma(
        client=client,
        collection_name=collection_name,
        embedding_function=embedding_fn
        )


def perform_search(
        query: str,
        collection_name: str = "my_collection",
        k: int = 1
        ):
>>>>>>> c104dbc5914d66cd663c11322c03f17169302329
    """Perform similarity search

    Args: 
        query (str): query string
        collection_name (str, optional): collection name. Defaults to "my_collection".
        k (int, optional): number of results. Defaults to 1.
    """
<<<<<<< HEAD
    db = Chroma(client=client, collection_name=collection_name, embedding_function=embedding_fn)
=======
    db = Chroma(
        client=client,
        collection_name=collection_name,
        embedding_function=embedding_fn
    )
>>>>>>> c104dbc5914d66cd663c11322c03f17169302329
    results = db.similarity_search(query=query, k=k)
    return results


<<<<<<< HEAD
   
=======
>>>>>>> c104dbc5914d66cd663c11322c03f17169302329
if __name__ == "__main__":
    Fire()
    