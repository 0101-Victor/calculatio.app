# calculatio.py

import random

def generate_addition_problems(n=10):
    problems = []
    for _ in range(n):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        problems.append({"a": a, "b": b, "operator": "+", "answer": a + b})
    return problems
