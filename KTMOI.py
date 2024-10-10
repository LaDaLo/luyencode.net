"""
---------------luyencode.net----------------------------------
---------------Problem: KTMOI-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-07 23:23:00.685526+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n, m = in2()
arr = [input() for i in range(n)]

ans = 0
def count(l):
    return max(0, l - 1)

for i in range(n):
    length = 0
    for j in range(m):
        if arr[i][j] == '.':
            length += 1
        else:
            ans += count(length)
            length = 0
    ans += count(length)

for j in range(m):
    length = 0
    for i in range(n):
        if arr[i][j] == '.':
            length += 1
        else:
            ans += count(length)
            length = 0
    ans += count(length)

print(ans)

##########################################
