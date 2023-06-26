import openai

def run_openai(prompt, api_key, model="gpt-3.5-turbo"):
    openai.api_key = api_key
    completion = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}] # 입력 prompt
    )
    answer = completion['choices'][0]['message']['content'].strip()
    token = completion.usage.total_tokens
    return answer, token

