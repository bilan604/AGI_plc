"""
Test stuff here
"""




def do_execute(code):
    global output_variable, output_error
    output_variable = None
    output_error = None
    try:    
        ##########
        # asign last variable to output variables
        code = "global output_variable, output_error\n" + code
        code = [l.strip() for l in code.split("\n") if l.strip()]
        if "print" in code[-1]:
            code[-1] = code[-1].replace("print", "", code[-1]) + "[0]"
        
        code[-1] = f"output_variable = {code[-1]}"
        code = "\n".join(code)
        
        print("!!!!!!!!!!!!!!!!!!!!!!!!! executing code:")
        print(code)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!")

        exec(code)
        
        return output_variable, output_error

    except Exception as e:
        print("Error:", e)
        return output_variable, e

code = """\
import numpy as np
arr = np.array([[0,1,2], [2,3,1]])

arr
"""
a,b=do_execute(code)
print(a)
print(b)



