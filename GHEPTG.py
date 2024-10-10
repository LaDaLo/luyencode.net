"""
---------------luyencode.net----------------------------------
---------------Problem: GHEPTG-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-09 22:24:59.086346+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
a, b, c = in2()

ans = float("inf")
ans = min(ans, max(0, c - a - b, b - a - c, a - b - c))
if ans == 0:
    print(ans)
else:
    print(ans + 1)

##########################################
