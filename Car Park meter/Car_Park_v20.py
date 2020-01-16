#Car Park: version 20

#~~~Modules~~~#

import time

#~~~Global variables~~~#

TicketPrice = 8

EngineerCode = '1234'



#~~~Random Procedures~~~#

def s(x):
    time.sleep(x)

#~~~Defined Procedures~~~#

def ShowTitle(TicketPrice):
    print("Luke's Car Park")
    print("Please insert £",TicketPrice,"for a ticket.\n")

def GetReg():
    Reg = input("Enter your registration: ").upper()
    if len(Reg) > 8:
        while len(Reg) <= 7:
            print("Too many characters entered")
    return Reg

def EngineerMode():
    print ("Engineer Mode")
    s(0.3)
    
    DataBase = LoadData()
    
    print("Which report would you like?\n")
    s(0.3)
    print("Registration report or Summary report? (R or S)")
    s(0.3)
    Choice = input(">>> ").upper()[0]
    
    #The line above creates the input variable "Choice" and makes it upper case at the first letter.

    if Choice == "R":
        time.sleep(0.5)
        RegistrationReport(DataBase)

    if Choice == "S":
        time.sleep(0.5)
        SummaryReport(DataBase)

def IsEngineer(Reg, EngineerCode):
    return Reg == EngineerCode

#Saved code for car park program
def RegistrationReport(DataBase):
    print("Registration Report ")                       #Only act as "print" statement
    s(0.25)
    
    Part = input("Enter part of the registration to find: ").upper()
    s(0.4)

    print("\nRegistration         Price of Ticket\n")
    
    for Record in DataBase:                             #For loop
        Registration = Record[0]
        if Part in Registration:                        #Searches for a character in the "Record"
            print(Record[0].ljust(26), Record[1])       #Prints the record. ".ljust(15)" moves "Record[0]" over to the left and creates a 15 space gap between it and "Record[1]"      

def SummaryReport(DataBase):
    print("Summary Report ")                            #Only act as "print" statement

    TotalCars =0
    Income = 0
    
    for Record in DataBase:                             #For loop for the DataBase Record
        print(Record)
  
        TotalCars = TotalCars + 1                       #Once the for loop checks if the record in the Database, it adds to a total car amount (each reg has a car with it...)
        Income = Income + int(Record[1])
                                     
    print("The total amount of cars is: ", TotalCars)
    print("The total amount of income is: £", Income)

def LoadData():

    DataBase = []                                       #Creates 2D database
        
    print("Loading data...")
    File = open("DataLog.txt","r")                      #Opens DataLog file
    Line = File.readline().rstrip()                     #Reads the first line. "rstrip" strips away new line

    while Line != "":                                   #Prints 
        Reg,TicketPrice = Line.split(",")
        Record = []                                     #Creates a list for varaibles to be entered in
                                          
        Record.append(Reg)                              #A line of Record.append() is needed for each variable that you want to show up
        Record.append(TicketPrice)                      
        """Record.append(Change)"""                           

        DataBase.append(Record)
        
        Line = File.readline().rstrip()                 #Duplicates to check line under empty line
    
    File.close()                                        #Closes Line
    return DataBase
    
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
    
    
def SaveDate(Reg, TicketPrice):
    print("Saving Data")
    File = open ("DataLog.txt", "a")

    OutputData = Reg + "," + str(TicketPrice) + "\n"

    File.write(OutputData)

    File.close

def Spacer():
    print("\n")
    print("#"*60)
    print("\n")

############################################################################################################################################################
###################################Above here is where the procedures are defined and below is where they are called upon###################################
############################################################################################################################################################

while True:
    ShowTitle(TicketPrice)                      #Need to send the global variable up to the procedure

    s(0.2)
    
    Reg = GetReg()

    if IsEngineer(Reg, EngineerCode):	

        EngineerMode()

    else:
        
        GetMoney(TicketPrice)

        GiveChange(Cash, TicketPrice)           #Could also make the variable "Cash" equal to get money so that you could print what the due change is if any   
                                                #Has to be set in the same order as the procedure
        PrintTicket(TicketPrice, Reg)

        SaveDate(Reg, TicketPrice)              #Calls on precedures

    s(0.25)
    Spacer()
    time.sleep(0.5)

