"""
---------------luyencode.net----------------------------------
---------------Problem: PQUEUE-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-13 10:18:42.252225+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
import heapq

heap = []
for i in range(in1()):
    query = input()
    if query[0] == '+':
        if len(heap) < 15000:
            heapq.heappush(heap, -int(query[1:]))
    else:
        if heap:
            val = heapq.heappop(heap)
            while heap and heap[0] == val:
                heapq.heappop(heap)
            


ans = []
while heap:
    val = -heapq.heappop(heap)
    if not ans or ans[-1] != val:
        ans.append(val)

print(len(ans))
print(*ans)
    

##########################################
