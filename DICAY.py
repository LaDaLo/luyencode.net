"""
---------------luyencode.net----------------------------------
---------------Problem: DICAY-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-19 14:00:53.526741+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
n, S = in3()
t = in2()
d = in2()
MAX_POINT = sum(d)
dp = [-1] * (MAX_POINT + 1)
dp[0] = 0
ans = 0
for i in range(n):
    for j in range(MAX_POINT, d[i] - 1, - 1):
        if dp[j - d[i]] != -1 and dp[j - d[i]] + t[i] <= S:
            if dp[j] != -1:
                dp[j] = min(dp[j - d[i]] + t[i], dp[j])
            else:
                dp[j] = dp[j - d[i]] + t[i]
            ans = max(ans, j)

print(ans)
##########################################
