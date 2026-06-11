from google import genai
print("Program Start")

client = genai.Client(
    api_key="Add your API key"
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain Artificial Intelligence in simple words",
    contents="What is the main idea behind the Transformer architecture?"
)

print(response.text)
prompt = "What is the main idea behind the Transformer architecture?"

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)
