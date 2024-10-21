"""
---------------luyencode.net----------------------------------
---------------Problem: WOODCUT-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-13 10:29:27.297890+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
import heapq

n = in1()
arr = in2()

ans = 0
heapq.heapify(arr)

while len(arr) > 1:
    l1 = heapq.heappop(arr)
    l2 = heapq.heappop(arr)
    ans += l1 + l2
    heapq.heappush(arr, l1 + l2)

print(ans)
##########################################
