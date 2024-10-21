"""
---------------luyencode.net----------------------------------
---------------Problem: STACK-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-12 16:06:33.996909+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
stack = []
for i in range(in1()):
    query = in2()
    if query[0] == 1:
        stack.append(query[1])
    elif query[0] == 2:
        if stack:
            stack.pop()
    else:
        if stack:
            print(stack[-1])
        else:
            print("Empty!")
##########################################
