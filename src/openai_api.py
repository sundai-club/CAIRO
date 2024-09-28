import openai

class OpenAIApi:
    def __init__(self):
        self.open_ai_client = openai.OpenAI()

    def get_completion(self, messages, model="gpt-4o-mini"):
        response = self.open_ai_client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.4,
            max_tokens=2048
                            )
        return response.choices[0].message.content