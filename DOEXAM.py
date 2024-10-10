"""
---------------luyencode.net----------------------------------
---------------Problem: DOEXAM-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-10 08:56:45.048516+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n, k = in2()
d = in2()

dp = [0] * (n + 1)
dp[1] = d[0]
dp[2] = d[1]
for i in range(2, k + 1):
    for j in range(n, 1, -1):
        val = 0
        if dp[j - 1] != 0:
            val = d[j - 1] + dp[j - 1]
        if dp[j - 2] != 0:
            val = max(val, d[j - 1] + dp[j - 2]) 
        dp[j] = val

print(max(dp))
##########################################
