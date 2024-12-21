"""
---------------luyencode.net----------------------------------
---------------Problem: THPTTD_111-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-23 21:06:50.029931+07:00---------
"""
import sys
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# input_path = "input.inp"
# output_path = "output.out"
input_path = "countdiv.inp"
output_path = "countdiv.out" 
from os import path
if path.exists(input_path):
    sys.stdin = open(input_path,"r")
    sys.stdout = open(output_path,"w")
# --------------- Solve ---------------  # 
import math
for _ in range(in1()):
    L, R, a, b = in3()
    LCM = (a * b) // math.gcd(a, b)
    ans = 0
    ans += math.floor(R / a) - math.ceil(L / a) + 1
    ans += math.floor(R / b) - math.ceil(L / b) + 1
    ans -= math.floor(R / LCM) - math.ceil(L / LCM) + 1


    print(ans)
##########################################
