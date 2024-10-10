"""
---------------luyencode.net----------------------------------
---------------Problem: MKRECT-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-07 23:46:49.190427+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n = in1()
arr = in2()

from collections import Counter
d = Counter(arr)

d1, d2 = -1, -1
for key in sorted(d.keys(), key=lambda x: -x):
    if d[key] >= 2:
        if d1 == -1:
            d1 = key
            if d[key] >= 4:
                d2 = key
                break
        elif d2 == -1:
            d2 = key
        else:
            break
if d1 == -1 or d2 == -1:
    print(0)
else:
    print(d1 * d2)
##########################################
