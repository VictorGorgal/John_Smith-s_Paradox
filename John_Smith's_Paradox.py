import random


def dice():  # returns a dice roll
    return random.randint(1, 6)


SAMPLE_SIZE = 20_000

A_wins = 0
B_wins = 0
C_wins = 0

for _ in range(SAMPLE_SIZE):
    A = [dice() for _ in range(6)]  # player A flings 6 dices
    B = [dice() for _ in range(12)]  # player B flings 12 dices
    C = [dice() for _ in range(18)]  # player C flings 18 dices

    if A.count(6) >= 1:  # player A wins if they roll at least 1 six
        A_wins += 1

    if B.count(6) >= 2:  # player B wins if they roll at least 2 sixes
        B_wins += 1

    if C.count(6) >= 3:  # player C wins if they roll at least 3 sixes
        C_wins += 1


print(f'In {SAMPLE_SIZE} games, the result was:')
print(f'A: {A_wins / SAMPLE_SIZE * 100 :.3f}% wins')
print(f'B: {B_wins / SAMPLE_SIZE * 100 :.3f}% wins')
print(f'C: {C_wins / SAMPLE_SIZE * 100 :.3f}% wins')
