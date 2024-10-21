"""
---------------luyencode.net----------------------------------
---------------Problem: MEDIAN-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-12 21:15:36.841523+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n, m = in2()
arr = in2()

idx_l = n // 2 - 1
idx_r = n // 2
for i in range(m):
    if n % 2:
        print(arr[idx_r], end=' ')
        idx_r += 1
    else:
        print(arr[idx_l], end=' ')
        idx_l -= 1
    n -= 1

##########################################
