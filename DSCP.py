"""
---------------luyencode.net----------------------------------
---------------Problem: DSCP-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-06 23:28:52.033783+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
import math
l, r = in2()
sqr_l = math.ceil(math.sqrt(l))
sqr_r = math.floor(math.sqrt(r))

print(sqr_r - sqr_l + 1)

##########################################
