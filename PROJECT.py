"""
---------------luyencode.net----------------------------------
---------------Problem: PROJECT-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-08 23:36:41.975356+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n, S = in2()
C = in2()
P = in2()

dp = [0] * (S + 1)
for i in range(n):
    for j in reversed(range(C[i], S + 1)):
        dp[j] = max(dp[j], dp[j - C[i]] + P[i])

print(dp[S])
##########################################
