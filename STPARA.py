"""
---------------luyencode.net----------------------------------
---------------Problem: STPARA-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-12 22:08:53.178025+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
stack = []
while True:
    n = in1()
    if n == 0:
        break
    arr = in2()
    idx = 1
    for v in arr:
        if v == idx:
            idx += 1
        else:
            stack.append(v)
        while stack and stack[-1] == idx:
            idx += 1
            stack.pop()
    if idx == n + 1:
        print("yes")
    else:
        print("no")
##########################################
