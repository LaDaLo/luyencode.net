"""
---------------luyencode.net----------------------------------
---------------Problem: FANUM-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-10 20:10:56.977005+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n = in1()
arr = in2()
from collections import Counter1
d = Counter(arr)
print(sum(1 for i in d.keys() if d[i] == 1))
##########################################
