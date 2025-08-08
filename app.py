from flask import Flask, render_template, request
import random

app = Flask(__name__)

# トップページ
@app.route('/')
def index():
    return render_template('index.html')

# たし算ページ（問題表示）
@app.route('/addition')
def addition():
    problems = []
    for _ in range(10):
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        problems.append({'a': a, 'b': b})
    return render_template('addition.html', problems=problems)

# 採点処理
@app.route('/addition_results', methods=['POST'])
def addition_results():
    results = []
    score = 0
    for i in range(10):
        a = int(request.form[f'a{i}'])
        b = int(request.form[f'b{i}'])
        correct_answer = a + b
        user_answer = request.form.get(f'answer{i}', '')
        try:
            user_answer_int = int(user_answer)
            is_correct = (user_answer_int == correct_answer)
        except:
            is_correct = False

        if is_correct:
            score += 1

        results.append({
            'a': a,
            'b': b,
            'user_answer': user_answer,
            'correct_answer': correct_answer,
            'is_correct': is_correct
        })

    return render_template('addition_results.html', results=results, score=score)

if __name__ == '__main__':
    app.run(debug=True)
