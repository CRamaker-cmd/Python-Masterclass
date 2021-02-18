available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "HDMI cable",
                   "dvd drive"
                   ]
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
current_choice = "-"
computer_part = []  # create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_part:
            computer_part.remove(chosen_part)
            print("Removing {}".format(chosen_part))
        else:
            computer_part.append(chosen_part)
            print("Adding {}".format(chosen_part))
        print("Your list now contains: {}".format(computer_part))
    else:
        print("Please add options from the list below: ")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print("Have fun with your computer consisting of: ")
print(computer_part)
