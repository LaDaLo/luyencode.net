"""
---------------luyencode.net----------------------------------
---------------Problem: KNAP-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-19 22:48:56.672357+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
n, M = in3()
arr = []
for i in range(n):
    arr[i][0], arr[i][1] = in3()
    arr.append(arr[i][0], arr[i][1])

dp = [0] * (M + 1)
ans = 0
for i in range(n):
    for j in range(M, arr[i][0] - 1, -1):
        dp[j] = max(dp[j], arr[i][1] + dp[j - arr[i][0]])
        ans = max(ans, dp[j])

print(ans)
##########################################
