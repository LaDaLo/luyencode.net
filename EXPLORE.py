"""
---------------luyencode.net----------------------------------
---------------Problem: EXPLORE-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-21 18:02:14.568213+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
T, N = in3()
dest = [in1() for _ in range(N)]
ans = 0
prev = 0
t = 0
for val in sorted(dest, key=lambda x : abs(x)):
    if abs(prev - val) + t <= T:
        ans += 1
        t += abs(prev - val)
        prev = val
    else:
        break
print(ans)
##########################################
