import random

def generate_addition_problems():
    problems = []
    for _ in range(5):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        problems.append((num1, num2))
    return problems

def generate_subtraction_problems():
    problems = []
    for _ in range(5):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, num1)  # num2 <= num1にしてマイナス防止
        problems.append((num1, num2))
    return problems

def generate_multiplication_problems():
    problems = []
    for _ in range(5):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        problems.append((num1, num2))
    return problems

def generate_division_problems():
    problems = []
    for _ in range(5):
        num2 = random.randint(1, 9)
        answer = random.randint(1, 9)
        num1 = num2 * answer  # 割り切れる問題にする
        problems.append((num1, num2))
    return problems
