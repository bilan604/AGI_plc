from api import *
from parsing import *
from google_search import *

import string
def strip_args(func, args):
    valid = string.ascii_letters + "0123456789"
    args = list(args)
    while args and args[-1] not in valid:
        args.pop()
    args = args[::-1]
    while args and args[-1] not in valid:
        args.pop()
    args = args[::-1]
    args = "".join(args)
    if func == "__SUBTASKS__":
        args = [arg.strip() for arg in args.split("\n") if arg.strip()]
        return args
    return args

def get_function(agent, resp):
    for func in agent.functions:
        if func in resp:
            return func
    return None

def get_function_args(agent, resp):
    print("get_function_args()")
    print(resp)
    func = get_function(agent, resp)
    if func == None:
        return None
    
    args = "".join(resp.split(func)[1:])
    args = strip_args(func, args)

    return args







def handle_subtasks(agent, subtasks):
    ########## 0
    return agent.handle_subtasks(agent, subtasks, 0, 0)

def visit(agent, url):
    return get_content_by_url(url, agent.objective)

def get_prompt_response(agent, prompt):
    print("\n------------->get_prompt_response() prompt:")
    print(prompt)
    resp = get_gpt4_result(prompt)
    print("\n------------->get_prompt_response() resp:")
    print(resp)
    return resp

def get_search_urls(agent, query):
    return get_search_results(query)

def get_search_results_with_agent(agent, query):
    return get_search_query_content(query)

def exec(agent, code):
    try:
        resp = exec(code)
        return resp
    except Exception as e:
        return 'Exception on executing code:'+str(e)


######################
def chain(agent, objective, subtask_objective, previous_response, prompt_depth):
    inside_subtask = ""
    if subtask_objective != "":
        inside_subtask = \
        f"""\
You are currently inside a subtask. Your subtask objective is to forward your MAIN_OBJECTIVE given your previous response.\
{format("Your SUBTASK_OBJECTIVE", subtask_objective)}
"""

    s = \
    f"""\
Your task is to complete your MAIN_OBJECTIVE given the objective.

{format("Your MAIN_OBJECTIVE", agent.objective)}
{inside_subtask}
{format("Your PREVIOUS_RESPONSE", previous_response)}
{get_nonsubtask_outro(agent, objective, prompt_depth)}\
"""
    return s

def get_nonsubtask_outro(agent, objective, depth):
    s = \
    f"""\
You have the option to continue your chain of thought or do one of the following functionalities:
=>__SUBTASKS__: Creates a list of subtasks
=>__RETURN__: Returns your response to this prompt (as the result of) and immediately ends this chain of prompts.
=>__SEARCH__: Gets content from the internet given a search query. Will be stored in your next prompt as the result of your previous prompt.
=>__GET_SEARCH_URLS__: Gets a list of urls for a given search query. Will be stored in your next prompt as the result of your previous prompt.
=>__VISIT__: Visits a url and returns the text content from the url. Will be stored in your next prompt as the result of your previous prompt.
=>__EXEC__: Execute a chunk of Python code. Will be stored in your next prompt as the result of your previous prompt.

To select a functionality, respond in the format "__FUNCTIONALITY__:\n[the args for your functionality]".
Subtasks should be listed in the format: "__SUBTASKS__:\n1) description for subtask one\n2) description for subtask two\n" etc...

Alternatively you can choose none of the above and simply further your chain of though reasoning. Your response to this prompt will be included by default in your next prompt.

Do not forget the original objective. There are {depth} prompt(s) remaining in this chain of prompts, and a global upper bound of {agent.N**2} prompts (not including the prompts from parsing Google searches).\
"""
    return s

class AutoAuto(object):
    def __init__(self, objective="", N=5):
        self.objective = objective
        self.driver = None
        self.prompts = []
        self.responses = []
        self.N = N
        self.result = ""
        self.functions = {
            "__SUBTASKS__": handle_subtasks,
            "__RETURN__": get_prompt_response,
            "__SEARCH__": get_search_results_with_agent,
            "__GET_SEARCH_URLS__": get_search_urls,
            "__VISIT__": visit,
            "__EXEC__": exec
        }

    def handle_function(self, resp):
        """
        Checks if there is a function and handles it

        Returns outcome of operation
        """
        func = get_function(self, resp)
        if func == None:
            ##########    
            pass
        args = get_function_args(self, resp)

        if func == "__EXEC__":
            function_declrs = ["def exec", "def store", "def get_search_urls", "def get_prompt_response", "def visit", "os.chdir", "os.set", "os.", "subprocess.", "w+"]
            if any([fd in resp for fd in function_declrs]):
                return "Parsing Error"

        return self.functions[func](self, args)

    def handle_subtasks(self, subtasks, subtask_depth, prompt_depth):
        
        # cache
        responses = []
        for subtask in subtasks:
            resp = self.interpret_chain(subtask, resp, subtask_depth + 1, 0)
            # cache
            responses.append(resp)
        
        return self.interpret_chain("", resp, subtask_depth, prompt_depth - 1)

    def interpret_chain(self, subtask_objective, previous, subtask_depth, prompt_depth):
        # interpret_chain = self.chain
        # Here is where subtasks can be made
        if subtask_depth == 2:
            return previous
        if prompt_depth == 0:
            return previous

        if "__SUBTASKS__" not in previous:
            prompt = chain(self, self.objective, subtask_objective, previous, prompt_depth)
            resp = get_prompt_response(self, prompt)
            
            # Check if function called
            func = get_function(self, resp)
            args = ""
            if func != None:
                args = get_function_args(self, resp)
            
            if func == "__RETURN__":
                return args
            elif func != None:
                resp = self.functions[func](self, args)
                return self.interpret_chain(subtask_objective, resp, subtask_depth, prompt_depth - 1)    
            return self.interpret_chain(subtask_objective, resp, subtask_depth, prompt_depth - 1)
        
        subtasks = parse_subtasks(resp)
        return self.handle_subtasks(subtasks, subtask_depth, prompt_depth)

    def finalize_response(self, interpretation):
        return interpretation

    def complete_objective(self):
        # add more interpretations
        interpretation = self.interpret_chain("", "", 0, self.N)
        # handle last prompt, etc
        result = self.finalize_response(interpretation)
        self.result = result


obj = "What is going to be in Python version 3.12?"
aa = AutoAuto(obj, 3)
aa.complete_objective()
print(aa.resp)











