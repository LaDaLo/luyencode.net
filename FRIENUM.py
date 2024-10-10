"""
---------------luyencode.net----------------------------------
---------------Problem: FRIENUM-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-09 22:45:34.948718+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n = in1()
arr = in2()

from collections import Counter
d = Counter(arr)
ans = 0
for val in d.values():
    if val > 1:
        ans += val
print(ans)
##########################################
