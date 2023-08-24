# LLM Summarization of Web Pages 
![document](images/summarization_use_case_2-f2a4d5d60980a79140085fb7f8043217.png)
Suppose we want to summarise content of a web page. 

We use use the [requests](http://docs.python-requests.org/en/master/) library to download the HTML content of the page.

We will use the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library to parse the HTML content of the page and extract the text.

We will leverage LLM from [GPT4All](https://gpt4all.io/index.html) to synthesise a summary of the text.


## Prerequisites
- Python 3.6 or higher
- [Poetry](https://python-poetry.org/) (optional)

## Download llm model fron GPT4All
What you need to do is to download the model from [GPT4All](https://gpt4all.io/index.html) and put it in the models folder inside the page_summarization folder.

## Install the libraries
if you are using poetry, you can install the libraries using the following command:
```bash
    cd page_summarization
```
```bash
    poetry install
```
Otherwise, you can install the libraries using the following command:
```bash
    pip install -r requirements.txt
```

## Usage/Examples
```pythhon
    from page_summarization.utils import get_text, create_docs, load_llm, summarize

    url = 'https://truera.com/retrieval-augmented-language-models-need-an-observability-layer/'
    
    # Load the text from a web page
    texts = get_text(url)
```
You can pass the number of pages  to the create_doc function to choose the number of pages in the summary. The default value is None which means all.
```python
    docs = create_docs(texts)
 
    # Load the model
    llm = load_llm(model_path="./web_summarization/models/ggml-model-gpt4all-falcon-q4_0.bin")
```

Load the summarization chain  
You can pass the chain_type parameter to the summarize function to choose the summarization chain. The default value is "map_reduce". The other option is "stuff" and "refine".

```python
    result = summarize(llm, docs, chain_type="map_reduce")  
    print(result)
```
You pass the documents into prompt and get the summary as a result.

```python

    template  = """
        Write a concise summary of the following:
        {text}
        CONCISE SUMMARY:
    """
    PROMPT = PromptTemplate(template=template, input_variables=["text"])

    result = summarize(llm, docs, chain_type="refine", prompt=PROMPT)
    print(result)
```




