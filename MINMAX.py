"""
---------------luyencode.net----------------------------------
---------------Problem: MINMAX-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-07 23:53:40.010820+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n = in1()
arr = in2()
min_val, min_idx, max_val, max_idx = arr[0], 0, arr[0], 0

for i in range(n):
    if arr[i] < min_val:
        min_val = arr[i]
        min_idx = i
    if arr[i] > max_val:
        max_val = arr[i]
        max_idx = i
print(min_val, min_idx + 1, max_val, max_idx + 1)
##########################################
