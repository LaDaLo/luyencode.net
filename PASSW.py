"""
---------------luyencode.net----------------------------------
---------------Problem: PASSW-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-09 22:36:29.365635+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
for i in range(in1()):
    password = input()
    ans = min(5, max(len(password) - 5, 0))
    level_1, level_2, level_3 = 0, 0, 0
    for c in password:
        if c.isupper():
            level_1 = 1 
        elif c.islower():
            level_2 = 1
        elif c.isnumeric():
            level_3 = 1
    level = level_1 + level_2 + level_3
    match level:
        case 1:
            print(ans + 1, end=' ')
        case 2:
            print(ans + 2, end=' ')
        case 3:
            print(ans + 5, end=' ')
##########################################
