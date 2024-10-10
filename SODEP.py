"""
---------------luyencode.net----------------------------------
---------------Problem: SODEP-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-07 09:29:09.121868+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
import sys

def check(n):
    temp1, temp2, sum = n, 0, 0
    while n:
        temp2 = temp2 * 10 + n % 10
        sum += n % 10
        n //= 10
    return (temp1 == temp2) and (sum % 10 == 0)

for line in sys.stdin:
    l, r = list(map(int, line.split()))

    ans = 0
    for i in range(l, r + 1):
        if check(i):
            ans += 1

    print(ans)
    ans = 0
##########################################
