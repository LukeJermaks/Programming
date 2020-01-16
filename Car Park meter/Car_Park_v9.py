#Car Park: version 9
#~~~Modules~~~#

import time

#~~~Global variables~~~#

TicketPrice = 8

#~~~Random Procedures~~~#

def delay(x):
    time.sleep(x)

#~~~Defined Procedures~~~#

def ShowTitle(TicketPrice):
    print("Luke's Car Park")
    print("Please insert £",TicketPrice,"for a ticket.\n")

def GetReg():
    Reg = input ("Enter your registration: ").upper()
    if len(Reg) > 8:
        print("Too many characters entered")
    return Reg

def GetMoney(TicketPrice):                          
    global Cash
    Cash = 0                                            #Create "Cash" variable
    while Cash < TicketPrice:                           #Loops until "Cash" is greater than or equal to "TicketPrice"
        Money = int(input("Please enter money "))       #Creates integer input for "Money"
        Cash = Money + Cash                             #Changes the value the variable "Cash"
    return Cash                                         #Returns the amount due    

def GiveChange(Cash, TicketPrice):                      #This is what calculates change due
    if Cash > TicketPrice:                              
        global Change
        Change =  Cash - TicketPrice                    
        print("Your change is £", Change)               #This is what prints change due
    else:
        print("There is no change due.")
               
def PrintTicket(TicketPrice, Reg):
    print("Printing Your Ticket...")
    print("#########################")
    print("     Luke's Car Park     ")
    print("#########################")  
    time.sleep(1)                                       #Delays code by 1 second
    print(" Registration: ", Reg, "     ")              #Prints fee paid
    print("#########################")
    time.sleep(1)                                       #Delays code by 1 second
    print("     Fee Paid: £", TicketPrice, "     ")     #Prints fee paid
    print("#########################")
    time.sleep(1)                                       #Delays code by 1 second
    print("    Change Due: £", Change, "    ")          #Prints change due
    print("#########################")
    
def SaveDate():
    print("Saving Data")
    file = open ("DataLog.txt", "a")

    OutputData = Reg + ", " + str(TicketPrice) + "\n"

    file.write(OutputData)

    file.close

def Spacer():
    print("\n")
    print("#"*60)
    print("\n")

############################################################################################################################################################
###################################Above here is where the procedures are defined and below is where they are called upon###################################
############################################################################################################################################################

while True:
    ShowTitle(TicketPrice)          #Need to send the global variable up to the procedure

    Reg = GetReg() 

    GetMoney(TicketPrice)

    GiveChange(Cash, TicketPrice)   #Could also make the variable "Cash" equal to get money so that you could print what the due change is if any   
                                    #Has to be set in the same order as the procedure
    PrintTicket(TicketPrice, Reg)

    SaveDate()                      #Calls on precedures

    Spacer()
