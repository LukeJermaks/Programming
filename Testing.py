#Testing stuff ting

import time

def s(x):
    time.sleep(x)

print("Hiya love!")
s(1)
print("Hiya again love!")







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



