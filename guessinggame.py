import random

i = 0
highest = 50
answer = random.randint(1, highest)
guess = 0

print(answer)  # TODO: Remove after testing

print("To quit the game, enter 0 as an answer")

print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())
    i += 1
    if guess == answer:
        if i == 1:
            print("well done, you've guessed it first try.")
        else:
            print("You've guessed correctly, and it took you {} guesses!".format(i))
    elif guess == 0:
        print("Better luck next time.")
        break
    elif guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")



# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")