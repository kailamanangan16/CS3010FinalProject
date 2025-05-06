# Equations (first variable is the result)
startEquations = [
    ["x'''''", "x","y","z","t","p"],
    ["y'''''", "y", "x"], 
    ["z'''''", "z", "y"],
    ["t'''''", "z", "z", "z", "y"],
    ["p'''''", "x", "y", "z", "t", "p"]
]

answerEquations = [
    ["x'''''", "x''''","y","z","t'","p''''"],
    ["y'''''", "y", "x''"], 
    ["z'''''", "z", "y''''"],
    ["t'''''", "z''''", "z''", "z", "y"],
    ["p'''''", "x", "y", "z", "t", "p"]
]

def integrateVar(var):
    return var + "'"


# -> start = startEquations[i] 
# -> answer = answerEquations[i]
def sumVar(start, answer): # makes all the start equation variables integrate ready
    for i in range(1,len(start)): # i = the variable that needs to be integrated
        while start[i] != answer[i]:
            start[i] = integrateVar(start[i])
            
# -> start = startEquations[i] 
# -> answer = answerEquations[i]
def equateVar(start, answer): #if these two are equal return true
    return start == answer

def run():
    result = True
    for i in range(len(startEquations)):
        sumVar(startEquations[i],answerEquations[i])
        if not equateVar(startEquations[i], answerEquations[i]):
            result = False
    return result

print(run())