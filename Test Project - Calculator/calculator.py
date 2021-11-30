import math

while True:
    print("\nChoose the math operation:\n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 - Square Root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n")

    option = input("\nYour option from the menu:")

    if option == "0":
            value1 = float(input("\nFirst value: "))
            value2 = float(input("\nSecond value: "))

            print("\nThe result is: " + str(value1 + value2) + "\n")

            back = input('\nGo back to the main menu? (y/n) ')

            if back == 'y':
                continue
            else:
                break

    elif option == "1":
            value1 = float(input("\nFirst value: "))
            value2 = float(input("\nSecond value: "))

            print("\nThe result is: " + str(value1 - value2) + "\n")

            back = input('\nGo back to the main menu? (y/n) ')

            if back == 'y':
                continue
            else:
                break

    elif option == "2":
            value1 = float(input("\nFirst value: "))
            value2 = float(input("\nSecond value: "))

            print("\nThe result is: " + str(value1 * value2) + "\n")

            back = input('\nGo back to the main menu? (y/n) ')

            if back == 'y':
                continue
            else:
                break

    elif option == "3":
            value1 = float(input("\nFirst value: "))
            value2 = float(input("\nSecond value: "))

            print("\nThe result is: " + str(value1 / value2) + "\n")

            back = input('\nGo back to the main menu? (y/n) ')

            if back == 'y':
                continue
            else:
                break

    elif option == "4":
            value1 = float(input("\nFirst value: "))
            value2 = float(input("\nSecond value: "))

            print("\nThe result is: " + str(value1 % value2) + "\n")

            back = input('\nGo back to the main menu? (y/n) ')

            if back == 'y':
                continue
            else:
                break

    elif option == "5":
            value1 = float(input("\nFirst value: "))
            value2 = float(input("\nSecond value: "))

            print("\nThe result is: " + str(math.pow(value1, value2)) + "\n")

            back = input('\nGo back to the main menu? (y/n) ')

            if back == 'y':
                continue
            else:
                break

    elif option == "6":
            value1 = float(input("\nEnter the value for extracting the square root: "))

            print("\nThe result is: " + str(math.sqrt(value1)) + "\n")

            back = input('\nGo back to the main menu? (y/n) ')

            if back == 'y':
                continue
            else:
                break

    elif option == "7":
            value1 = float(input("\nEnter the value for calculating the logartithm to base 2: "))

            print("\nThe result is: " + str(math.log(value1, 2)) + "\n")

            back = input('\nGo back to the main menu? (y/n) ')

            if back == 'y':
                continue
            else:
                break

    elif option == "8":
            value1 = float(input("\nEnter the value (in degrees) for calculating the sine: "))

            print("\nThe result is: " + str(math.sin(math.radians(value1))) + "\n")

            back = input('\nGo back to the main menu? (y/n) ')

            if back == 'y':
                continue
            else:
                break

    elif option == "9":
            value1 = float(input("\nEnter the value (in degrees) for calculating the cosine: "))

            print("\nThe result is: " + str(math.cos(math.radians(value1))) + "\n")

            back = input('\nGo back to the main menu? (y/n) ')

            if back == 'y':
                continue
            else:
                break

    elif option == "10":
            value1 = float(input("\nEnter the value (in degrees) for calculating the tangent: "))

            print("\nThe result is: " + str(math.tan(math.radians(value1))) + "\n")

            back = input('\nGo back to the main menu? (y/n) ')

            if back == 'y':
                continue
            else:
                break

    else:
        print("Invalid option\n")
        continue
