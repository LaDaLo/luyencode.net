"""
---------------luyencode.net----------------------------------
---------------Problem: FLASHMOB-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-09 22:19:51.249688+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
winner = [0] * 34
has_flag = 0
c, n = in2()
winner[c] = 1
has_flag = c
for i in range(n):
    a, b = in2()
    if has_flag == b:
        has_flag = a
        winner[a] = 1

print(has_flag, sum(winner))
##########################################
