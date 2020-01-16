#Loop thing I guess.
#By Luke Jermaks

def NestedLoop():
    score = int(input("Input Score\n  >>>"))

    if score > 89:                              #Needs to be > 89 due to the grade being only over 90 for a grade 9
        print("Grade 9")                        #You could also use => or =< and then the lower bound of the grade

    elif score > 79:
        print("Grade 8")

    elif score > 69:
        print("Grade 7")

    elif score > 59:
        print("Grade 6")

    elif score > 49:
        print("Grade 5")

    elif score > 39:
        print("Grade 4")

    elif score > 29:
        print("Grade 3")

    elif score > 19:
        print("Grade 2")

    elif score > 9:
        print("Grade 1")
    
    else:
        print("Ungraded")

def Spacer():

    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    
    
while True:

    NestedLoop()

    Spacer()
