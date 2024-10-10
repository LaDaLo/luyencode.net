"""
---------------luyencode.net----------------------------------
---------------Problem: SCBN2-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-08 08:11:36.241740+07:00---------
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

def cal(val):
    n = 1
    for i in range(2, val + 1):
        n *= i
    d = 2
    for i in range(2, val - 1):
        d *= i
    return n // d

for val in d.values():
    ans += cal(val)

print(ans)
##########################################
