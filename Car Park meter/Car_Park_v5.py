#Car Park: version 5

#~~~Global variables~~~#

TicketPrice = 8

#~~~Defined Procedures~~~#

def ShowTitle(TicketPrice):
    print("Luke's Car Park")
    print("Please insert £",TicketPrice,"for a ticket.\n")

def GetMoney(TicketPrice):                          
    global Cash
    Cash = 0                                            #Create "Cash" variable
    while Cash < TicketPrice:                           #Loops until "Cash" is greater than or equal to "TicketPrice"
        Money = int(input("Please enter money "))       #Creates integer input for "Money"
        Cash = Money + Cash                             #Changes the value the variable "Cash"
    return Cash                                         #Returns the amount due    

def GiveChange(Cash, TicketPrice):
    if Cash > TicketPrice:
        Change =  Cash - TicketPrice
        print("Your change is £", Change)
    else:
        print("There is no change due.")
               
def PrintTicket():
    print("Printing Your Ticket ")

def SaveDate():
    print("Saving Data ")

############################################################################################################################################################
###################################Above here is where the procedures are defined and below is where they are called upon###################################
############################################################################################################################################################


ShowTitle(TicketPrice)          #Need to send the global variable up to the procedure

GetMoney(TicketPrice)

GiveChange(Cash, TicketPrice)   #Could also make the variable "Cash" equal to get money so that you could print  

PrintTicket()

SaveDate()                      #Calls on precedures
