"""
---------------luyencode.net----------------------------------
---------------Problem: FIBO1-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-07 23:41:37.475964+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
t = in1()
arr = in2()

from functools import cache
import sys
sys.setrecursionlimit(10000000)

dp = [1] * 10001
for i in range(2, 10001):
    dp[i] = dp[i - 1] + dp[i - 2]

for v in arr:
    print(dp[v])
##########################################
