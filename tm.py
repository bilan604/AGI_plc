from main import prompt_autoauto

prompts = [
    """Please note: In the following EXERCISE, it is important that you only respond with a single line in the format (x, y). Imagine you are standing in a 2D coordinate grid at (0, 0) where coordinates are represented like (x, y). You are currently facing the positive y direction. EXERCISE: If you take 3 steps backward, then take 1 step backward, what coordinate are you at?""",
]

for prompt in prompts:
    prompt_autoauto(prompt)