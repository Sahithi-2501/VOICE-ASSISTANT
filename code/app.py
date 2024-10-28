from openai import OpenAI
from apikey import api_data

Model='gpt-4o'
client = OpenAI(api_key=api_data)

def Reply(Question):
    completion = client.chat.completions.create(
        model=Model,
        messages=[
            {'role':"system","content":"You are a helpful assistant"},
            {'role':"user","content":question}
        ],
        max_tokens = 200
    )
    answer = completion.choices[0].message.content
    return answer

question = "In simple terms explain me AI not more than 50 words?"

ans = Reply(question)

print(ans)