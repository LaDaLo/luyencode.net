"""
---------------luyencode.net----------------------------------
---------------Problem: LCOJ-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-19 23:01:38.926490+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
a = input()
b = input()
n, m = len(a), len(b)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = 1 + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

print(dp[n][m])
##########################################
