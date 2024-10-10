"""
---------------luyencode.net----------------------------------
---------------Problem: SMARTATM-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-06 23:34:31.019563+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n, m = in2()
arr = in2()

dp = [-1] * (m + 1)
dp[0] = 0
for v in arr:
    for j in range(v, m + 1):
        if dp[j - v] != -1:
            if dp[j] == -1:
                dp[j] = 1 + dp[j - v]
            else:
                dp[j] = min(dp[j], 1 + dp[j - v])

print(dp[m])
##########################################
