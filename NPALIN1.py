"""
---------------luyencode.net----------------------------------
---------------Problem: NPALIN1-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-07 00:28:06.261982+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
import sys
for v in sys.stdin:
    ans = 9
    for i in range((int(v) - 1) // 2):
        ans *= 10
    print(ans)

##########################################
