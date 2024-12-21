"""
---------------luyencode.net----------------------------------
---------------Problem: THPTTD_114-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-23 21:18:41.899577+07:00---------
"""
import sys
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# input_path = "input.inp"
# output_path = "output.out"
input_path = "bwater.inp"
output_path = "bwater.out" 
from os import path
if path.exists(input_path):
    sys.stdin = open(input_path,"r")
    sys.stdout = open(output_path,"w")
# --------------- Solve ---------------  # 
arr = in2()
amount = [0.25, 0.5, 1, 2]
N = in1()

sorted_arr = sorted([[arr[0] * 4, 0], [arr[1] * 2, 1], [arr[2], 2], [arr[3] / 2, 3]])
ans = 0
index = 0
while N != 0:
    if amount[sorted_arr[index][1]] == 2 and N < 2:
        index += 1
    else:
        if amount[sorted_arr[index][1]] == 0.25:
            k = N * 4
        elif amount[sorted_arr[index][1]] == 0.5:
            k = N * 2
        elif amount[sorted_arr[index][1]] == 1:
            k = N
        else:
            k = N // 2
        ans += k * arr[sorted_arr[index][1]]
        N -= k * amount[sorted_arr[index][1]]
        index += 1

print(ans)
##########################################
