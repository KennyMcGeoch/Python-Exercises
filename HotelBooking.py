surname = input("What is your surname?")
singleRoom = input("How many single rooms would you like to book?")
doubleRoom = input("How many double rooms would you like to book?")
familyRoom = input("How many family rooms would you like to book?")
lengthOfStay = input("How many days would you like to stay?")
date = input("Please enter your arrival date: ")

try:
    singleRoom = int(singleRoom)
    doubleRoom = int(doubleRoom)
    familyRoom = int(familyRoom)
    lengthOfStay = int(lengthOfStay)
except ValueError:
        print("***Invalid Data Input***")
        print("Please enter whole numbers for the number of rooms and the length of your stay")
        sys.exit()

priceMultiplier = 0

numberOfRooms = singleRoom + doubleRoom + familyRoom

validRoom = False
validStay = False
if numberOfRooms >= 1 and numberOfRooms <= 4:
    validRoom = True

if lengthOfStay >= 1 and lengthOfStay <= 14:
    validStay = True

if validRoom == False:
    print("You must select from 1 to 4 rooms total to book")
elif validStay == False:
    print("We only accept booking of up to 14 days in length")
elif numberOfRooms >= 3 and lengthOfStay >= 7 and validRoom == True and validStay == True:
    priceMultiplier = 0.9
elif validRoom == True and validStay == True:
    priceMultiplier = 1.0
else:
    print("We only accept stays of between 1 and 14 days")
    
totalCost = (((singleRoom * 47) + (doubleRoom * 90) + (familyRoom * 250)) * priceMultiplier * lengthOfStay)

vat = (totalCost * 0.2)
finalTotalCost = "£{:,.2f}".format(totalCost + vat)

vat = "£{:,.2f}".format(vat)
totalCost = "£{:,.2f}".format(totalCost)

if priceMultiplier == 0.9:
    print("You qualified for a discount of 10%")
    
def printReceipt():
    print(f"Thank you Mr/Ms {surname}")
    print(f"You have requested {numberOfRooms} rooms for {lengthOfStay} days")
    print(f"You have requested {singleRoom} Single room(s)")
    print(f"You have requested {doubleRoom} Double room(s)")
    print(f"You have requested {familyRoom} Family room(s)")
    print(f"The total price will be {totalCost} plus {vat} VAT to give a grand total of {finalTotalCost} ")
    print(f"You will arrive on {date} ")
    
if priceMultiplier > 0:  
    printReceipt()
else:
    print("Sorry but we are unable to process your booking")
