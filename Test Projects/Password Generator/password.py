import random

lowercase_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols_list = ["!", "#", "$", "%", "&", "(", ")", "*", "+", "@"]

def LowerCaseLetters():
    return random.sample(lowercase_list, int(character_count) - int(uppercase_count) - int(number_count) - int(symbol_count))

def UpperCaseLetters():
     return random.sample(uppercase_list, int(uppercase_count))

def Numbers():
    return random.sample(numbers_list, int(number_count))

def Symbols():
    return random.sample(symbols_list, int(symbol_count))

print("How many passwords would you like to generate?")
password_count = input()

password_amount = 1

while True:
    print("How many characters do you want your password to be? (Min. 8)")
    character_count = input()
    if character_count.isdigit() == False or int(character_count) < 8:
        print("Your input is incorrect, please try again:")
        continue
    else:
        break

while True:
    print("How many uppercase letters do you want to use in your password (Min. 1)")
    uppercase_count = input()
    if uppercase_count.isdigit() == False or int(uppercase_count) < 1:
        print("Your input is incorrect, please try again:")
        continue
    else:
        break

while True:
    print("How many digits do you want to use in your password (Min. 1)")
    number_count = input()
    if number_count.isdigit() == False or int(number_count) < 1:
        print("Your input is incorrect, please try again:")
        continue
    else:
        break

while True:
    print("How many symbols do you want to use in your password (Min. 1)")
    symbol_count = input()
    if symbol_count.isdigit() == False or int(symbol_count) < 1:
        print("Your input is incorrect, please try again:")
        continue
    else:
        break

print("Your generated passwords:\n")
while password_amount <= int(password_count) :
    password_combined = LowerCaseLetters() + UpperCaseLetters() + Numbers() + Symbols()
    random.shuffle(password_combined)
    print("".join(password_combined))
    password_amount += 1
