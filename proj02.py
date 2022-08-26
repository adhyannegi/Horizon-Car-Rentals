##########################################################################
#    Computer Project #2
#    Algorithm
#        Prompt to ask the user if they want to continue.
#        Prompt the user to input information about the rented vehicle.
#        Compute amount of money based on the player's classification code.
#        Display summary with all the information.
#           
##########################################################################

#importing math module
import math

#printing welcome message
print("\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)" )

#Prompt to ask the user if they want to continue
answer = input('\nWould you like to continue (A/B)? ')

#If they want to continue
while answer == "A":
    code = input("\nCustomer code (BD, D, W): ")
    
    #If code is invalid
    while (code != "BD" and code != "D" and code != "W"):
        print("\n\t*** Invalid customer code. Try again. ***")
        code = input("\nCustomer code (BD, D, W): ")
    
    days = int(input("\nNumber of days: "))
    start = int(input("Odometer reading at the start: "))
    end = int(input("Odometer reading at the end:   "))

    #Calulating miles    
    if end < start:
        miles = ((1000000 - start) + end)/10
    else:
        miles = (end - start)/10

    #Calculating base charge and mileage charge based on code input
    if code == "BD":
        base_charge = 40 * days
        mileage_charge = 0.25 * miles

    elif code == "D":    
        base_charge = 60 * days
        if miles/days <= 100:
            mileage_charge = 0
        else:
            mileage_charge = 0.25 * days * ((miles/days) - 100)
    
    else:
        week = math.ceil(days/7)
        base_charge = 190 * week
        if miles/week <= 900:
            mileage_charge = 0
        elif 900 < miles/week <= 1500:
            mileage_charge = 100 * week
        else:
            mileage_charge = (200 * week) + 0.25 * week * ((miles/week) - 1500)

    #Calculating total amount
    amount = round((float(base_charge + mileage_charge)),2)

    #Display summary with all the information.
    print("\nCustomer summary:")
    print("\tclassification code:", code)
    print("\trental period (days):", days)
    print("\todometer reading at start:", start)
    print("\todometer reading at end:  ", end)
    print("\tnumber of miles driven: ", miles)
    print("\tamount due: $", amount)

    #Prompt to ask the user if they still want to continue
    answer = input('\nWould you like to continue (A/B)? ')

#Thank you message
print("Thank you for your loyalty.")













