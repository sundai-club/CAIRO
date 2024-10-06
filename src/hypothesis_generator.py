from src.openai_api import OpenAIApi
from src.utils import parse_llm_response

from dotenv import load_dotenv
load_dotenv()


openai_api = OpenAIApi()

MAX_RETRIES = 3


prompt = """
You are an expert in Sales and Marketing Automation, specializing in generating detailed customer personas based on company information provided. Your task is to thoroughly analyze the given company details and generate multiple comprehensive customer personas.

Your analysis should cover, but not be limited to, the following aspects:

Demographics (age, gender, location, education, occupation)
Psychographics (interests, values, lifestyle, attitudes)
Pain points or challenges the customer faces
Needs and desires
How the company's products or services address these needs
Preferred communication channels
Preferred device type
Trigger events that indicate buying opportunities
Purchasing behavior and decision-making process
Potential objections to overcome
Influences and motivators
Goals and aspirations
Based on your analysis, generate 5 detailed customer personas. Each persona should represent a distinct segment of the company's target audience. Your personas should be specific, well-reasoned, and grounded in the provided information.

When formulating your personas:

Consider both current and potential future customers.
Think about how each persona interacts with the company's offerings.
Reflect on how the company's products or services can be positioned to appeal to each persona.
Contemplate emerging trends or future needs that might influence the personas.
Identify trigger events that indicate a buying opportunity for each persona.
Specify the preferred device type for each persona.
Please think step-by-step and reason thoroughly over the given company description before generating your personas. Your thought process should be detailed and logical, considering various angles and possibilities.

Details about the company:

{company_details}

Please articulate your thought process between the given thinking tags:

<thinking></thinking>

After your analysis, please generate the personas in the following JSON format. Only output the personas, without any additional commentary:

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

Your personas should be concise yet comprehensive, each capturing a distinct aspect of the company's target audience. Avoid repetition and ensure each persona provides a unique insight or perspective on the company's potential customers.

Output:
"""

system_prompt = """
You are an AI assistant specialized in analyzing company information and generating insightful hypotheses. Your primary function is to interpret company details, identify key aspects of their business model, and formulate well-reasoned hypotheses about their potential impact and value proposition.
When presented with company information, you will:

Carefully analyze the provided details to understand the company's core business, target market, and unique offerings.
Think critically about the industry context and potential market needs that the company might be addressing.
Use your analytical skills to identify possible pain points the company could solve, services they might offer, and values they could provide to customers, clients, or investors.
Generate multiple hypotheses that cover these aspects, ensuring they are grounded in the information provided and logical deductions.
Present your thought process clearly within the designated thinking tags.
Format your final hypotheses in the specified JSON structure.

You should aim to be thorough in your analysis but concise in your output. Your hypotheses should be clear, relevant, and potentially valuable insights about the company's business potential.
Remember to focus solely on generating hypotheses based on the given information. Do not include any additional commentary, explanations, or questions in your final output. Adhere strictly to the format specified in the user's prompt.
"""


def generate_hypothesis(company_details):
    messages = [{'role': 'system', 'content': system_prompt},
        {"role": "user", "content": prompt.format(company_details=company_details)}]

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
