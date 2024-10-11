"""
---------------luyencode.net----------------------------------
---------------Problem: UOC2-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-10 22:12:04.074027+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
ans = 0
i = 1
a, b = in2()
while i * i <= a:
    if a % i == 0 and b % i == 0:
        ans += i
    if a % i == 0 and a // i != i and b % (a // i) == 0:
        ans += a // i
    i += 1

print(ans)
##########################################
