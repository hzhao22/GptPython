import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = ""

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Can you tell me something about Oakville, ON?"}
    ]
)

print(response)
print(response["choices"][0]["message"]["content"])
