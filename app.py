# app.py

from flask import Flask, render_template, request
from calculatio import generate_addition_problems

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addition', methods=['GET', 'POST'])
def addition():
    if request.method == 'POST':
        problems = eval(request.form['problems'])  # 文字列 → リストに変換（安全性は後で改善可）
        score = 0
        results = []

        for i, p in enumerate(problems):
            user_answer = request.form.get(f'answer_{i}')
            correct = str(p['answer']) == user_answer.strip()
            results.append({
                "question": f"{p['a']} + {p['b']}",
                "user": user_answer,
                "correct": correct,
                "answer": p['answer']
            })
            if correct:
                score += 1

        return render_template('addition_result.html', results=results, score=score, total=len(problems))

    problems = generate_addition_problems()
    return render_template('addition.html', problems=problems)

if __name__ == '__main__':
    app.run(debug=True)
