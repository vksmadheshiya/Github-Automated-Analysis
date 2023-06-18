## Integrate our code OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"]=openai_key


def calculate_complexity_by_chatgpt(code_snippet):
    prompt = PromptTemplate(
        input_variables=['code_snippet'], 
        template = "Calculate the complexity(cyclomatic complexity) of given code snippet `{code_snippet}` and return complexity in float value without any explanation ")

    ## OPENAI LLMS
    llm=OpenAI(temperature=0.8)
    chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

    return chain.run(code_snippet)
