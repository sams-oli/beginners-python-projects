import random

correct_number = random.randrange(101)

print(correct_number)

user_number = int(input("Please enter an integer number: \n"))

for i in range(0, 5):
    if user_number == correct_number:
        print("Correct! Congratulations")
        break
    elif user_number != correct_number and i == 4:
        print("Your odds are over. The number was", correct_number)
    elif correct_number < user_number:
        user_number = int(input("A little bit less. Try again \n"))
    elif correct_number > user_number:
        user_number = int(input("A little bit more. Try again \n"))
    pass
