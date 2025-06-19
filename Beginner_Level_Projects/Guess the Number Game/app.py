import random

def generate_random_number():
    return random.randint(1,10)

random_number = generate_random_number()
attempt = 0
user_guess_num = 0

while user_guess_num != random_number:
    user_guess_num = int(input("Guess the Number between 1 - 10 : "))
    attempt += 1

    if user_guess_num > random_number:
        print("You can guess its too high")
    elif user_guess_num < random_number:
        print("You can guess its too low")
    else:
        print("Congrates You can guess the correct Number")

    print(f"your {attempt} Attempt")

    if user_guess_num == random_number:
        again_play = input("Can you play again (Yes / No)? ")
        if again_play.lower() == "yes":
            random_number = generate_random_number()
        else:
            print("\n Thank You For Play The Number Guessing Game \n")
            break


