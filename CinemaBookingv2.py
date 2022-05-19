tickets = input("How many tickets for your family do you require? ")
ages = []

def printOut(adults, teenagers, children, total):
    print("Thank You")
    print("TICKET PRICE DETAILS are as follows:")
    print(f"Number of Adults = {adults} at £14.50 each")
    print(f"Number of Teenagers = {teenagers} at £10.00 each")
    print(f"Number of Childrens = {children} at £5.00 each")
    total = "£{:,.2f}".format(total)
    print(f"The total cost of these tickets are {total}")
    return

def errorMsgFunc(error):
    print(error)
    print("Your order has been cancelled. Please restart your order ensuring that all data entered is valid")
    return

def priceCalc(ages):
    adults = 0
    teenagers = 0
    children = 0
    total = 0
    for x in ages:
        if x > 19:
            adults +=1
            total += 14.5
        elif x > 10:
            teenagers +=1
            total += 10
        else:
            children +=1
            total += 5
    printOut(adults, teenagers, children, total)
    return
    
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
        priceCalc(ages)
        return
    elif noBabies == False:
        errorMsgFunc("We cannot process you order as the party contains a child under the age of 2")
        return
    else:
        errorMsgFunc("We cannot process your order as the party has no accompanying adult")
        return 

def checkTicketNumbers(tickets):
    try:
        tickets = int(tickets)
    except ValueError:
        errorMsgFunc("You have entered an invalid number of tickets. All tickets must be a whole number")
        return
    else:
        if tickets > 5 or tickets < 2:
            errorMsgFunc("You can only book 2 to 5 tickets. Please enter a number within that range")
            return 
        else:
            getInputs(tickets)
            return
        
def getInputs(ticketsValidated):
    print("Please enter the ages for each ticket")
    i = 1
    while i <= ticketsValidated:
        try:
            ages.append(int(input(f"What age is the family member for ticket {i}: ")))
            i+=1
        except ValueError:
            errorMsgFunc("You have entered an invalid age. All ages must be a whole number")
            return
        
    ageVerification(ages)
    return
        
checkTicketNumbers(tickets)
