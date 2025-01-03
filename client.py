from openai import OpenAI
client = OpenAI(
    api_key="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"
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)