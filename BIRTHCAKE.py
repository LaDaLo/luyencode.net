"""
---------------luyencode.net----------------------------------
---------------Problem: BIRTHCAKE-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-13 10:48:03.392497+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
import heapq

N, T = list(in2())
cakes = (in2() for i in range(N))
ans = 0
heap = []
used = 0
for x, t in cakes:
    heapq.heappush(heap, -t)
    used += t
    while heap and T - x < used:
        used += heapq.heappop(heap)
    ans = max(ans, len(heap))

print(ans)

##########################################
