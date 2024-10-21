"""
---------------luyencode.net----------------------------------
---------------Problem: SEQ-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-19 23:33:56.069223+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
import sys
sys.setrecursionlimit(10000000)
n, k = in3()
arr = in2()
dp = [[0] * k for _ in range(2)]

if k > 1:
    dp[0][1] = arr[0]

for i in range(1, n):
    for j in range(1, k):
        dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + arr[i]
    
    dp[i % 2][0] = max(dp[(i - 1) % 2])

print(max(dp[(n - 1) % 2]))

##########################################
