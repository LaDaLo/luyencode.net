"""
---------------luyencode.net----------------------------------
---------------Problem: CVB2D-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-07 23:58:20.725231+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
t = in1()
for i in range(t):
    s = input()
    print(int(s, 16))

##########################################
