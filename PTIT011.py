"""
---------------luyencode.net----------------------------------
---------------Problem: PTIT011-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-22 20:15:57.634745+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
import math
n = in1()

if n < 6:
    print("NO")
else:
    # case 1
    delta = 1 + 8 * n
    x = int(math.sqrt(delta))
    check_1, check_2 = False, False
    if x * x == delta:
        check_1 = True
    # case 2
    x = int(math.sqrt(n))
    if x * x == n:
        check_2 = True

    if check_1 or check_2:
        print("YES")
    else:
        print("NO")
##########################################
