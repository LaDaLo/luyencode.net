"""
---------------luyencode.net----------------------------------
---------------Problem: TRAOGIAI-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-10 09:08:01.922259+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n = in1()
arr = in2()
val = n // 2
arr.sort(reverse=True)

ans = val

for i in range(val, n):
    if arr[i] == arr[val - 1]:
        ans += 1

print(ans)

##########################################
