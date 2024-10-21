"""
---------------luyencode.net----------------------------------
---------------Problem: QUEUE-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-12 23:16:42.827751+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
from collections import deque

q = deque()
for i in range(in1()):
    query = in2()
    if query[0] == 1:
        q.append(query[1])
    elif query[0] == 2:
        if q:
            q.popleft()
    else:
        if q:
            print(q[0])
        else:
            print("Empty!")
##########################################
