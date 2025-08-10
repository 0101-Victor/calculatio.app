import random

def generate_addition_problems():
    problems = []
    for _ in range(5):  # 5問
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        problems.append((num1, num2))
    return problems
