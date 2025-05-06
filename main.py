# Equations (first variable is the result)
finalEquations = [
    ["x'''''", "x''''","y","z","t'","p''''"],
    ["y'''''", "y", "x''"], 
    ["z'''''", "z", "y''''"],
    ["t'''''", "z''''", "z''", "z", "y"],
    ["p'''''", "x", "y", "z", "t", "p"]
]

startEquations = [
    ["x'''''", "x","y","z","t","p"],
    ["y'''''", "y", "x"], 
    ["z'''''", "z", "y"],
    ["t'''''", "z", "z", "z", "y"],
    ["p'''''", "x", "y", "z", "t", "p"]
]

def sumVar():
    pass

def integrateVar(var):
    return var + "'"

def equateVar(integratedList, answerList):
    pass

def run():
    for i in range(len(startEquations)):
        pass

run()