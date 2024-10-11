"""
---------------luyencode.net----------------------------------
---------------Problem: MCAKE-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-11 22:36:31.156367+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n, L = in2()
empty = [True] * (L + 1)
x, y = 0, 0
for i in range(n):
    a, b = in2()
    x = max(x, b - a + 1)
    count = 0
    for j in range(a, b + 1):
        if empty[j]:
            count += 1
            empty[j] = False
    y = max(y, count)
print(x, y)
##########################################
