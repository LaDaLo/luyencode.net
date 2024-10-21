"""
---------------luyencode.net----------------------------------
---------------Problem: LDIGIT1-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-19 13:11:11.620123+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
n = in1()

def sol1(n):
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i

        while (ans != 0) and ans % 10 == 0:
            ans = ans // 10
        
        ans = ans % 10000
    return ans % 10


print(sol1(n))
##########################################
