"""
---------------luyencode.net----------------------------------
---------------Problem: THPTTD_110-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-23 20:41:14.762678+07:00---------
"""
import sys
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
input_path = "game.inp"
output_path = "game.out" 
from os import path
if path.exists(input_path):
    sys.stdin = open(input_path,"r")
    sys.stdout = open(output_path,"w")
# --------------- Solve ---------------  # 

for _ in range(in1()):
    X, Y, N = in3()
    if N % 2:
        print(max(X * 2, Y) // min(X * 2, Y))
    else:
        print(max(X, Y) // min(X, Y))
##########################################
