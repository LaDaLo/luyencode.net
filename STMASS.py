"""
---------------luyencode.net----------------------------------
---------------Problem: STMASS-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-12 22:22:27.789269+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
w = {'C' : 12, 'H' : 1, 'O' : 16}
for i in range(in1()):
    s = input()
    stack = []
    n = len(s)
    for idx in range(n):
        c = s[idx]
        if c == '(':
            stack.append(c)
        elif c.isnumeric():
            prev = stack.pop()
            stack.append(prev * int(c))
        elif c == ')':
            val = 0
            while stack[-1] != '(':
                val += stack.pop()
            stack.pop()
            stack.append(val)
        else:
            stack.append(w[c])
    print(sum(stack))

##########################################
