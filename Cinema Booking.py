tickets = input("How many tickets for your family do you require?")
print("Please enter the ages for each ticket")

def checkTicketNumbers(tickets):
    try:
        tickets = int(tickets)
    except ValueError:
        print("***Invalid Data Input***")
        print("You must enter digits like 2 or 3")
        return 0
    if tickets > 5 or tickets < 2:
        print("You can only book 2 to 5 tickets and number")
        return 0
    else:
        return tickets

ticketsValidated = checkTicketNumbers(tickets)

ages = []

i = 1
while i <= ticketsValidated:
    try:
        ages.append(int(input(f"What age is the family member for ticket {i}: ")))
        i+=1
    except ValueError:
        ticketsValidated = 0

def ageVerification(ages):
    noBabies = True
    accompanyingAdults = False
    for x in ages:
        if x < 2:
            noBabies = False
            break
        if x > 19:
            accompanyingAdults = True
            
    if accompanyingAdults and noBabies:
        return True
    else:
        return False

ageValid = ageVerification(ages)            
        

def priceCalc(ages):
    if ageValid == False:
        return [0,0,0,0]
    Adults = 0
    Teenagers = 0
    Children = 0
    Total = 0
    for x in ages:
        if x > 19:
            Adults +=1
            Total += 14.5
        elif x > 10:
            Teenagers +=1
            Total += 10
        else:
            Children +=1
            Total += 5
    return [Adults, Teenagers, Children, Total] 

infoArray = priceCalc(ages)
totalCost = "£{:,.2f}".format(infoArray[3])

def printOut():
    if ticketsValidated == 0:
        print("Sorry, the order could not be processed as the input was invalid")
        return
    elif ageValid != True:
        print("Sorry, we cannot process orders that contain a baby or that don't have an accompanying adult so your order could not be processed")
        return
    else:
        print("Thank You")
        print("TICKET PRICE DETAILS are as follows:")
        print(f"Number of Adults = {infoArray[0]} at £14.50 each")
        print(f"Number of Teenagers = {infoArray[1]} at £10.00 each")
        print(f"Number of Childrens = {infoArray[2]} at £5.00 each")
        print(f"The total cost of these tickets are {totalCost}")
        return

printOut()
