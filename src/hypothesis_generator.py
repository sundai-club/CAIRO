from src.openai_api import OpenAIApi
from src.utils import parse_llm_response

from dotenv import load_dotenv
load_dotenv()


openai_api = OpenAIApi()

MAX_RETRIES = 3


prompt = """
You are an expert agent specializing in generating comprehensive hypotheses based on information provided about companies and startups. Your task is to analyze the given company details thoroughly and generate multiple insightful hypotheses.
Your analysis should cover, but not be limited to, the following aspects:

Pain points the company can solve
Services it provides
Value proposition for customers/clients/investors
Potential market impact
Unique selling points or competitive advantages
Possible growth trajectories or expansion opportunities
Technological innovations or disruptive elements
Target audience or market segments
Potential challenges or risks the company might face
Societal or environmental impact, if applicable

Based on your analysis, generate 5 detailed hypotheses. Each hypothesis should focus on a different aspect of the company's potential, capabilities, or impact. Your hypotheses should be specific, well-reasoned, and grounded in the provided information.
When formulating your hypotheses:

Consider both immediate and long-term implications of the company's offerings
Think about how the company might evolve or adapt in its industry
Reflect on potential ripple effects in related industries or markets
Contemplate how the company's services or products might address emerging trends or future needs

Please think step-by-step and reason thoroughly over the given company description before generating your hypotheses. Your thought process should be detailed and logical, considering various angles and possibilities.
Details about the company:
{company_details}


Please articulate your thought process between the given thinking tags:
<thinking></thinking>


After your analysis, please generate the hypotheses in the following JSON format. Only output the hypotheses, without any additional commentary:
```json[{{"hypothesis": "hypothesis", "pain_point": "pain point", "pitch": "pitch"}}]```

Your hypotheses should be concise yet comprehensive, each capturing a distinct aspect of the company's potential impact, offerings, or value proposition. Avoid repetition and ensure each hypothesis provides a unique insight or perspective on the company's capabilities or market position.
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


desc = """
Sundai Club is an innovative community of engineers and developers focused on creating applications that leverage cutting-edge AI tools. The club operates on a subscription model, offering members access to a range of benefits and resources to support their AI-driven app development projects.
Key Features
Weekly Builds: Sundai Club members collaborate on building new AI applications every week, fostering a culture of continuous innovation and learning.
Exclusive Access: Members gain access to the latest AI tools and technologies, allowing them to stay at the forefront of AI development.
Community Engagement: The club provides a platform for like-minded engineers to connect, share ideas, and collaborate on projects.
Membership Benefits
AI Tool Access: Members receive access to a curated selection of advanced AI tools, enabling them to experiment with and integrate these technologies into their projects.
Learning Resources: The club offers educational materials and guidance to help members enhance their skills in AI application development.
Networking Opportunities: Sundai Club facilitates connections between engineers, potentially leading to collaborations and knowledge sharing.
Project Focus
The applications developed by Sundai Club members likely span a wide range of domains, leveraging various AI technologies such as:
Natural Language Processing
Computer Vision
Machine Learning
Generative AI
By focusing on the latest AI tools, Sundai Club members are positioned to create innovative applications that push the boundaries of what's possible with artificial intelligence.

"""
print(generate_hypothesis(desc))