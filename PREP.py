"""
---------------luyencode.net----------------------------------
---------------Problem: PREP-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-11 21:48:50.720954+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
a, b, x, y = in2()
print(a * x + b * y)
##########################################