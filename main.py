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

prompt1 = """Please note: In the following EXERCISE, it is important that you only respond with a single line in the format (x, y). Imagine you are standing in a 2D coordinate grid at (0, 0) where coordinates are represented like (x, y). You are currently facing the positive y direction.

EXERCISE: If you take 3 steps backward, then take 1 step backward, what coordinate are you at?"""
prompt2 = """You are a codebreaker and you know the keyboard layout of Nokia's 3310 model released in 2000. There is a person who set a purely digital password for his social account. In order to facilitate memory, he referred to the layout of the 3310 mobile phone keyboard and wrote a line of letters in the notebook. I tell you the letters, you tell me the password, without explanation. For example, I give you "faopwgoapwjgaweojgop", you reply "32679462795429365467". If you can't do it, just reply "Unknown".

ok"""
prompt3 = """Pretend you are 3DPathGPT, a model that can accurately track 3D paths on, around, and through planet Earth based on plain language descriptions. For each path, determine the state, province, or ocean of the final destination. You may assume the object traveling the path encounters no resistance, such as if it were a neutrino. Try reasoning through the 3D path one step at a time, and at the end, provide the final answer enclosed in square brackets like [Europe]. Start at the center of San Francisco and travel due East 0.1 degrees
"""

for prompt in [prompt2, prompt3]:
    prompt_autoauto(prompt)

