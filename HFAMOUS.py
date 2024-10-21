"""
---------------luyencode.net----------------------------------
---------------Problem: HFAMOUS-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-14 22:44:12.408843+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
from collections import deque

n, m, k = in2()
graph = [set() for _ in range(n + 1)]
for _ in range(m):
    u, v = in3()
    graph[u].add(v)
    graph[v].add(u)
# visited = [False] * (n + 1)
eliminated = [False] * (n + 1)
level = [len(graph[i]) for i in range(n + 1)]
q = deque()

for i in range(1, n + 1):
    if level[i] < k:
        q.appendleft(i)
        eliminated[i] = True

while q:
    current = q.pop()

    for next in graph[current]:
        if not eliminated[next]:
            level[next] -= 1
            if level[next] < k:
                q.appendleft(next)
                eliminated[next] = True

total = sum(1 for i in range(1, n + 1) if eliminated[i] == False)
print(total)
for i in range(1, n + 1):
    if not eliminated[i]:
        print(i, end=' ')

##########################################
