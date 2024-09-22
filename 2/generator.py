# Problem generator
# n, k: n people in k groups
# unfamiliarity: unfamiliarity[i][j] is the unfamiliarity between person i and person j, symmetric

import random
from solution import solve
from backtrack import brute_solve

def generate():
    n= random.randint(1, 7)
    k= random.randint(1, n)

    unfamiliarity = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            unfamiliarity[i][j]= random.randint(1, 100)
            unfamiliarity[j][i]= unfamiliarity[i][j]

    return n, k, unfamiliarity

def trying():
    for i in range(1000):
        n, k, unfamiliarity= generate()
        assert solve(n, k, unfamiliarity) == brute_solve(n, k, unfamiliarity)

if __name__ == "__main__":
    trying()