import sys

N = 4002
dp = [[float('inf')] * N for _ in range(N)]
prefix = [[0] * N for _ in range(N)]
n, k = 0, 0

def initialize():
    global N, dp, prefix, n, k
    N = 4002
    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    prefix = [[0] * (n+1) for _ in range(n+1)]

def cost(l, r):
    return (prefix[r][r] - prefix[l - 1][r] - prefix[r][l - 1] + prefix[l - 1][l - 1]) // 2


def compute(group, l, r, optL, optR):
    if l > r:
        return
    mid = (l + r) // 2
    opt = -1
    for i in range(optL, min(mid, optR + 1) + 1):
        val = dp[i][group - 1] + cost(i + 1, mid)
        if val <= dp[mid][group]:
            dp[mid][group] = val
            opt = i
    compute(group, l, mid - 1, optL, opt)
    compute(group, mid + 1, r, opt, optR)


def solve(n_,k_,unfamiliarity):
    global n, k
    n, k = n_, k_

    initialize()

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            prefix[i][j] = prefix[i][j - 1] + prefix[i - 1][j] - prefix[i - 1][j - 1] + unfamiliarity[i - 1][j - 1]

    for i in range(1, n + 1):
        dp[i][1] = cost(1, i)

    for g in range(2, k + 1):
        compute(g, 1, n, 1, n)

    return dp[n][k]


if __name__ == "__main__":
    solve()
