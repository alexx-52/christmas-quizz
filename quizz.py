import random

# Questions about Latvia
questions = [
    # Burovs Rodions
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Daņilovs Roberts
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Dmitrijevs Kirils
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Jevstifejevs Vladislavs
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Kisļaks Kirills
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Korsaks Edvīns
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Kozinda Dmitrijs
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Nosovs Artjoms
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Rudņevs Dmitrijs
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Savostijanova Jelizaveta
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Silickis Marks
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Zaicevs Daņila
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Adadurova Anastasija
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Bogdanovs Ņikita
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Grigorenko Artjoms
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Mahajevs Maksims
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Mieriņs Aleksandrs
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Pavlova Anastasija
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Roguļskis Aleksandrs
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Švecs Kristians
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Vasiļjeva Anastasija
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
    # Vinčenko Nikita
    {
        "question": "",
        "options": ["a", "b", "c", "d"],
        "correct_answer": "a"
    },
]

def run_quiz():
    # Shuffle the questions
    random.shuffle(questions)

    # Initialize score
    score = 0

    # Iterate through questions
    for i, question_data in enumerate(questions, 1):
        if question_data['question'] == "":
          continue

        print(f"Jautājums {i}: {question_data['question']}")
        for j, option in enumerate(question_data['options'], 1):
            print(f"  {j}. {option}")

        # Get user input
        user_answer = input("Atbilde (ieraksti varianta numuru): ")

        # Check if the answer is correct
        correct_answer = question_data['options'].index(question_data['correct_answer']) + 1
        if user_answer == str(correct_answer):
            print("Pareizi!\n")
            score += 1
        else:
            print(f"Kļūda! Pareizā atbilde ir {correct_answer}: {question_data['correct_answer']}\n")

    # Display final score
    print(f"Gala rezultāts: {score}/{len(questions)}")

# Run the quiz
run_quiz()
