# from dotenv import load_dotenv
# from os.path import join, dirname
# from os import getenv
import openai

# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

openai.api_key = "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" #getenv("API_KEY")
completion = openai.Completion()

def ask(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        presence_penalty=0.6,
        stop="\n"
    )
    return str(response.choices[0].text)