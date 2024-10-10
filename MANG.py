"""
---------------luyencode.net----------------------------------
---------------Problem: MANG-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-10 08:48:15.498575+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n = in1()
arr = in2()
print(sum(arr), sum(1 for i in arr if i % 2 == 0), max(arr[max([0] + [idx for idx in range(n) if arr[idx] > 0])], 0))
##########################################
