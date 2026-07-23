import ollama
import traceback

messages = [
    {"role": "system", "content": "You are a helpful assistant, who responds to user queries and then provide the total count of tokens and their respective mappings to the user message"},
    {"role": "user", "content": "hello, I am Arunabha, can you tell me a joke?"}
]

messages_2 = [
    {"role": "system", "content": "You are a helpful assistant, who responds to user queries and then provide the total count of tokens and their respective mappings to the user message"},
    {"role": "user", "content": "hello, Tell me what's my name?"}
]


res = ollama.chat(
    model="llama3.2:1b",
    messages=messages_2,
    options={
        "temperature": 0.7,
        "seed": 70,
    }
)
print(res.message.content)