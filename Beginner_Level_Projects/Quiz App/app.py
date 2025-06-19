
print("\n ------ Welcome To Quiz App ------")

def quiz_app():
    quiz = [
        {
            "question":"1. What is the capital of Australia?",
            "option_1":"A) Sydney",
            "option_2":"B) Melbourne",
            "option_3":"C) Canberra",
            "option_4":"D) Brisbane",
            "answer":"C"
        },
        {
            "question":"2. Who wrote the play Romeo and Juliet?",
            "option_1":"A) William Wordsworth",
            "option_2":"B) William Shakespeare",
            "option_3":"C) Charles Dickens",
            "option_4":"D) Jane Austen",
            "answer":"B"
        },
        {
            "question":"3. What is the largest planet in our Solar System?",
            "option_1":"A) Earth",
            "option_2":"B) Jupiter",
            "option_3":"C) Saturn",
            "option_4":"D) Mars",
            "answer":"B"
        },
        {
            "question":"4. Which element has the chemical symbol 'O'?",
            "option_1":"A) Gold",
            "option_2":"B) Oxygen",
            "option_3":"C) Osmium",
            "option_4":"D) Ozone",
            "answer":"B"
        },
        {
            "question":"5. In which country is the Great Pyramid of Giza located?",
            "option_1":"A) Mexico",
            "option_2":"B) Peru",
            "option_3":"C) Egypt",
            "option_4":"D) India",
            "answer":"C"
        }
    ]
    score = 0

    for items in quiz:
        print()
        print(items["question"])
        print(items["option_1"])
        print(items["option_2"])
        print(items["option_3"])
        print(items["option_4"])
        print()

        answer = input("Enter Answer in key: ")

        if answer.lower() == items["answer"].lower():
            score += 1
    print(f"\nYour Score is {len(quiz)}/{score}\n")

    
quiz_app()
