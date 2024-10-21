"""
---------------luyencode.net----------------------------------
---------------Problem: CONCERT-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-12 21:29:17.061327+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n = in1()
arr = in2()
stack = []
ans = 0
for v in arr:
    if not stack:
        stack.append((v, 0))
    else:
        if stack[-1][0] == v:
            prev = stack.pop()
            if stack: 
                ans += prev[1] + 2
            else:
                ans += prev[1] + 1
            stack.append((v, prev[1] + 1))
        elif stack[-1][0] < v:
            while stack and stack[-1][0] < v:
                prev = stack.pop()
                ans += prev[1] + 1
            if stack and stack[-1][0] == v:
                prev = stack.pop()
                if stack: 
                    ans += prev[1] + 1 + stack[-1][1] + 1
                else:
                    ans += prev[1] + 1
                stack.append((v, prev[1] + 1))
            elif stack:
                ans += 1
                stack.append((v, 0))
            else:
                stack.append((v, 0))
        else:
            ans += 1
            stack.append((v, 0))
print(ans)

##########################################
