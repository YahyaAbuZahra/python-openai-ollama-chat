from openai_client import ask_openai
from ollama_client import ask_ollama

def main():
    print("Welcome to the Python Tutor Chat Tool!\n")
    question = input("Please enter your Python question:\n> ").strip()
    print("\n--- Asking OpenAI GPT-4o-mini ---\n")
    ask_openai(question)
    print("\n--- Asking Ollama 3.2 ---\n")
    ask_ollama(question)

if __name__ == "__main__":
    main()
