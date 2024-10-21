"""
---------------luyencode.net----------------------------------
---------------Problem: STRPN-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-12 16:13:05.653052+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
for i in range(in1()):
    s = input()
    operator = []
    ans = ""
    order = {'(' : 0, '+' : 1, '-' : 1, '*' : 2, '/' : 2, '^' : 3}   

    for c in s:
        if c == '(':
            operator.append(c)
        elif c in order: 
            while operator and order[operator[-1]] >= order[c]:
                ans += operator.pop()
            operator.append(c)
        elif c == ')':
            while operator and operator[-1] != '(':
                ans += operator.pop()
            operator.pop()
        else:
            ans += c
    while operator:
        ans += operator.pop()

    print(ans)
        
##########################################
