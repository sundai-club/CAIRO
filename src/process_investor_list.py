import numpy as np
from scipy.optimize import linear_sum_assignment
from copy import deepcopy
from itertools import product
import random
import re
import json
from prompt_scoring_list import score_investor_on_hypothesis
from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import SimpleJsonOutputParser
# from langchain_core.output_parsers import BaseOutputParser
from langchain_core.exceptions import OutputParserException
from langchain_core.runnables import chain
# from tenacity import retry, stop_after_attempt, retry_if_exception_type


# class ScratchpadAndScoreParser(BaseOutputParser[dict]):
#     def parse(self, text: str) -> dict:
#         scratchpad_match = re.search(r"<scratchpad>(.*?)</scratchpad>", text, re.DOTALL)
#         score_match = re.search(r"<score>(\d+)</score>", text)

#         if scratchpad_match and score_match:
#             scratchpad = scratchpad_match.group(1).strip()
#             score = int(score_match.group(1))
#             return {"scratchpad": scratchpad, "score": score}
#         else:
#             raise OutputParserException(
#                 error="The output could not be parsed correctly.",
#                 observation="Ensure the output contains both <scratchpad> and <score> tags.",
#                 llm_output=text,
#             )
# def parse_output(text: str) -> dict:
#     scratchpad_match = re.search(r"<scratchpad>(.*?)</scratchpad>", text, re.DOTALL)
#     score_match = re.search(r"<score>(\d+)</score>", text)

#     if scratchpad_match and score_match:
#         scratchpad = scratchpad_match.group(1).strip()
#         score = int(score_match.group(1))
#         return {"scratchpad": scratchpad, "score": score}
#     else:
#         raise OutputParserException(
#             error="The output could not be parsed correctly.",
#             observation="Ensure the output contains both <scratchpad> and <score> tags.",
#             llm_output=text,
#         )
def parse_output(text: str) -> dict:
    scratchpad_match = re.search(r"<scratchpad>(.*?)</scratchpad>", text, re.DOTALL)
    score_match = re.search(r"<score>(.*?)</score>", text, re.DOTALL)

    if scratchpad_match and score_match:
        scratchpad = scratchpad_match.group(1).strip()
        score_json = score_match.group(1).strip()
        try:
            scores = json.loads(score_json)
        except json.JSONDecodeError:
            raise OutputParserException(
                error="The score JSON could not be parsed correctly.",
                observation="Ensure the score JSON is well-formed.",
                llm_output=text,
            )
        return {"scratchpad": scratchpad, "scores": scores, "mean_score": sum(scores.values()) / len(scores)}
    else:
        raise OutputParserException(
            error="The output could not be parsed correctly.",
            observation="Ensure the output contains both <scratchpad> and <score> tags.",
            llm_output=text,
        )
# output_parser = ScratchpadAndScoreParser()

llm = ChatOpenAI(model="o1-mini", temperature=1, max_retries=10)

@chain
def score_person(arg):
    investor, hypothesis = arg
    score_person_chain = score_investor_on_hypothesis | llm
    # print(f"Processing investor: \033[92m{investor['name']}\033[0m with hypothesis \033[92m{hypothesis['hypothesis']}\033[0m")
    for _ in range(5):
        try:
            answer = score_person_chain.invoke(
                {
                    "PERSON_OF_INTEREST_INFO": json.dumps(investor, indent=4),
                    "HYPOTHESIS": hypothesis["hypothesis"],
                    "PAIN_POINT": hypothesis["pain_point"],
                    "PITCH": hypothesis["pitch"],
                }
            )
            investor.update(parse_output(answer.content))
            # investor["reasoning"] = answer["scratchpad"]
            # investor["score"] = answer["score"]
            investor.update(hypothesis)
            # print(f"Done processing investor: {investor['name']}")
            return investor
        except Exception as e:
            import traceback
            print("Exception occurred while processing investor:")
            print(traceback.format_exc())
            print(f"Failed to process investor: {investor['name']}")
    return investor



def score_persons(
    investors_list: list[dict[str, str]],
    hypotheses: list[dict[str, str]],
    num_investors: int = 100,
):
    investors_list = random.sample(investors_list, min(num_investors, len(investors_list)))
    inv_id = 0
    for inv in investors_list:
        inv['id'] = inv_id
        inv_id += 1
    hyp_id = 0
    for hyp in hypotheses:
        hyp['hyp_id'] = hyp_id
        hyp_id += 1
    args = [(deepcopy(investor), hypothesis) for investor, hypothesis in product(investors_list, hypotheses)]
    print(f"Processing {len(args)} arguments")
    return score_person.batch(args, {'max_concurrency': 5000})


def collapse_investors_scored(investors_scored):
    investors_scored_collapsed = []
    idx_of_investor = {}
    
    for investor in investors_scored:
        inv_id = investor['id']
        hyp_id = investor['hyp_id']
        
        if inv_id not in idx_of_investor:
            idx_of_investor[inv_id] = len(investors_scored_collapsed)
            investors_scored_collapsed.append({
                'id': inv_id,
                'name': investor['name'],
                'current location': investor['current location'],
                'description': investor['description'],
                'website': investor['website'],
                'other links': investor['other links'],
                'current firm name': investor['current firm name'],
                'firm url': investor['firm url'],
                'firm description': investor['firm description'],
                'firm investment': investor['firm investment'],
                'scores_per_hypothesis': {}
            })
        
        investors_scored_collapsed[idx_of_investor[inv_id]]['scores_per_hypothesis'][hyp_id] = {
            'scratchpad': investor['scratchpad'],
            'scores': investor['scores'],
            'mean_score': investor['mean_score'],
            'hypothesis': investor['hypothesis'],
            'pain_point': investor['pain_point'],
            'pitch': investor['pitch']
        }
    
    return investors_scored_collapsed


def process_investors_scored(investors_scored, hypotheses, max_investors_per_hypothesis=None):
    if max_investors_per_hypothesis is None:
        max_investors_per_hypothesis = len(investors_scored) // len(hypotheses)
    # Collapse the investors scored
    investors_scored_collapsed = collapse_investors_scored(investors_scored)

    # Create a dictionary to track the number of investors assigned to each hypothesis
    hypothesis_capacity = {hyp['hyp_id']: 0 for hyp in hypotheses}

    # Sort investors based on their highest mean score for any hypothesis
    sorted_investors = sorted(investors_scored_collapsed, key=lambda inv: max(inv['scores_per_hypothesis'].values(), key=lambda x: x['mean_score'])['mean_score'], reverse=True)

    # Assign each investor to the hypothesis with the highest mean score that hasn't reached its capacity
    for inv in sorted_investors:
        best_hypothesis = None
        best_score = -float('inf')
        for hyp_id, scores in inv['scores_per_hypothesis'].items():
            if hypothesis_capacity[hyp_id] < max_investors_per_hypothesis and scores['mean_score'] > best_score:
                best_hypothesis = hyp_id
                best_score = scores['mean_score']
        
        if best_hypothesis is not None:
            best_hyp = inv['scores_per_hypothesis'][best_hypothesis]
            hypothesis_capacity[best_hypothesis] += 1
            inv['matched_hypothesis'] = {
                'hypothesis': best_hyp['hypothesis'],
                'pain_point': best_hyp['pain_point'],
                'pitch': best_hyp['pitch'],
                'hyp_id': best_hyp['hyp_id'],
            }

    return investors_scored_collapsed

def get_aldo_data(hypotheses: list[dict[str, str]]):
    with open("investors_list_no_score.jsonl", "r", encoding="utf-8") as file:
        investors_list = [json.loads(line) for line in file]
    investors_list = random.sample(investors_list, min(100, len(investors_list)))
    investors_scored = score_persons(investors_list, hypotheses)
    assigned_investors = process_investors_scored(investors_scored, hypotheses)
    return assigned_investors


if __name__ == "__main__":
    # Read the JSONL file and output a simple list
    with open("investors_list_no_score.jsonl", "r", encoding="utf-8") as file:
        investors_list = [json.loads(line) for line in file]
    with open("hypothesis.jsonl", "r", encoding="utf-8") as file:
        hypothesis = [json.loads(line) for line in file]
    test = get_aldo_data(hypothesis)
    # investors_list = random.sample(investors_list, min(100, len(investors_list)))
    # import time
    # start_time = time.time()
    # investors_scored = score_persons(investors_list, hypothesis)
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print(f"Time taken to score investors: {elapsed_time:.2f} seconds")
    # with open("investors_scored.jsonl", "w", encoding="utf-8") as outfile:
    #     for investor in investors_scored:
    #         json.dump(investor, outfile)
    #         outfile.write("\n")

    # investors_scored = [json.loads(line) for line in open("investors_scored.jsonl", "r", encoding="utf-8")]
    # from IPython import embed; embed()
    
    # investors_scored_ = process_investors_scored(investors_scored, hypothesis)

    # investors_cross_hypothesis = {
    #     h['hypothesis']: score_persons(investors_list, score_list_investors, h)
    #     for h in hypothesis
    # }

    # investors_list_scored = score_persons(investors_list, score_list_investors, hypothesis[0])

    # investors_list_scored_no = [investor for investor in investors_list_scored if "score" not in investor]
    # score_person.invoke((investors_list_scored_no[0], hypothesis[0], score_list_investors))
    # print(score_list_investors.format(
    #     PERSON_OF_INTEREST_INFO=json.dumps(investors_list[0], indent=4),
    #     HYPOTHESIS=hypothesis[0]["hypothesis"],
    #     PAIN_POINT=hypothesis[0]["pain_point"],
    #     PITCH=hypothesis[0]["pitch"],
    # ))

    # score_person.invoke((investors_list[0], hypothesis[0], score_list_investors))
