"""
---------------luyencode.net----------------------------------
---------------Problem: LKNGOAC-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-12 16:10:30.229756+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
stack = []
s = input()
for i in range(len(s)):
    if s[i] == '(':
        stack.append(i + 1)
    else:
        print(stack.pop(), i + 1)
##########################################
