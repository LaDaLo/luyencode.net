"""
---------------luyencode.net----------------------------------
---------------Problem: THPTTD_108-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-23 20:15:58.771550+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
import sys
sys.stdin = open("countpairs.inp", "r")
sys.stdout = open("countpairs.out", "w")

for _ in range(in1()):
    K = in1()
    ans = 0

    for a in range(1, K // 2 + 1):
        l = a + 1
        r = K - a
        ans += r - l + 1
    print(ans)
##########################################
