"""
---------------luyencode.net----------------------------------
---------------Problem: GACHO-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-19 13:48:16.845394+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
m, n = in3()
# x + y = m
# 4x + 2y = n
# y = (4m - n) / 2
# x = m - y
if (4 * m - n) % 2 == 0:
    y = (4 * m - n) // 2
    x = m - y
    if x >= 0 and y >= 0:
        print(y, x)
    else:
        print(-1)
else:
    print(-1)
##########################################
