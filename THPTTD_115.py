"""
---------------luyencode.net----------------------------------
---------------Problem: THPTTD_115-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-29 23:03:39.715352+07:00---------
"""
import sys
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
__input = 'cfile'
input_path = f"{__input}.inp"
output_path = f"{__input}.out"
from os import path
if path.exists(input_path):
    sys.stdin = open(input_path,"r")
    sys.stdout = open(output_path,"w")
# --------------- Solve ---------------  # 
N = in1()
arr = in2()
arr.sort()
ans = 0
idx = 0
for i in range(1, N):
    while idx < i and arr[idx] < 0.9 * arr[i]:
        idx += 1
    ans += i - idx

print(ans)
##########################################
