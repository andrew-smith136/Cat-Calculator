while True:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter a number: "))
    
    choice = input ("1. Add 2. Subtract 3. Multiply 4. Divide: ")

    if choice == '1':
        result = number1 + number2
        print(result)
    elif choice == '2':
        result = number1 - number2
        print(result)
    elif choice == '3':
        result = number1 * number2
        print(result)
    elif choice == '4':
        result = number1 / number2
        print(result)
    else:
        print('Not a valid choice, please try again.')