import random


dice_faces = {
    1: (
        "-----\n"
        "|   |\n"
        "| o |\n"
        "|   |\n"
        "-----"
    ),
    2: (
        "-----\n"
        "|o  |\n"
        "|   |\n"
        "|  o|\n"
        "-----"
    ),
    3: (
        "-----\n"
        "|o  |\n"
        "| o |\n"
        "|  o|\n"
        "-----"
    ),
    4: (
        "-----\n"
        "|o o|\n"
        "|   |\n"
        "|o o|\n"
        "-----"
    ),
    5: (
        "-----\n"
        "|o o|\n"
        "| o |\n"
        "|o o|\n"
        "-----"
    ),
    6: (
        "-----\n"
        "|o o|\n"
        "|o o|\n"
        "|o o|\n"
        "-----"
    )
}

def generate_random_number():
    return random.randint(1,6)

while True:
    user_ask = input("Press Enter to roll the dice or type 'exit' : ")
    random_number = generate_random_number()

    if user_ask.lower() == "exit":
        break
    print(dice_faces[random_number])

    roll_again = input("Roll Again (Yes / No)? ")

    if roll_again.lower() == "yes":
        continue
    else:
        break


# print(dice_faces[6])