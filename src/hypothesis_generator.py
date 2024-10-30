from src.openai_api import OpenAIApi
from src.utils import parse_llm_response

from dotenv import load_dotenv
import os
load_dotenv()

print("\n\n\n")
openai_api = OpenAIApi(os.getenv("OPENAI_API_KEY"))


MAX_RETRIES = 3


prompt = """
Your task is to generate 5 detailed customer personas based on the company details provided below.

Analysis Requirements:

Your analysis should cover, but not be limited to, the following aspects for each persona:

Demographics: Age, gender, location, education, occupation.
Psychographics: Interests, values, lifestyle, attitudes.
Pain Points or Challenges: Specific problems or challenges the customer faces.
Needs and Desires: What the customer is seeking to achieve or obtain.
How the Company Addresses These Needs: Ways in which the company's products or services fulfill the customer's needs.
Preferred Communication Channels: Methods of communication the customer prefers (e.g., email, social media, phone).
Preferred Device Type: Devices the customer commonly uses (e.g., smartphone, tablet, desktop).
Trigger Events: Events or circumstances that indicate a buying opportunity.
Purchasing Behavior and Decision-Making Process: How the customer makes purchasing decisions.
Potential Objections to Overcome: Reasons the customer might hesitate to purchase.
Influences and Motivators: Factors that influence the customer's decisions.
Goals and Aspirations: What the customer hopes to achieve personally or professionally.
Pitch: A tailored message that would appeal to the customer.
Persona Creation Guidelines:

Distinct Segments: Each persona should represent a unique segment of the target audience.
Interaction with Offerings: Consider how each persona interacts with the company's products or services.
Positioning: Reflect on how the offerings can be positioned to appeal to each persona.
Emerging Trends: Contemplate trends or future needs that might influence each persona.
Trigger Events Identification: Identify events that indicate a buying opportunity for each persona.
Device Preference: Specify the preferred device type for each persona.
Instructions:

Think Step-by-Step:

Reason thoroughly over the company description before generating the personas.
Your thought process should be detailed and logical, considering various angles and possibilities.
Articulate your thought process within the <thinking></thinking> tags.
Generate Personas:

After your analysis, present the personas in the following JSON format.
Only output the personas without any additional commentary.
Company Details:

{company_details}

Output Format:
```json[
  {{
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
  }}
]```

Output should contain persona name, demographics, psychographics, pain points, needs, how the company addresses these needs, preferred communication channels, preferred device type, trigger events, purchasing behavior, potential objections, 
influences and motivators, goals and aspirations, and pitch for each persona.

Final Notes:

Conciseness and Comprehensiveness: Ensure each persona is concise yet comprehensive.
Uniqueness: Avoid repetition; each persona should provide a unique insight into the company's potential customers.
"""

system_prompt = """
You are an AI assistant specialized in Sales and Marketing Automation. Your primary function is to analyze company information and generate detailed customer personas. Your responsibilities include:

Analyzing Company Details:
Carefully examine the provided company information to understand their core business, products/services, target market, and unique value propositions.
Generating Customer Personas:
Create comprehensive customer personas that represent distinct segments of the company's target audience.
Considering Key Aspects:
Incorporate demographics, psychographics, pain points, needs, preferred communication channels, preferred device types, trigger events, purchasing behaviors, potential objections, influences, motivators, goals, and aspirations.
Structured Thinking Process:
Think step-by-step and reason thoroughly, considering various angles and possibilities.
Articulate your thought process within the designated thinking tags: <thinking></thinking>.
Formatting Output:
Present the final personas in the specified JSON format.
Do not include any additional commentary or explanations outside the required format.
Remember to focus solely on generating customer personas based on the given information. Your output should be clear, relevant, and adhere strictly to the format specified in the user's prompt.
"""


def generate_hypothesis(company_details):
    messages = [{'role': 'system', 'content': system_prompt},
        {"role": "user", "content": prompt.format(company_details=company_details)}]

    hypothesis = None
    print("Inside generate hypithesis")
    for _ in range(MAX_RETRIES):
        print("Inside for loop")
        try:
            print("Inside try")
            response = openai_api.get_completion(messages, model="gpt-4o-mini")
            print("Response:", response)
            hypothesis = parse_llm_response(response)                
            if hypothesis is not None:
                return hypothesis
            
        except:
            pass
    return hypothesis



def edit_hypothesis(hypothesis, conversation):
    messages = [{'role': 'system', 'content': system_prompt},
        {"role": "user", "content": prompt.format(company_details=conversation)}]

    hypothesis = None
    for _ in range(MAX_RETRIES):
        try:
            response = openai_api.get_completion(messages, model="gpt-4o-mini")
            hypothesis = parse_llm_response(response)                
            if hypothesis is not None:
                return hypothesis
            
        except:
            pass
    return hypothesis
