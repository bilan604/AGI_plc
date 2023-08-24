import json
from AutoAuto import AutoAuto


def prompt_autoauto(prompt):
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


prompts = [
    """Please note: In the following EXERCISE, it is important that you only respond with a single line in the format (x, y). Imagine you are standing in a 2D coordinate grid at (0, 0) where coordinates are represented like (x, y). You are currently facing the positive y direction. EXERCISE: If you take 3 steps backward, then take 1 step backward, what coordinate are you at?""",
]

for prompt in prompts:
    prompt_autoauto(prompt)