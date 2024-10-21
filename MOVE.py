"""
---------------luyencode.net----------------------------------
---------------Problem: MOVE-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-19 23:21:32.655955+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
n, m = in3()
arr = [in2() for _ in range(n)]

dp = [[0] * m for _ in range(2)]
for i in range(m):
    dp[0][i] = (i > 0) * dp[0][i - 1] + arr[0][i]

for i in range(1, n):
    dp[i % 2][0] = dp[(i - 1) % 2][0] + arr[i][0]
    for j in range(1, m):
        dp[i % 2][j] = max(dp[i % 2][j - 1] + arr[i][j], dp[(i - 1) % 2][j] + arr[i][j])

print(dp[(n - 1) % 2][m - 1])

##########################################
