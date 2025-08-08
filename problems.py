import random

def generate_addition_problems(stage=1, num_problems=5):
    problems = []
    digit = stage  # ステージ1→1桁、2→2桁、3→3桁...

    for _ in range(num_problems):
        max_num = 10 ** digit - 1
        a = random.randint(1, max_num)
        b = random.randint(1, max_num)
        problems.append({"a": a, "b": b, "answer": a + b})
    
    return problems
