"""
---------------luyencode.net----------------------------------
---------------Problem: PTIT005-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-21 20:59:31.443275+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
n = input()

if int(n) % sum(int(c) for c in n) == 0:
    print("YES")
else:
    print("NO")
##########################################
