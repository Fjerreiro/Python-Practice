print("Welcome to the binary number converter. Please pick an option from below:\n\n1. Binary to decimal numbers\n2. Decimal to binary numbers.\n3. Quit the program.")

while True:
    print("\nPlease type 1, 2 or 3 to pick from the menu:")
    option = input()

    if option == "1":
        print("\nPlease enter the binary number:")
        binary = input()
        print("\nThe binary value of", binary, "is", int("0b" + binary, 2), "in decimals.\n")

    elif option == "2":
        print("\nPlease enter the decimal number:")
        decimal = input()
        print("\nThe decimal value of", decimal, "is", bin(int(decimal))[2:], "in binary\n")

    elif option == "3":
        print("Quitting the program!")
        break

    else:
        print("This is not a valid choice. Please enter either 1, 2 or 3.")
        continue
