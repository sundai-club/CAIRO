hypotheis_update_prompt = """
You are given the following company information and all the hypotheses generated based on the company information and different value adds it provides.

Details about the company:
{company_details}

Hypotheses:
{hypotheses}

Now based on the user input, update the hypotheses based on the company details and provide the updated hypotheses.

Conversation history:
{conversation_history}

User input:
{user_input}

Return all the updated hypotheses in the same format as the original hypotheses along with the reasoning.
```json[{{"hypothesis": "hypothesis", "pain_point": "pain point", "pitch": "pitch"}}, ...]```

Output:
"""