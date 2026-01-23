questions = [
{
"question": "What is the capital of India?",
"options": ["A. Chennai", "B. Mumbai", "C. Delhi", "D. Kolkata"],
"answer": "C"
},
{
"question": "Which language is used for web development?",
"options": ["A. Python", "B. HTML", "C. Java", "D. All of the above"],
"answer": "D"
},
{
"question": "What does RAM stand for?",
"options": ["A. Read Only Memory", "B. Random Access Memory",
"C. Computer Processing Unit", "D. Control Processing Unit"],
"answer": "B"
}
]
score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nQuiz Completed!")
print("Your Score:", score, "/", len(questions))