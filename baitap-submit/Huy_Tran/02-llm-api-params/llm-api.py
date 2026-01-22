# 1
from openai import OpenAI

client = OpenAI(
    base_url = "https://api.groq.com/openai/v1",
    api_key = "",
)

print("Hello, I am a Chatbot_Intelligent, how can I help you today? (type 'exit' to exit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Thank you! See you later.")
        break

    response = client.responses.create(
        model="llama-3.1-8b-instant",
        input=user_input
    )

    bot_reply = response.output_text
    print("Bot:", bot_reply)
    
