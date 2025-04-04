from jinja2 import Template
from promptflow.core import tool
from promptflow.connections import CustomConnection
from promptflow.contracts.types import PromptTemplate
from .AIF_client import AIFLLMClient


@tool
def custom_llm(
    connection: CustomConnection, 
    api: str,          
    model_name: str,
    temperature: float,
    prompt: PromptTemplate,
    top_p: float,
    max_tokens: int,
    response_format: object,
    presence_penalty: float,
    frequency_penalty: int,    
    **kwargs
) -> str:  
    client = AIFLLMClient(
        auth_url=connection.configs['auth_url'],
        client_id=connection.configs['client_id'],
        client_secret=connection.secrets['client_secret'],
        scope=connection.configs['scope'],
        subscription_key=connection.configs['subscription_key']
    )   
    
    # Replace with your tool code, customise your own code to handle and use the prompt here.
    # Usually connection contains configs to connect to an API.
    # Not all tools need a connection. You can remove it if you don't need it.

    apiURL=f"{connection.configs['api_url']}/{model_name}"
    rendered_prompt = Template(prompt, trim_blocks=True, keep_trailing_newline=True).render(**kwargs)
    response = client.call_custom_model_api(
        apiURL= apiURL,       
        input_prompt=rendered_prompt,         
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        response_format=response_format,
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty
    )
    return response