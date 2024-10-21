"""
---------------luyencode.net----------------------------------
---------------Problem: SHEIGHT-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-12 22:30:29.563725+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
operator = set(['+', '-', '*', '/', '^'])
for i in range(in1()):
    s = input()

    stack = []
    ans = 0
    for c in s[::-1]:
        if c in operator:
            if stack:
                stack[-1] += 1
            stack.append(0)
            ans = max(ans, len(stack))
        else:
            if stack:
                stack[-1] += 1
            while stack and stack[-1] == 2:
                stack.pop()

    print(ans)
        
##########################################
