"""
---------------luyencode.net----------------------------------
---------------Problem: ENCRYPT-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-11 22:41:44.643060+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
s = input()
number = 0
for c in s:
    if c.isnumeric():
        number += int(c)
    else:
        print(c, end='')
print(number)
##########################################
