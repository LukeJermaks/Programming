#Global And Local Variables

def SetValue():
    global Score #Makes "Score" a global variable. Only needs "global Score" because it isn't set at the top!
    Score = 5

######################

Score = 0

SetValue()
print(Score)
