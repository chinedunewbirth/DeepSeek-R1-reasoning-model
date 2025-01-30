import ollama 
import time

start = time.time()

desiredModel = "deepseek-r1:1.5b"
questionToAsk = "step by step solve quadratic equation 2x^2 + 5x + 3 = 0"

response = ollama.chat(model=desiredModel, messages=[
    {
        'role': 'user',
        'content': questionToAsk,
    },
])

OllamaResponse=response['message']['content']

print(OllamaResponse)

with open('outputOllama.txt', 'w', encoding='utf-8') as f:
    f.write(OllamaResponse)

end = time.time()

print(f"Time taken: {end - start} seconds")