from flask import Flask, request, jsonify

app = Flask(__name__)

questions = [
    {
        "id": 1,
        "question": "What is the capital of India?",
        "options": ["A. Chennai", "B. Mumbai", "C. Delhi", "D. Kolkata"],
        "answer": "C"
    },
    {
        "id": 2,
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. Java", "D. All of the above"],
        "answer": "D"
    },
    {
        "id": 3,
        "question": "What does RAM stand for?",
        "options": ["A. Read Only Memory", "B. Random Access Memory",
        "C. Computer Processing Unit", "D. Control Processing Unit"],
        "answer": "B"
    }
]

@app.route("/questions", methods=["GET"])
def get_questions():
    return jsonify(questions)

@app.route("/submit", methods=["POST"])
def submit_quiz():
    user_answers = request.get_json()
    score = 0

    for i, q in enumerate(questions):
        if user_answers.get(str(q["id"])) == q["answer"]:
            score += 1

    return jsonify({
        "score": score,
        "total": len(questions)
    })

if __name__ == "__main__":
    app.run(debug=True)
