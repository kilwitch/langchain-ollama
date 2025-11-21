from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template ="""
Answer the question below:

Here is the conversation:{context}

Question: {question}

Answer:
"""
model =OllamaLLM(model="llama2")
prompt=ChatPromptTemplate.from_template(template)

chain= prompt|model

def handle_conversation():
    context=""
    print("Welcome to the chat! Type 'exit' to quit.")
    while True:
        user_input=input("You:")
        if user_input.lower()=='exit':
            print("Goodbye!")
            break
        response = chain.invoke({"context":context,"question":user_input})
        print("Bot:",response)
        context +=f"\nUser: {user_input}\nBot: {response}"

if __name__=="__main__":
    handle_conversation()