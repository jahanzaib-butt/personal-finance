
import random

target = random.randrange(1, 120)

while True:
    user = input("guess a number or quit:")

    if user in ["quit", "exit", "bye"]:
        print("Exiting. Goodbye!")
        break
    user_guess = int(user)
    if user_guess == target:
        print("congrats you guess the right number ")
        break
    elif user_guess > target:
        print(" your number is too big choose smaller one")
    elif user_guess < target:
        print(" your number is too small choose bigger one")

    else:
        print("try again next time")


print("---game over---")
