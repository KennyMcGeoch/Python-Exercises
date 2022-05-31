def userName(): #asks for first and second name and returns full name
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your second name: ")
    fullName = firstName + " " + lastName
    return fullName
    
def menu(fullName): # asks for menu option and runs relevant function or asks again if invalid input is given
    print(f"Welcome to the Online Numbers Help {fullName}")
    print("Please select one of the following menu options:")
    print("Option 1: Display all the integers between any two integers (1-100) entered")
    print("Option 2: Work out and display the highest and lowest of five integers entered")
    print("Option 3: To exit the application")
    choice = input("Menu Option (1-3): ")
    if choice == "1":
        optionOne()
    elif choice == "2":
        optionTwo()
    elif choice == "3":
        print("You have successfully exited the program")
        return
    else:
        print(f"{fullName}, you must enter 1, 2 or 3. Any other input won't be accepted")
        menu(fullName)
    return

def optionOne(): #asks for 2 integer inputs, validates it to ensure it's an integer. The does comparison to see which is the biggest and loops while appending the value to the string. As it's a while loop and loop starts at value + 1 it means that for consecutive numbers it's an empty string so the length attribute can be used to catch that scenario. integersPresent variable is used to have a nicer output
    firstInt = input("Please enter the first integer: ")
    secondInt = input("Please enter the second integer: ")
    numbersList = ""
    integersPresent = False
    try:
        firstInt = int(firstInt)
        secondInt = int(secondInt)
    except ValueError:
        print("Please enter valid integers")
        optionOne()
        return
    
    if firstInt < 1 or firstInt > 100 or secondInt < 1 or secondInt > 100:
        print("You have entered an integer outside of the 1 to 100 range. Please try again")
        optionOne()
        return
    
    if firstInt > secondInt:
        secondIntCounter = secondInt
        secondIntCounter +=1
        while secondIntCounter < firstInt:
            numbersList = numbersList + " " + str(secondIntCounter)
            secondIntCounter +=1
            integersPresent = True
    elif secondInt > firstInt:
        firstIntCounter = firstInt
        firstIntCounter +=1
        while firstIntCounter < secondInt:
            numbersList = numbersList + " " + str(firstIntCounter)
            firstIntCounter +=1
            integersPresent = True
    elif firstInt == secondInt:
        print("There are no integers between the specified numbers as both numbers are the same.\n")
    elif len(numbersList) == 0:
        numbersList = "There are no integers between the specified numbers as numbers are consecutive.\n"
    if integersPresent == True:
        print(f"The list of numbers between {str(firstInt)} and {str(secondInt)} is as follows: {numbersList}\n")
    else:
        print(f"{numbersList}\n")
    menu(getName)
    return

def optionTwo(): #asks for 5 integers and inserts them into an array with error validation present. Then uses sort method to arrange them and displays output.
    print("We will now request you to enter 5 integers")
    i = 1
    numbers = []
    while i <= 5:
        try:
            numbers.append(int(input(f"Please enter integer number {i}: ")))
            i+=1
        except ValueError:
            print("You have an entered an invalid integer. Please re-enter the integers again")
            optionTwo()
            return
    sortedNumbers = sorted(numbers)
    print(f"The numbers given were {numbers}. Of these the highest number is {sortedNumbers[4]} and the lowest number is {sortedNumbers[0]}\n")
    menu(getName)
    return

getName = userName()
menu(getName)
