menu = ['Quit', 'Swimming', 'Clubbing', 'Sleep',
        'Train', 'Read', 'Eat', 'Shower', 'Netflix', 'Relax']
ValidInteger = False
while not ValidInteger:
    print("""1. Swimming
2. Clubbing
3. Sleep
4. Train
5. Read
6. Eat
7. Shower
8. Netflix
9. Relax
0. Quit
Please pick any of these options: """)

    choice = input()
    if choice.isnumeric:
        ValidInteger = True
        if ValidInteger:
            IntegerChoice = int(choice)
            if IntegerChoice not in range(0, 10):
                print("Please give me a valid option, 0-9")
                continue
            elif IntegerChoice != 0:
                print("Have fun with {}".format(menu[IntegerChoice]))
            elif IntegerChoice == 0:
                print("Goodbye")
                continue
    ValidInteger = False
    else:
        print("Please enter a number")
        continue

