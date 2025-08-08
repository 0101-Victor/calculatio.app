from flask import Flask, render_template, request, redirect, session, url_for
from problems import generate_addition_problems

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # セッション用

@app.route('/')
def index():
    session['stage'] = 1
    session['round'] = 0
    return render_template('index.html')

@app.route('/addition', methods=['GET', 'POST'])
def addition():
    if 'stage' not in session:
        session['stage'] = 1
    if 'round' not in session:
        session['round'] = 0

    if request.method == 'POST':
        problems = json.loads(request.form['problems'])
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

        session['round'] += 1
        is_last_round = session['round'] >= 5

        if is_last_round:
            session['stage'] += 1
            session['round'] = 0  # 次ステージに移行

        return render_template(
            'addition_result.html',
            results=results,
            score=score,
            total=len(problems),
            is_last_round=is_last_round
        )

    problems = generate_addition_problems(stage=session['stage'])
    return render_template('addition.html', problems=problems)

if __name__ == '__main__':
    app.run(debug=True)