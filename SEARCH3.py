"""
---------------luyencode.net----------------------------------
---------------Problem: SEARCH3-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-14 23:20:34.067255+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
n, m = in3()
A = {}
idx = 1
for v in in3():
    if v not in A:
        A[v] = idx
    idx += 1

for v in in3():
    if v in A:
        print(A[v], end=' ')
    else:
        print(0, end=' ')
##########################################
