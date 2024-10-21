"""
---------------luyencode.net----------------------------------
---------------Problem: LAKE-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-21 17:35:32.939487+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
import sys
sys.setrecursionlimit(10000000)
ans = 0
n, m, k = in3()
flooded = [[False] * (m + 1) for _ in range(n + 1)]
for i in range(k):
    x, y = in3()
    flooded[x][y] = True

visited = [[False] * (m + 1) for _ in range(n + 1)]

def dfs(x, y):
    if x > n or y > m or x < 1 or y < 1:
        return 0
    if not flooded[x][y] or visited[x][y]:
        return 0
    visited[x][y] = True
    return 1 + dfs(x + 1, y) + dfs(x, y + 1) + dfs(x, y - 1) + dfs(x - 1, y)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if flooded[i][j] and not visited[i][j]:
            size = dfs(i, j)
            ans = max(ans, size)
print(ans)
##########################################
