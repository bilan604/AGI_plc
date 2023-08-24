import sys
import json
from parsing import get_env
from AutoAuto import AutoAuto

from flask import Flask, request, jsonify

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



app = Flask(__name__)

@app.route('/api/', methods=['POST'])
def post_request():
    data = request.get_json()  # Load the JSONified dictionary from the request
    if 'prompt' in data:
        prompt = data['prompt']  # Get the 'prompt' parameter value
        resp = "Error on AutoAuto runtime"
        resp = prompt_autoauto(prompt)
        return jsonify({'message': resp})  # Return a response
    else:
        return jsonify({'error': 'No prompt parameter found in the request.'})  # Error message if 'prompt' is not in the request body.

if __name__ == '__main__':
    app.run(debug=True)





