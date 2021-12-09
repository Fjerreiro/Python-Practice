while True:
    user_value = input("\nEnter a word to see if it's a palindrome: ")
    if user_value == user_value[::-1]:
        print("This is a palindrome!")
        again = input("\nDo you want to check another word? y/n: ")
        if again == "y":
            continue
        else:
            break
    else:
        print("This is not a palindrome...")
        again = input("\nDo you want to check another word? y/n: ")
        if again == "y":
            continue
        else:
            break
