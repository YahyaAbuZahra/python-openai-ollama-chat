import openai
#use your API KEY
openai.api_key = "£££££££"
MODEL_GPT = 'gpt-4o-mini'

def ask_openai(question: str) -> str:
    
    print(" GPT-4o-mini says:\n")
    response = openai.chat.completions.create(
        model=MODEL_GPT,
        messages=[
            {"role": "system", "content": "You are a helpful Python tutor."},
            {"role": "user", "content": question}
        ],
        stream=True
    )
    full_reply = ""
    for chunk in response:
        content = chunk.choices[0].delta.content or ""
        print(content, end="", flush=True)
        full_reply += content
    print("\n")
    return full_reply
