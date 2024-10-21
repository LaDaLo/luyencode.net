"""
---------------luyencode.net----------------------------------
---------------Problem: PTIT007-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-21 21:03:54.034169+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
import bisect
MIN = 1 
MAX = 512

def cal(b):
    ans = 0
    idx = 1
    for c in reversed(bin(b)[2:]):
        if c == '1':
            ans += idx
        idx *= 3
    return ans

for _ in range(in1()):
    N = in1()

    l, r = MIN, MAX
    while l < r:
        m = (r - l) // 2 + l
        if cal(m) >= N:
            r = m
        else:
            l = m + 1
    print(cal(l))

##########################################
