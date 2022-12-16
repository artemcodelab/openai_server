import openai

API_KEY = "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"

openai.api_key = API_KEY
completion = openai.Completion()

def ask(message, engine, temperature, max_tokens, top_p, presence_penalty):
    response = openai.Completion.create(
        engine=engine,
        prompt=message,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        presence_penalty=presence_penalty,
        stop="\n"
    )
    return str(response.choices[0].text)