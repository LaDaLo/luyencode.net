"""
---------------luyencode.net----------------------------------
---------------Problem: LDIGIT2-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-19 13:42:56.574963+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
a, n = in3()
temp = a % 10
ans = 1
for i in range(1, n + 1):
    ans = ans * temp
    ans %= 10
print(ans)
##########################################
