from main import prompt_autoauto

prompts = [
    """Write a report on the following topic: What influences how the perception and \
intent occurs? How could the perception of intent differ from actual intent, \
and how does context affect this issue? \
Is it possible for someone to project their own intent on things without intent \
in the first place?"""
]

for prompt in prompts:
    prompt_autoauto(prompt)