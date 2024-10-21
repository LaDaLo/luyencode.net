"""
---------------luyencode.net----------------------------------
---------------Problem: SEARCH2-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-12 15:22:25.111847+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n, m = in2()
a = in2()
b = in2()

from bisect import bisect_left
for v in b:
    idx = bisect_left(a, v)
    if idx < n and a[idx] == v:
        print(idx + 1, end=' ')
    else:
        print(0, end=' ')
##########################################
