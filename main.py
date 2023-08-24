import sys
import json
from parsing import get_env
from AutoAuto import AutoAuto


import openai
openai.api_key = get_env()["OPENAI_API_KEY"].strip()


def prompt_autoauto(prompt: str):
    
    objective = prompt

    AGI = AutoAuto(objective)
    AGI.complete_objective()
    print("\n===================>:")
    print(AGI.result)
    print("---------fin----------")
    
    ########################
    with open("responses.txt", "a") as f:
        if type(AGI.result) == str and AGI.result:
            save_obj = {"objective": objective, "response": AGI.result}
            f.write(json.dumps(save_obj))
    #######################

    return AGI.result


