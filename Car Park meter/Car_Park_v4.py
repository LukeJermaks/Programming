#Car Park: version 4

#~~~Global variables~~~#

TicketPrice = 8
cash = 0

#~~~Defined Procedures~~~#

def ShowTitle(TicketPrice):
    print("Luke's Car Park")
    print("Please insert £", TicketPrice, " for a ticket.\n")

def GetMoney(TicketPrice):
    Cash = 0                                            #Create "Cash" variable
    while Cash<TicketPrice:                             #Loops until "Cash" is greater than or equal to "TicketPrice"
        Money = int(input("Please enter money "))       #Creates integer input for "Money"
        Cash = Money + Cash                             #Changes the value the variable "Cash"
        
def GiveChange():
    print("Your change is ")

def PrintTicket():
    print("Printing Your Ticket ")

def SaveDate():
    print("Saving Data ")

############################################################################################################################################################
###################################Above here is where the procedures are defined and below is where they are called upon###################################
############################################################################################################################################################


ShowTitle(TicketPrice)          #Need to send the global variable up to the procedure

GetMoney(TicketPrice)

GiveChange()

PrintTicket()

SaveDate()                      #Calls on precedures
