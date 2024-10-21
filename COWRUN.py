"""
---------------luyencode.net----------------------------------
---------------Problem: COWRUN-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-19 17:08:38.755032+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
n, m = in3()
D = [0] * n
for i in range(n):
    D[i] = in1()

dp = [[-1] * 2 for _ in range(n + 1)]
dp[n][m] = 0

for i in range(n - 1, -1, -1):
    if dp[i + 1][m - 1] != -1:
        dp[i][m] = max(D[i] + dp[i + 1][m - 1], dp[i + 1][m])
    else:
        dp[i][m] = dp[i + 1][m]

    for j in range(1, m):
        if dp[i + 1][j - 1] != -1 and dp[i + 1][j + 1] != -1:
            dp[i][j] = max(D[i] + dp[i + 1][j - 1], dp[i + 1][j + 1])
        elif dp[i + 1][j - 1] != -1:
            dp[i][j] = D[i] + dp[i + 1][j - 1]
        elif dp[i + 1][j + 1] != -1:
            dp[i][j] = dp[i + 1][j + 1]
    
    if dp[i + 1][1] != -1:
        dp[i][0] = dp[i + 1][1]

print(dp[0][m])


##########################################
