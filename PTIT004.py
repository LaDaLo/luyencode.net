"""
---------------luyencode.net----------------------------------
---------------Problem: PTIT004-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-21 20:56:37.843508+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
s = input()
while len(s) > 1:
    s = str(sum(int(v) for v in s))

print(s)
##########################################
