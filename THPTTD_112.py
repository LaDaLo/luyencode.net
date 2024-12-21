"""
---------------luyencode.net----------------------------------
---------------Problem: THPTTD_112-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-28 21:55:17.792214+07:00---------
"""
import sys
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
input_name = 'average'
input_path = f"{input_name}.inp"
output_path = f"{input_name}.out"
from os import path
if path.exists(input_path):
    sys.stdin = open(input_path,"r")
    sys.stdout = open(output_path,"w")
# --------------- Solve ---------------  # 
n = in1()
arr = in2()
max_val = max(arr)
ans = 1
left = 0
while left < n:
    if arr[left] == max_val:
        right = left
        while right < n and arr[right] == arr[left]:
            right += 1
        ans = max(ans, right - left)
        left = right
    left += 1

print(ans)
##########################################
