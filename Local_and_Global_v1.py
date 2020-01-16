#Global And Local Variables

def SetValue():
    global Score #Makes "Score" a global variable.
    Score = 5

######################

Score = 0

SetValue()
print(Score)
