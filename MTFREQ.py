"""
---------------luyencode.net----------------------------------
---------------Problem: MTFREQ-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-07 23:39:49.004378+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n = in1()
arr = in2()

from collections import Counter
count = Counter(arr)

print(len(count))
for key, value in count.items():
    print(key, value)
##########################################
