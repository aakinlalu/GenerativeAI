# Generative AI
![topic](images/QA_retriever_pipeline.png)
We will cover series of generative ai tasks which include but not limited to:
- Retrieval-Augmented Generation (RAG)
- LLM Page Summarization
- Retrieval-based Chatbots
- so on...

## Tasks
<details>
<summary markdown="span"><h3>Retrieval Augmented Generation with LLM Part 1</h3></summary>

RAG is a process of fetching up to date or context specific data from an external database and making it available to to an LLM when asking it to generate a response.  

To be able to do this, we need an open source language model, a vector database and a composer. Fortunately, there are freely available open source python libraries to create this solution. For simplicity, we will use the following:

* Pre-trained T5 model from Huggingface as LLM
* ChromaDB as vector database 
* Langchain as application tools.

Click [here](Retrieval_Augmented_Generation_with_LLM.ipynb) for more.
</details>
<details>
<summary markdown="span"><h3>Retrieval Augmented Generation with LLM Part 2</h3></summary>
Instead of using a pre-trained T5 model, we will use gpt4all models.

Click [here](Retrieval_Augmented_Generation_with_LLM_part_2.ipynb) for more.
</details>
<details>
<summary markdown="span"><h3>LLM Page Summarization</h3></summary>
To summarize a page, we will use a GPT4All as LLM.    

For more, click [here](page_summarization/README.md)
</details>

## Hi, I'm Ade! 👋

## 🚀 About Me
I'm a full stack AI developer...


## Authors

- [@aakinlalu](https://www.github.com/aakinlalu)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://codestreet.ai/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adebayo-akinlalu-5451a129/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Akinlalu)


## Acknowledgements

 - [langchain](https://python.langchain.com/docs/get_started/introduction.html)
 - [GPT4ALL](https://gpt4all.io/index.html)