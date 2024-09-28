from langchain_core.prompts import PromptTemplate

score_investor_on_hypothesis = """# Task Description
Given the following information about a person of interest:
<person_of_interest_info>
{PERSON_OF_INTEREST_INFO}
</person_of_interest_info>
And the following hypothesis:

<hypothesis>{HYPOTHESIS}</hypothesis>
<pain_point>{PAIN_POINT}</pain_point>
<pitch>{PITCH}</pitch>

Please analyze the potential value of reaching out to this investor based on the given hypothesis. Consider the investor's background, expertise, investment focus, and any other relevant information. Then, provide a score on a scale of 0 to 10 for each of the following rubrics, where 0 means not relevant at all and 10 means highly relevant.

Use the following guidelines to inform your scoring decision:

1. Strategic Fit (x2 weight): Evaluate how well the hypothesis aligns with the investor's strategic focus areas and investment thesis.
2. Investment Stage & Range Alignment: Assess if the implied stage and scale of the pitch match the investor's preferred investment stages and typical investment range.
3. Sector Expertise: Consider the depth of the investor's expertise in the relevant sector(s).
4. Track Record: Evaluate the investor's history of successful investments in similar areas.
5. Value-Add Potential: Assess the investor's ability to provide value beyond capital (e.g., network, mentorship, industry insights).
6. Decision-Making Authority: Consider the investor's role and ability to influence investment decisions.
7. Recent Investment Activity: Evaluate how active the investor has been recently in making new investments.
8. Geographical Alignment: Assess if the investor's geographical focus matches the scope of the hypothesis/pitch.
9. Innovation Appetite: Evaluate the investor's interest in and history of backing innovative or disruptive solutions.
10. Potential for Follow-On Investment: Consider the investor's capacity and history of providing follow-on funding.

Instructions for Analysis:
1. Use a <scratchpad> section to work through your reasoning based on the guidelines above. Consider each relevant factor and how it contributes to the overall score for each rubric.
2. After analyzing individual factors, provide a summary paragraph that synthesizes your analysis and highlights the most compelling reasons for or against reaching out to this investor.
3. After the scratchpad, provide a JSON object with the scores for each rubric enclosed in <score> tags. For example:
<score>
{{
    "Strategic Fit": 8,
    "Investment Stage & Range Alignment": 7,
    "Sector Expertise": 9,
    "Track Record": 6,
    "Value-Add Potential": 8,
    "Decision-Making Authority": 7,
    "Recent Investment Activity": 5,
    "Geographical Alignment": 6,
    "Innovation Appetite": 9,
    "Potential for Follow-On Investment": 7
}}
</score>
Remember to use the full range of scores (0-10) to differentiate levels of relevance, and focus on the available data if any information is missing for certain criteria. A high score should indicate an investor who not only aligns well with the hypothesis but also has the potential to be a valuable long-term partner.
# Output Format: 
make sure your output has this format so it's easy to parse.
<scratchpad>
1. Strategic Fit: [Your analysis]
2. Investment Stage & Range Alignment: [Your analysis]
[Continue with relevant factors...]
10. Potential for Follow-On Investment: [Your analysis]
[A paragraph summarizing the key points from your analysis, synthesizing the information to give an overall picture of the investor's relevance]
</scratchpad>
then output a JSON object with the scores for each rubric enclosed in <score> tags.
"""

score_investor_on_hypothesis = PromptTemplate.from_template(score_investor_on_hypothesis)
