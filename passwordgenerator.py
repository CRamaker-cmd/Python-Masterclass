import random
password = ""
numbers = "0123456789"
letters = "abcdefghijklmnopqsrtuvwxyz"
symbols = "!@#$%^&*"
upper = "ABCDEFGHIJKLMNOPQRSTUVWQYZ"
together = ""
print("1 for YES and 2 for NO")
if input("Do you want numbers in your password? ") == "1":
    together += numbers
    print("You've added numbers in your password")
else:
    print("No numbers will be added to your password")
if input("Do you want letters in your password? ") == "1":
    together += letters
    print("You've added letters in your password")
else:
    print("No letters will be added to your password")
if input("Do you want capital letters in your password? ") == "1":
    together += upper
    print("You've added capital letters in your password")
else:
    print("No capital letters will be added to your password")
if input("Do you want symbols in your password? ") == "1":
    together += symbols
    print("You've added symbols in your password")
else:
    print("No symbols will be added to your password")
GeneratorLength = len(together)
if GeneratorLength == 0:
    print("You haven't added anything to your password")
    exit()

try:
    PasswordLength = int(input("How many characters do you want in your password? "))
except ValueError:
    print("You have not used a number, ending program.")
    exit()
for x in range(0, PasswordLength):
    password += together[random.randint(0, GeneratorLength - 1)]
print(password)