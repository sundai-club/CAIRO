import openai
from typing import List, Dict, Optional
from ai21 import AI21Client
from ai21.models.chat import UserMessage, SystemMessage

class OpenAIApi:
    def __init__(self, api_key: Optional[str] = None):
        self.client = openai.OpenAI(api_key=api_key)

    def get_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "gpt-4-0125-preview",
        temperature: float = 0.4,
        max_tokens: int = 2048
    ) -> str:
        try:
            print("Inside get_completion")
            print("model:", model)
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            print("Response:", response)
            return response.choices[0].message.content
        except openai.OpenAIError as e:
            raise Exception(f"OpenAI API error: {str(e)}")
        
class JambaAIApi:
    def __init__(self, api_key: Optional[str] = None):
        self.client = AI21Client(api_key=api_key)

    def get_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "jamba-1.5-large",
        temperature: float = 0.4,
        max_tokens: int = 2048
    ) -> str:
        mm = []
        for m in messages:
            if m["role"]=="user":
                mm.append(UserMessage(content=m["content"]))
            elif m["role"]=="system":
                mm.append(SystemMessage(content=m["content"]))
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=mm,
                top_p=temperature,
            )
            return str(response.choices[0].message.content)
        except:
            raise Exception("Jamba")
