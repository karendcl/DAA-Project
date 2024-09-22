import sys
from collections import defaultdict
from math import inf



MOD = 10**9 + 7
N = 1000 + 77

# Binary Exponentiation in Python
def binpow(a, b):
    if b == 0:
        return 1
    val = binpow(a, b // 2)
    if b % 2 == 0:
        return val * val % MOD
    else:
        return val * val * a % MOD

n = 0
k = 0
ans = inf

g = defaultdict(list)
dpr = [[[] for _ in range(N)] for _ in range(N)]
dp = [[inf] * N for _ in range(N)]
rebro = [[0] * N for _ in range(N)]
answ = []

# DFS (Depth-First Search)
def dfs(v, p=0):
    global ans, answ

    dp[v][1] = 0
    for to in g[v]:
        if to != p:
            dfs(to, v)
            for i in range(n, 0, -1):
                if dp[v][i] > 500:
                    continue
                for j in range(1, n + 1):
                    if dp[v][i + j] > dp[to][j] + dp[v][i]:
                        dp[v][i + j] = dp[to][j] + dp[v][i]
                        dpr[v][i + j] = dpr[to][j].copy()
                        for ab in dpr[v][i]:
                            dpr[v][i + j].append(ab)
                dp[v][i] += 1
                dpr[v][i].append(rebro[v][to])

    if dp[v][k] + (p != 0) < ans:
        ans = dp[v][k] + (p != 0)
        answ = dpr[v][k].copy()
        if p:
            answ.append(rebro[p][v])

# Main function to solve the problem
def solve(n_,k_,edges):
    global n, k, ans

    n, k = n_, k_
    index = 1
    for i in edges:
        v, u = i
        g[v].append(u)
        g[u].append(v)
        rebro[v][u] = rebro[u][v] = index
        index += 1

    for i in range(n + 1):
        for j in range(k + 1):
            dp[i][j] = inf

    ans = inf
    dfs(1)

    print(len(answ))
    print(' '.join(map(str, answ)))



