"""
---------------luyencode.net----------------------------------
---------------Problem: FLOWER-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-11 22:01:24.123817+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n, m = in2()
arr = [in2() for i in range(n)]

dp = [-1] * (m)
dp[0] = arr[0][0]
for i in range(1, m):
    if arr[0][i] != -1 and dp[i - 1] != -1:
        dp[i] = arr[0][i] + dp[i - 1]

for i in range(1, n):
    for j in range(m):
        val = -1
        if arr[i][j] != -1:
            if j > 0 and dp[j - 1] != -1:
                val = dp[j - 1] + arr[i][j]
            if dp[j] != -1:
                val = max(val, dp[j] + arr[i][j])
        dp[j] = val
print(dp[m - 1])
    
##########################################
