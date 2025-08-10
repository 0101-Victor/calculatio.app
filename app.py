from flask import Flask, render_template, request
from calculate import generate_addition_problems

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addition', methods=['GET', 'POST'])
def addition():
    if request.method == 'POST':
        results = []
        score = 0
        total = 5
        for i in range(total):
            num1 = int(request.form[f'num1_{i}'])
            num2 = int(request.form[f'num2_{i}'])
            correct_answer = num1 + num2
            user_answer = int(request.form[f'answer{i}'])
            is_correct = (user_answer == correct_answer)
            if is_correct:
                score += 1
            results.append({
                "problem": f"{num1} + {num2}",
                "user_answer": user_answer,
                "correct_answer": correct_answer,
                "is_correct": is_correct
            })
        return render_template('addition.html', results=results, score=score, total=total)
    else:
        problems = generate_addition_problems()
        return render_template('addition.html', problems=problems)

if __name__ == '__main__':
    app.run(debug=True)
