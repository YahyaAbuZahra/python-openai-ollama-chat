import requests

MODEL_LLAMA = "llama-3.2"

def ask_ollama(question: str) -> str:
    print(" LLaMA 3.2 says:\n")
    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": MODEL_LLAMA,
                "messages": [
                    {"role": "system", "content": "You are a helpful Python tutor."},
                    {"role": "user", "content": question}
                ],
                "stream": False
            }
        )
        if response.ok:
            answer = response.json()["message"]["content"]
            print(answer)
            return answer
        else:
            error_msg = " Failed to connect to Ollama. Is the server running?"
            print(error_msg)
            return error_msg
    except requests.exceptions.RequestException as e:
        error_msg = f" Error connecting to Ollama: {e}"
        print(error_msg)
        return error_msg
