"""
---------------luyencode.net----------------------------------
---------------Problem: NUMTRANS-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-08 23:32:52.484224+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n = in1()
arr = input().split()

for val in sorted(arr)[::-1]:
	print(val, end='')

##########################################
