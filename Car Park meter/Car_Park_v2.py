#Car Park: version 2

#~~~Global variables~~~#

TicketPrice = 8

#~~~Defined Procedures~~~#

def ShowTitle(TicketPrice):
    print("Luke's Car Park")
    print("Please insert £", TicketPrice, " for a ticket.")
    print()

def GetMoney():
    cash = input("Please enter money ")

def GiveChange():
    print("Your change is ")

def PrintTicket():
    print("Printing Your Ticket ")

def SaveDate():
    print("Saving Data ")

############################################################################################################################################################
###################################Above here is where the procedures are defined and below is where they are called upon###################################
############################################################################################################################################################

ShowTitle(TicketPrice)

GetMoney()

GiveChange()

PrintTicket()

SaveDate()          #Calls on precedures
