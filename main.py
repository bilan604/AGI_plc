import sys
import json
from parsing import get_env
from AutoAuto import AutoAuto


import openai
openai.api_key = get_env()["OPENAI_API_KEY"].strip()


def prompt_autoauto(prompt: str):
    
    objective = prompt
    print(objective)

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


prompt = \
f"""\
Given a PIL image in Python, write the function(s) necessary to take the PIL image (screenshot of browser) and generate the coordinates required for \
a mouse click based on instructions provided by SUBTASK objective (i.e. clicking a button or moving the mouse to an input box before clicking it to type something)."""
for i in range(3):
    prompt_autoauto(prompt)

