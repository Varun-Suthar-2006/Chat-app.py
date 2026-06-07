# import namespaces
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
# Initialize the OpenAI client
token_provider = get_bearer_token_provider(
     DefaultAzureCredential(), "https://ai.azure.com/.default"
)
    
openai_client = OpenAI(
     base_url=azure_openai_endpoint,
     api_key=token_provider
)
# Get a response
completion = openai_client.chat.completions.create(
     model=model_deployment,
     messages=[
         {
             "role": "system",
             "content": "You are a helpful AI assistant that answers questions and provides information."
         },
         {
             "role": "user",
             "content": input_text
         }
     ]
)
print(completion.choices[0].message.content)