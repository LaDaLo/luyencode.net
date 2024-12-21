"""
---------------luyencode.net----------------------------------
---------------Problem: THPTTD_117-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-11-04 22:59:09.945902+07:00---------
"""
import sys
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
__input = 'local'
input_path = f"{__input}.inp"
output_path = f"{__input}.out"
from os import path
if path.exists(input_path):
    sys.stdin = open(input_path,"r")
    sys.stdout = open(output_path,"w")
# --------------- Solve ---------------  # 
n, x = in3()
import math
ans = 0
for i in range(1, int(math.sqrt(x)) + 1):
    if x % i == 0:
        x1 = x // i
        x2 = x // x1
        if x1 <= n and x2 <= n:
            ans += 2
            if x1 == x2:
                ans -= 1

print(ans)
##########################################
