"""
---------------luyencode.net----------------------------------
---------------Problem: KNAPSACK1-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-23 20:45:38.109384+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
input_path = "input.txt"
output_path = "output.txt" 
import sys
from os import path
if path.exists(input_path):
    sys.stdin = open(input_path,"r")
    sys.stdout = open(output_path,"w")
# --------------- Solve ---------------  # 

N, W = in3()
dp = [-1] * (W + 1)
dp[0] = 0
O = [in2() for _ in range(N)]
ans = 0
for i in range(N):
    w, v = O[i]
    for j in range(W, w - 1, -1):
        if dp[j - w] != -1:
            dp[j] = max(dp[j], dp[j - w] + v)
        ans = max(ans, dp[j])
print(ans)
##########################################
