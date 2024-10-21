"""
---------------luyencode.net----------------------------------
---------------Problem: TRIBO-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-20 00:04:04.752231+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
# preprocess
tribo = [0, 0, 1]
while True:
    if tribo[-1] > 1000000000:
        break
    next = tribo[-1] + tribo[-2] + tribo[-3]
    tribo.append(next)

import sys
import bisect
for line in sys.stdin:
    n = int(line)
    idx = bisect.bisect_left(tribo, n)
    print(tribo[idx])
##########################################
