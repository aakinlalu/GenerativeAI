from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All, Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from ctransformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM, Config


def get_mistral():
    conf = AutoConfig(Config(temperature=0.8, repetition_penalty=1.2, max_new_tokens=1024, context_length=2048))

    llm = AutoModelForCausalLM.from_pretrained(
        "models/mistral-7b-instruct-v0.1.Q4_K_M.gguf", 
        model_type="mistral", 
        config=conf
    )
    return llm


def get_gpt4all(model_pth, backend='gptj'): 
    callbacks = [StreamingStdOutCallbackHandler()]
    # callbacks = [StreamingStdOutCallbackHandler()]

    llm = GPT4All(model=model_pth, backend=backend)
    return llm

def get_ollama(model_name='llama2'):
    # callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
    return Ollama(model=model_name)


def create_prompt(template:str, context:str):
    return PromptTemplate(template=template, input_variables=['question', 'context']).partial(context=context)


def get_answer(llm, question:str):
    return llm({'question': question})
    
