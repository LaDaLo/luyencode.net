"""
---------------luyencode.net----------------------------------
---------------Problem: TTBFS-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-12 14:37:42.105598+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n, m = in2()
child = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = in2()
    child[a].append(b)
    child[b].append(a)

from collections import deque
q = deque()
q.append(1)
visited = [False] * (n + 1)
visited[0] = visited[1] = True
while True:
    while q:
        current = q.pop()
        print(current)
        for next in sorted(child[current]):
            if not visited[next]:
                q.appendleft(next)
                visited[next] = True
    if all(visited):
        break

    for v in range(2, n + 1):
        if not visited[v]:
            q.append(v)
            visited[v] = True
            break

##########################################
