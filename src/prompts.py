hypotheis_update_prompt = """
You are given the following company information and the customer personas previously generated based on the company's details.

Company Details:

{company_details}

Existing Customer Personas:

{customer_personas}

Now, based on the user input, refine and update the customer personas while ensuring they remain grounded in the company details. Provide the updated customer personas.

Conversation History:

{conversation_history}

User Input:

{user_input}

Please think step-by-step and reason thoroughly over the given information before updating the personas. Your thought process should be detailed and logical, considering various angles and possibilities. Articulate your thought process within the <thinking></thinking> tags.

Return all the updated customer personas in the same format as the original personas, without any additional commentary.

Output Format:
[
  {
    "persona_name": "Name",
    "demographics": "Demographics",
    "psychographics": "Psychographics",
    "pain_points": "Pain points",
    "needs": "Needs",
    "how_company_addresses_needs": "How the company's products or services address these needs",
    "preferred_communication_channels": "Preferred communication channels",
    "preferred_device_type": "Preferred device type",
    "trigger_events": "Trigger events that indicate buying opportunities",
    "purchasing_behavior": "Purchasing behavior and decision-making process",
    "potential_objections": "Potential objections to overcome",
    "influences_and_motivators": "Influences and motivators",
    "goals_and_aspirations": "Goals and aspirations",
    "pitch": "Pitch"
  }
]
Final Notes:

Ensure each persona is concise yet comprehensive.
Avoid repetition; each persona should provide a unique insight into the company's potential customers.
"""
