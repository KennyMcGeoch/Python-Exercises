surname = input("What is your surname?")
singleRoom = int(input("How many single rooms would you like to book?"))
doubleRoom = int(input("How many double rooms would you like to book?"))
familyRoom = int(input("How many family rooms would you like to book?"))
lengthOfStay = int(input("How many days would you like to stay?"))
date = input("Please enter your arrival date: ")

priceMultiplier = 0

numberOfRooms = singleRoom + doubleRoom + familyRoom

if numberOfRooms > 4:
    print("We only have a maximum of 4 rooms available")
elif numberOfRooms < 1:
    print("You haven't requested any rooms")
elif numberOfRooms >= 3 and lengthOfStay >= 7 and lengthOfStay <= 14:
    priceMultiplier = 0.9
elif numberOfRooms <= 4 and numberOfRooms > 0 and lengthOfStay > 0 and lengthOfStay <= 14:
    priceMultiplier = 1.0
else:
    print("We only accept stays of between 1 and 14 days")

   
    
totalCost = ((singleRoom * 47) + (doubleRoom * 90) + (familyRoom * 250)) * priceMultiplier * lengthOfStay

if priceMultiplier == 0.9:
    print("You qualified for a discount of 10%")
    
def printReceipt():
    print(f"Thank you Mr/Ms {surname}")
    print(f"You have requested {numberOfRooms} rooms for {lengthOfStay} days")
    print(f"You have requested {singleRoom} Single room(s)")
    print(f"You have requested {doubleRoom} Double room(s)")
    print(f"You have requested {familyRoom} Family room(s)")
    print(f"The total price will be {totalCost} ")
    print(f"You will arrive on {date} ")
    
if priceMultiplier > 0:  
    printReceipt()
else:
    print("Sorry but we are unable to process your booking")