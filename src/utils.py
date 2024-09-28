import re
import ast

def parse_llm_response(response):
    match = re.findall(r"```json(.*?)```", response, re.DOTALL)
    if len(match) == 0:
        return None
    try:
        response = ast.literal_eval(match[0])
    except:
        response = None
    return response