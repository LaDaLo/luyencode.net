"""
---------------luyencode.net----------------------------------
---------------Problem: COMPCONN-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-12 15:00:31.328170+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
from collections import deque
n, m = in2()
graph = [set() for i in range(n + 1)]
for i in range(m):
    a, b = in2()
    graph[a].add(b)
    graph[b].add(a)

visited = [False] * (n + 1)
groups = []
queue = deque()
for v in range(1, n + 1):
    if not visited[v]:
        queue.append(v)
        visited[v] = True
        g = []
        while queue:
            current = queue.pop()
            g.append(current)
            for next in graph[current]:
                if not visited[next]:
                    visited[next] = True
                    queue.appendleft(next)
        groups.append(g)

print(len(groups))
for g in groups:
    print(len(g), end=' ')
    print(*sorted(g))

##########################################
